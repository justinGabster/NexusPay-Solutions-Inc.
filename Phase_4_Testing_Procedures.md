# Phase 4: Verification & Testing Procedures (Updated by VJ)

Based on the verification check conducted by your co-member VJ, the following testing procedures and troubleshooting fixes must be validated in your `NetAD_Nexus_Topology.pkt` file.

---

## 🛑 Test 1: DHCP & Native VLAN Troubleshooting
**Goal:** Prove DHCP works and resolve Native VLAN mismatches.
*   **Initial Issue:** PC0 was stuck on "Requesting IP Address". 
*   **Root Cause:** CDP Native VLAN mismatch (VLAN 1 vs VLAN 99) on trunk ports between Core switches and Access switches.
*   **The Fix:**
    1. On **Core-SW-A** and **Core-SW-B**, set `switchport trunk native vlan 99` on the trunk interfaces (Gig1/0/2-7 and Gig1/0/24).
    2. On **ACC-SW-1 through ACC-SW-6**, set `switchport trunk native vlan 99` on uplink ports (Gig0/1-2).
*   **Verification:** Go to **PC0 -> Desktop -> IP Configuration**. Select DHCP. It should now successfully pull an IP like `192.168.10.11` (Success!).

---

## 🛑 Test 2: Inter-VLAN Routing
**Goal:** Prove internal devices can route to different VLAN gateways.
*   **Steps:** From **PC0**, open Command Prompt.
*   Run `ping 192.168.10.1` (VLAN 30 Gateway).
*   Run `ping 192.168.10.65` (VLAN 20 Gateway).
*   **Result:** Should succeed with replies (Success!).

---

## 🛑 Test 3: Guest ACL Blocking
**Goal:** Prove the Guest network (VLAN 60) is isolated from internal networks.
*   **Steps:** Open **PC3** (which is assigned to VLAN 60 Guest).
*   Run `ping 192.168.10.1` (Internal Gateway).
*   **Result:** Should FAIL with "Destination host unreachable" (Success!).

---

## 🛑 Test 4: High Availability (HSRP)
**Goal:** Prove Core-SW-A is Active and Core-SW-B is Standby.
*   **Steps:** 
    1. On **Core-SW-A** CLI, run `show standby brief`. It should list states as **Active**.
    2. On **Core-SW-B** CLI, run `show standby brief`. It should list states as **Standby**.
*   **Result:** Verified (Success!).

---

## 🛑 Test 5: FTP Server Access
**Goal:** Prove internal PCs can access the FTP server in the Server Farm (VLAN 70).
*   **Steps:** From any internal PC, run `ftp 192.168.10.231`.
*   **Login:** `guest` / `password`.
*   **Result:** Should successfully say "Logged in" (Success!).

---

## 🔥 Advanced Panel-Pleaser Tests (Optional)
If you want to absolutely impress your grading panel during the defense, perform these live demonstrations:

### 1. Spanning Tree Protocol (STP) Failover
**Goal:** Prove Layer 2 redundancy works.
*   **Steps:** On `ACC-SW-1`, identify the active trunk link going to `Core-SW-A`. Go into the CLI and manually shut it down (`interface Gig0/1`, then `shutdown`). 
*   **Result:** Watch the orange light on the link to `Core-SW-B` turn green as STP recalculates and unblocks the redundant path, keeping the PCs online.

### 2. Simulation Mode: VLAN Broadcast Isolation
**Goal:** Visually prove to the panel that your VLANs are properly containing broadcast traffic, effectively stopping broadcast storms.
*   **Steps:** In Packet Tracer, switch from "Realtime" to "Simulation" mode (bottom right corner). From PC0 (VLAN 30), ping the broadcast address of VLAN 30 (`ping 192.168.10.63`). Click the "Play" button in the Simulation Panel.
*   **Result:** The panel will visually see the packet travel to the Access Switch and only be forwarded to other ports in VLAN 30 and the trunk link. It will hit the Core switch and STOP. This proves that your VLAN segmentation is successfully blocking the broadcast from flooding the rest of the company network!

### 3. Rogue Device Port Security Trigger
**Goal:** Prove that an unauthorized device cannot connect to your access switches.
*   **Steps:** Disconnect a PC from `ACC-SW-2` and connect a rogue switch or laptop with a different MAC address into that exact same switch port. Try to ping the gateway.
*   **Result:** The port will immediately turn red and enter an `err-disable` state because it violated the `switchport port-security maximum 1` rule, physically blocking the attacker.

---
*(Note: Limitation recognized by VJ - Core-SW-B cannot reach the internet directly due to the NIM-ES2-4 module operating at Layer 2).*
