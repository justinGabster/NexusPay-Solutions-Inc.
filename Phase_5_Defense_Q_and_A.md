# Phase 5: Panel Defense Q&A Study Guide

According to the Networking Capstone Rubric, each team member may be randomly selected to answer questions. An incorrect or unanswered question results in a **15-point deduction** from the group grade. 

To ensure everyone is prepared, here is a study guide covering the key topics your panel is likely to ask about the **NexusPay Solutions** network.

---

## 1. Network Design & Topology Decisions
**Q: Why did you separate the network into so many different VLANs?**
**A:** We separated the network into functional VLANs (HR, Finance, Dev, etc.) to limit broadcast domains, which improves network performance, and to logically group users for security purposes. As a FinTech company, it is critical that our Finance department is isolated from general staff to comply with financial data security standards (like PCI-DSS).

**Q: Why use a /27 subnet for most of the VLANs instead of a standard /24?**
**A:** We used Variable Length Subnet Masking (VLSM) to conserve IP addresses. Since departments like HR and Finance only have around 15-20 hosts, allocating a full /24 (254 usable IPs) to them would be a massive waste of address space. A /27 provides 30 usable hosts, which perfectly fits their current size with some room for growth, allowing us to fit the entire company into a single `192.168.10.0/24` block.

---

## 2. Technical Concepts & Configuration Details
**Q: How does the Guest Network (VLAN 60) ACL work?**
**A:** We applied an Extended Access Control List (ACL) inbound on the Guest VLAN interface. The ACL explicitly permits UDP for DHCP/DNS, and permits TCP ports 20 and 21 specifically to the IP address of the FTP server (`192.168.10.231`). Immediately after that, we have a `deny ip` statement blocking the guest network from reaching the rest of the `192.168.10.0/24` internal network. Finally, a `permit ip any` allows guests to reach the internet. 

**Q: Explain how High Availability was implemented in your network.**
**A:** We used **HSRP (Hot Standby Router Protocol)** on our two Core Multilayer Switches. We configured both switches with virtual IPs (VIPs) for every VLAN. Core-Sw-A is configured with a priority of 110, making it the Active gateway, while Core-Sw-B has a default priority of 90, making it the Standby. If Core-Sw-A fails, Core-Sw-B automatically takes over the VIP, and end-users experience almost zero downtime. We also rely on **STP (Spanning Tree Protocol)** to prevent Layer 2 loops on our redundant access switch uplinks.

**Q: How are PCs getting their IP addresses if the DHCP server is on a completely different VLAN (VLAN 70)?**
**A:** Routers (and Layer 3 switches) drop broadcast traffic by default. Since DHCP requests are broadcasts, they wouldn't reach VLAN 70. To fix this, we configured the `ip helper-address 192.168.10.230` command on every SVI. This tells the Core switch to take the DHCP broadcast, convert it to a unicast packet, and forward it directly to the DHCP server's IP address.

---

## 3. Troubleshooting Scenarios
**Q: A user in the HR department (VLAN 50) complains they cannot reach the internet, but they can ping the Dev department (VLAN 30). What is likely the issue?**
**A:** Since they can ping another internal VLAN, we know their physical connection, IP address, and Inter-VLAN routing on the Core Switch are working. The issue is likely at the edge of the network. It could be a missing static route on the Edge Router pointing back to the internal network, or an issue with the NAT (Network Address Translation) overload configuration not translating the internal `192.168.10.0/24` addresses to the public IP.

**Q: You notice that network traffic is extremely slow and the switch CPU utilization is at 99%. What happened?**
**A:** This is a classic symptom of a Layer 2 switching loop, also known as a broadcast storm. This happens if Spanning Tree Protocol (STP) fails or is disabled, and redundant physical cables continuously loop broadcast frames infinitely. 

---
*Tip for the Team: Make sure every member can point to the Packet Tracer topology and trace the path a packet takes from a PC, up to the Access Switch, to the Core Switch, out the Edge Router, and to the Internet.*
