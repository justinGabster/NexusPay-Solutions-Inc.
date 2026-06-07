# Phase 3: Network Configuration Implementation Guide

This guide will walk you through applying the exact configurations to your Cisco Packet Tracer simulation for **NexusPay Solutions**.

## 1. Drag & Drop Your Topology
Before applying the scripts, ensure your Packet Tracer workspace has the following devices wired up:
- **1x Edge Router** (e.g., Cisco 4321) connected to an ISP Router/Cloud.
- **2x Core Switches** (e.g., Cisco 3650 or 3560 Multilayer Switches). Ensure they are connected to each other, and each connects to the Edge Router.
- **6x Access Switches** (e.g., Cisco 2960). Connect them to both Core Switch A and Core Switch B using redundant cables (Spanning Tree will handle the loops).
- **Servers**: Add 3 Server End-Devices to represent DHCP, FTP, and DNS. Connect them to an Access Switch assigned to VLAN 70.
- **PCs/Laptops**: Distribute them across your access switches to represent the different departments (HR, IT, Guest, etc.).

## 2. Configure the Servers (GUI Method)
In Packet Tracer, it is best to configure your servers via the GUI interface:

### A. The Central DHCP Server (VLAN 70)
1. Give the Server a static IP: `192.168.10.230`, Subnet Mask `255.255.255.240`, Default Gateway `192.168.10.225`.
2. Go to **Services > DHCP**.
3. Create a pool for **each** VLAN (Except VLAN 70 and 99). 
   - *Example for VLAN 30:* Pool Name: `Dev_Pool`, Default Gateway: `192.168.10.1`, DNS Server: `192.168.10.232`, Start IP: `192.168.10.10`, Subnet Mask: `255.255.255.192`.
4. Turn the DHCP Service **ON**.

### B. The FTP Server (VLAN 70)
1. Give the Server a static IP: `192.168.10.231`, Subnet Mask `255.255.255.240`, Default Gateway `192.168.10.225`.
2. Go to **Services > FTP**.
3. Create a user (e.g., Username: `guest`, Password: `password`) with Read-only permissions, and an Admin user with full permissions.

### C. The Web/DNS Server (VLAN 70)
1. Give the Server a static IP: `192.168.10.232`, Subnet Mask `255.255.255.240`, Default Gateway `192.168.10.225`.
2. Go to **Services > DNS**. Add an A Record: Name: `ftp.nexuspay.local`, Address: `192.168.10.231`.

---

## 3. Apply the CLI Configuration Scripts
I have generated text files containing the exact CLI commands needed for your switches and routers. 
To apply them:
1. Click on the device in Packet Tracer.
2. Go to the **CLI** tab.
3. Type `enable` to enter privileged EXEC mode (if not already there).
4. Open the respective text file, copy the entire contents, and **paste** it into the CLI.

**The files are located in your project folder:**
* `Phase_3_Core_Switch_A_Config.txt` - Handles Inter-VLAN routing, HSRP (Active), and ACLs.
* `Phase_3_Core_Switch_B_Config.txt` - Handles HSRP (Standby) for High Availability.
* `Phase_3_Access_Switch_Config.txt` - Template for configuring access ports and port-security.
* `Phase_3_Edge_Router_Config.txt` - Handles NAT out to the internet and static routing.

## 4. Verification Check
Once everything is pasted and the links turn green (STP convergence takes ~30 seconds):
1. Connect a PC to an Access Switch port (e.g., VLAN 30).
2. Set the PC to **DHCP**. It should successfully pull an IP like `192.168.10.10`.
3. Try to ping the gateway: `ping 192.168.10.1`.
4. From a Guest PC (VLAN 60), try to ping a Dev PC (VLAN 30). It should **FAIL** (Destination Unreachable) because of the ACL, proving your security works!
