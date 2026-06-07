# Phase 2: Network Design & Architecture

## 1. VLSM IP Addressing Scheme Table

To adhere to best practices for the **NexusPay Solutions** FinTech environment, we will use a Class C private network block **`192.168.10.0/24`** for all internal employee and guest VLANs. 

By applying Variable Length Subnet Masking (VLSM), we allocate subnets starting with the largest host requirement down to the smallest to ensure zero IP waste.

### Internal Network: `192.168.10.0/24`

| VLAN ID | Department Name | Required Hosts | Subnet / CIDR | Subnet Mask | Network Address | Usable IP Range | Broadcast Address | Default Gateway |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **VLAN 30** | Core Engineering (Dev) | 50 | **/26** | `255.255.255.192` | `192.168.10.0` | `192.168.10.1 - 192.168.10.62` | `192.168.10.63` | `192.168.10.1` |
| **VLAN 20** | IT Ops & NetSec | 20 | **/27** | `255.255.255.224` | `192.168.10.64` | `192.168.10.65 - 192.168.10.94` | `192.168.10.95` | `192.168.10.65` |
| **VLAN 50** | Human Resources (HR) | 20 | **/27** | `255.255.255.224` | `192.168.10.96` | `192.168.10.97 - 192.168.10.126` | `192.168.10.127` | `192.168.10.97` |
| **VLAN 60** | Guest Network | 20 | **/27** | `255.255.255.224` | `192.168.10.128` | `192.168.10.129 - 192.168.10.158` | `192.168.10.159` | `192.168.10.129` |
| **VLAN 10** | Executive & Management | 15 | **/27** | `255.255.255.224` | `192.168.10.160` | `192.168.10.161 - 192.168.10.190` | `192.168.10.191` | `192.168.10.161` |
| **VLAN 40** | Finance & Payroll | 15 | **/27** | `255.255.255.224` | `192.168.10.192` | `192.168.10.193 - 192.168.10.222` | `192.168.10.223` | `192.168.10.193` |
| **VLAN 70** | Server Farm (DC) | 10 | **/28** | `255.255.255.240` | `192.168.10.224` | `192.168.10.225 - 192.168.10.238` | `192.168.10.239` | `192.168.10.225` |
| **VLAN 99** | Native / Management | N/A | **/28** | `255.255.255.240` | `192.168.10.240` | `192.168.10.241 - 192.168.10.254` | `192.168.10.255` | `192.168.10.241` |

*(Note: The Default Gateway for each VLAN is traditionally the first usable IP address in its subnet. This will be configured on the respective Router sub-interfaces or Layer 3 Switch Virtual Interfaces (SVIs).)*

### Point-to-Point Transit Links (Infrastructure Routing)
For the transit links connecting the Core Switches to the Edge Routers, we will use a completely separate address space `10.0.0.0/30` to maximize security and strictly segment infrastructure traffic from user traffic.

| Connection | Subnet / CIDR | Subnet Mask | Network Address | Usable IP Range |
| :--- | :--- | :--- | :--- | :--- |
| **Core Sw-A to Edge Router 1** | **/30** | `255.255.255.252` | `10.0.0.0` | `10.0.0.1 - 10.0.0.2` |
| **Core Sw-B to Edge Router 2** | **/30** | `255.255.255.252` | `10.0.0.4` | `10.0.0.5 - 10.0.0.6` |
| **Edge Router to ISP** | **/30** | `255.255.255.252` | `203.0.113.0` | `203.0.113.1 - 203.0.113.2` |

---

## 2. Logical Network Topology

To successfully visualize and build this in Cisco Packet Tracer, the following topology guidelines apply:

1. **Edge Level:** The Edge Router acts as the boundary, connecting to the Internet (ISP).
2. **Core/Distribution Level:** Two Cisco 3650 Multilayer Switches will act as the Core. They will run FHRP (e.g., HSRP) to provide a virtual IP (VIP) as the default gateway for all VLANs, ensuring that if Core Sw-A goes down, Core Sw-B seamlessly takes over.
3. **Access Level:** Six Cisco 2960 switches will connect down to the Core switches using redundant trunk links. STP (Spanning Tree Protocol) will prevent routing loops on these redundant links.
4. **Servers Level:** The FTP, DNS, and DHCP servers will plug into an access switch configured for VLAN 70.
5. **Security Policy (ACL Target):** An Extended Access Control List will be placed on the SVI or sub-interface for VLAN 60, permitting TCP port 20/21 (FTP) to the `192.168.10.224/28` subnet, but `deny ip` to all other `192.168.10.0/24` subnets.
