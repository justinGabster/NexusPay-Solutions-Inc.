# Phase 1: Company Profile & Statement of Work

## 1. Company Profile

**Company Name:** NexusPay Solutions, Inc.
**Industry:** Financial Technology (FinTech) & Digital Payment Processing

### History
Founded in 2024, NexusPay is a rapidly growing startup that provides local businesses with secure, real-time digital wallet APIs and point-of-sale (POS) terminal integrations.

### Mission
"To democratize digital commerce by providing seamless, secure, and resilient payment infrastructure for emerging markets."

### Vision
"To become the leading, most trusted financial transaction gateway in Southeast Asia by 2030."

### Department & VLAN Breakdown (150+ LAN users)
| Department / Network | Estimated Host Count | Justification & Access Rights |
| --- | --- | --- |
| **VLAN 10: Executive & Management** | ~15 hosts | High-priority access; requires access to all internal servers and resources. |
| **VLAN 20: IT Operations & NetSec** | ~20 hosts | The administrators. This VLAN needs SSH access to network infrastructure and complete visibility. |
| **VLAN 30: Core Engineering & Dev** | ~50 hosts | The largest group. Software engineers building the payment APIs. Needs access to local development servers. |
| **VLAN 40: Finance & Payroll** | ~15 hosts | Highly sensitive. Handles corporate accounts. **Must be heavily isolated** from regular corporate traffic. |
| **VLAN 50: Human Resources (HR)** | ~20 hosts | Handles employee data and onboarding. |
| **VLAN 60: Guest Network** | ~20 hosts | **The ACL Target.** Visitors, auditors, and clients. Completely blocked from VLANs 10–50; restricted only to the FTP Server and Internet. |
| **VLAN 70: Server Farm (Data Center)** | ~10 hosts | Contains DHCP Server, FTP Server, and internal databases. |
| **VLAN 99: Native / Management** | N/A | Strictly for switch/router management traffic. |

---

## 2. Statement of Work (SOW)

### Project Purpose and Scope
The purpose of this project is to design, configure, and implement a robust, secure, and highly available local area network (LAN) for NexusPay Solutions. The network must support over 150 internal employees across segmented departments while adhering to strict financial industry compliance.

### Client's Business Context and Needs
As a FinTech company handling transactional data, NexusPay must comply with strict financial regulations (e.g., PCI-DSS). The company frequently hosts clients and third-party auditors who need internet and FTP access, but they must be completely isolated from the internal network hosting financial applications.

### Client's Business Goals
- **High Availability (STP/FHRP):** A network outage means transactions fail, causing immediate financial and reputational loss. Gateway and switch redundancy are critical.
- **Security & Segregation:** Strict logical isolation (VLANs and ACLs) must be enforced. The Guest Network must strictly sandbox visitors, keeping core database segments completely invisible to them.

---

## 3. Physical Hardware Requirements
**Routers & Firewalls:**
- 2x **Cisco 4321 Routers** (Configured for FHRP/HSRP to provide redundant default gateways)
- 1x **Internet Edge Router** (To simulate ISP connection)

**Switches:**
- 2x **Cisco 3650 / 3560 Layer 3 Multilayer Switches** (Core/Distribution layer, handling Inter-VLAN routing and FHRP/STP)
- 6x **Cisco 2960 Layer 2 Switches** (Access layer, connecting end devices per department)

**Servers & End Devices:**
- 1x **Central DHCP Server** (Assigning IPs to all VLANs)
- 1x **FTP Server** (Accessible by Guests and Internal staff)
- 1x **Web/DNS Server** (For internal naming resolution)
- ~150x **PCs/Laptops** (Distributed across department VLANs)
- ~20x **Guest Laptops/Mobile Devices**
