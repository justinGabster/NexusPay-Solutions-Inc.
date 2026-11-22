# Phase 4: Final Technical Documentation
**Project Title:** Enterprise Network Design for NexusPay Solutions
**Course:** Networking Capstone

---

## 1. Executive Summary & Statement of Work
**NexusPay Solutions, Inc.** is a rapidly growing FinTech startup founded in 2024 that provides secure digital wallet APIs and POS terminal integrations. As part of our infrastructure overhaul, this project implements a highly structured, secure, and robust enterprise network environment capable of supporting 150+ internal employees and up to 20 concurrent guests.

### Key Business Goals Achieved:
* **Segregation & Security:** Implemented strict VLAN segmentation separating highly sensitive departments (Finance, Executive) from general staff (HR, IT, Dev).
* **Compliance Sandbox:** Created a dedicated Guest Network (VLAN 60) governed by Access Control Lists (ACLs) to strictly isolate visitors from internal financial data, while permitting access to a public FTP server and the Internet.
* **High Availability:** Configured First Hop Redundancy Protocol (FHRP / HSRP) and Spanning Tree Protocol (STP) across core multilayer switches to ensure 99.9% uptime, as required for processing real-time digital payments.

---

## 2. IP Addressing Scheme & VLSM Table
The internal network operates on the `192.168.10.0/24` block, divided efficiently using VLSM to accommodate host requirements while preventing IP waste.

| VLAN ID | Department Name | Required Hosts | Subnet / CIDR | Usable IP Range | Default Gateway (VIP) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VLAN 30** | Core Engineering (Dev) | 50 | **/26** | `192.168.10.1 - .62` | `192.168.10.1` |
| **VLAN 20** | IT Ops & NetSec | 20 | **/27** | `192.168.10.65 - .94` | `192.168.10.65` |
| **VLAN 50** | Human Resources (HR) | 20 | **/27** | `192.168.10.97 - .126` | `192.168.10.97` |
| **VLAN 60** | Guest Network | 20 | **/27** | `192.168.10.129 - .158` | `192.168.10.129` |
| **VLAN 10** | Executive & Management | 15 | **/27** | `192.168.10.161 - .190` | `192.168.10.161` |
| **VLAN 40** | Finance & Payroll | 15 | **/27** | `192.168.10.193 - .222` | `192.168.10.193` |
| **VLAN 70** | Server Farm (DC) | 10 | **/28** | `192.168.10.225 - .238` | `192.168.10.225` |
| **VLAN 99** | Native / Management | N/A | **/28** | `192.168.10.241 - .254` | `192.168.10.241` |

---

## 3. Network Design & Configuration Details
### Routing & Switching Core
* **Inter-VLAN Routing** is managed by two Cisco Layer 3 Core Switches.
* **HSRP (Hot Standby Router Protocol)** is configured across the SVIs of both Core Switches. Core-Sw-A acts as the Active gateway (`priority 110`), and Core-Sw-B acts as Standby (`priority 90`). 
* **DHCP Services** are centralized on a dedicated server in the Server Farm (VLAN 70). The Core switches use `ip helper-address 192.168.10.230` to forward broadcast DHCP requests across VLANs.

### Security Implementation (ACL)
To meet PCI-DSS compliance and secure the internal network, an Extended ACL was applied inbound on the Guest VLAN (VLAN 60).
```text
ip access-list extended GUEST_RESTRICTION
 permit udp any any eq bootpc
 permit udp any any eq bootps
 permit udp 192.168.10.128 0.0.0.31 any eq domain
 permit tcp 192.168.10.128 0.0.0.31 host 192.168.10.231 eq ftp
 permit tcp 192.168.10.128 0.0.0.31 host 192.168.10.231 eq ftp-data
 deny ip 192.168.10.128 0.0.0.31 192.168.10.0 0.0.0.255
 permit ip 192.168.10.128 0.0.0.31 any
```
* **Explanation:** Allows DHCP and DNS traffic. Allows FTP traffic specifically to the FTP server (`.231`). Explicitly denies all other traffic destined to the `192.168.10.0/24` internal network. Allows all other traffic (Internet bound).

---

## 4. Testing & Verification
*(The following tests were successfully verified in the Packet Tracer simulation by the engineering team (VJ). See Verification Check document for screenshots.)*

1. **DHCP Verification:** After resolving a Native VLAN mismatch (VLAN 1 vs 99) on the Core-to-Access trunk links, PCs successfully pulled IPs (e.g., `192.168.10.11`) dynamically from the central DHCP server.
2. **Inter-VLAN Routing:** Verified via `ping` from PC0 to internal gateways (`192.168.10.1` and `192.168.10.65`), achieving 100% success.
3. **High Availability Failover (HSRP):** Verified via `show standby brief` on the Core switches. Core-SW-A correctly assumed the **Active** role, while Core-SW-B correctly assumed the **Standby** role.
4. **Guest ACL Verification:** Verified from PC3 (VLAN 60 Guest). Pings to internal networks (e.g., `192.168.10.1`) returned "Destination host unreachable", confirming strict network segregation.
5. **FTP Access:** Internal PCs successfully connected to `192.168.10.231` via FTP and authenticated using guest credentials.
