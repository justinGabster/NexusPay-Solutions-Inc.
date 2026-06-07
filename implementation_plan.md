# Capstone Network Administration Final Project Plan

This document outlines the step-by-step implementation plan and roadmap for your final network project. It combines the requirements from both your course rubric and the specific technical scenario.

## User Review Required
> [!IMPORTANT]
> Please review this roadmap carefully. Since this is your capstone project, confirm if you have a preferred network simulation tool (e.g., **Cisco Packet Tracer**, **GNS3**, or **EVE-NG**) so we can tailor the configuration steps.

## Deliverables Checklist
- `[ ]` **Phase 1: Company Profile & Statement of Work**
  - Project Scope and Purpose Document
  - Fictional Company Profile (Name, History, Mission, Vision)
  - Requirement Analysis (Business goals, scalability, security)
- `[ ]` **Phase 2: Network Design & Architecture**
  - Network Topology Diagram (Logical and Physical)
  - IP Addressing Scheme (VLSM) Table
  - Hardware Requirements List (Routers, Switches, Servers, Cables)
- `[ ]` **Phase 3: Network Configuration (Proof of Concept)**
  - Simulated Network File (e.g., `.pkt` for Packet Tracer)
  - VLAN and Inter-VLAN Routing Configuration
  - DHCP Server Configuration
  - High Availability Configurations (STP, FHRP, Backup Routes)
  - Security Configurations (ACLs for Guest Network, SSH, Port Security)
- `[ ]` **Phase 4: Testing & Documentation**
  - Testing and Verification Procedures (Ping/Traceroute logs)
  - Complete Technical Documentation (Configs, Tables, Diagrams)
- `[ ]` **Phase 5: Presentation & Defense Preparation**
  - Presentation Slides
  - Individual Defense Preparation (Q&A study guide)

---

## Proposed Roadmap

### Phase 1: Planning and Documentation (Competency 1 & 3)
1. **Create the Fictional Company Profile**:
   - Invent a company name, its history, mission, and vision.
   - Define the organization structure (e.g., HR, Payroll, IT, Executives) to map to your VLANs.
2. **Draft the Statement of Work (SOW)**:
   - Outline the project scope: A small business network supporting 150 LAN users across different departments and at least 10 guest users.
   - Determine client goals regarding performance, scalability, and security.
3. **List Physical Hardware**:
   - Specify the required Cisco Routers, Cisco Switches, Internet Router, PCs, Servers (DHCP, FTP), and optional Cisco Firewalls.

### Phase 2: IP Addressing and Network Design (Competency 2)
1. **Design the IP Addressing Scheme (VLSM)**:
   - Select an appropriate IP Class (e.g., `10.0.0.0/8` or `192.168.0.0/16`).
   - Subnet the network to accommodate 150+ LAN users across various department VLANs.
   - Create a dedicated subnet for the Guest Network (supporting at least 10 users).
   - Document this in an **IP Network Design Table**.
2. **Create the Network Topology Diagram**:
   - Map out where switches and routers connect.
   - Label devices, interfaces, and IP networks.

### Phase 3: Network Implementation & Configuration (Competency 4)
*This will be done in your chosen simulation tool (e.g., Packet Tracer).*
1. **Basic Device Configuration**:
   - Assign hostnames, configure passwords, and enable SSH for secure management.
2. **VLANs and Switching**:
   - Create VLANs for each department (HR, Payroll, IT) and the Guest Network.
   - Assign access ports to PCs and configure trunk ports between switches.
   - (Optional but recommended) Configure Port Security on access switches.
3. **Routing and DHCP**:
   - Configure Inter-VLAN routing (Router-on-a-Stick or Layer 3 Switch).
   - Set up a central DHCP server (or configure the router as a DHCP server) to dynamically assign IPs to all end-devices.
   - Configure your preferred Routing Protocol (e.g., OSPF or EIGRP) across the network.
4. **High Availability Implementation**:
   - Ensure Spanning Tree Protocol (STP) is optimized.
   - Configure First Hop Redundancy Protocol (FHRP) like HSRP or VRRP for gateway redundancy.
   - Set up backup static routes where applicable.
5. **Security and Access Control Lists (ACLs)**:
   - **Crucial Requirement**: Configure an ACL so the Guest Network can ONLY access the FTP service on the FTP server.
   - Explicitly block the Guest Network from accessing the rest of the LAN.

### Phase 4: Testing & Technical Documentation
1. **Test the Network**:
   - Verify PCs get IP addresses via DHCP.
   - Use `ping` and `traceroute` to ensure inter-VLAN routing works.
   - **Test the ACL**: Verify a Guest PC can reach the FTP server but fails to ping any HR/Payroll PC.
2. **Compile Documentation**:
   - Gather all configuration snippets, the IP table, diagrams, and testing proofs into the final Technical Documentation report.

### Phase 5: Final Presentation & Defense Preparation (Competency 5)
1. **Create the Presentation**:
   - Build engaging slides starting with the company profile, moving to the network design, showcasing the configurations, and concluding with a live demonstration.
2. **Prepare for the Panel Q&A**:
   - Ensure you (and every team member) understand the *"why"* behind every design decision.
   - Review routing, VLANs, ACLs, and troubleshooting scenarios.
   - *Note: As per the rubric, incorrect or unanswered questions result in a 15-point deduction from the group grade.*

## Next Steps
Once you approve this roadmap, we can begin **Phase 1**. Do you have a fictional company name and department structure in mind, or would you like me to generate some ideas for you?
