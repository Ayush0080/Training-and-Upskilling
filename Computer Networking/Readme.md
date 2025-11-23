####  Local Area Network (LAN)

- LANs are networks designed to connect multiple devices in a single physical location, enabling
seamless communication between computers and other devices such as printers.
-  LANs can be established using both wired and wireless technologies


#### Network Interface Cards (NICs)
- Network Interface Cards are hardware components, typically built into modern computers, responsible
for connecting devices to a LAN.
- NICs have physical ports to which Ethernet cables are connected, allowing devices to access the LAN

#### MAC Addresses

- Every NIC has a unique Media Access Control (MAC) address, a hardware-based identifier hard-coded
by manufacturers.
- A MAC address is permanently associated with a specific NIC and is used for addressing and routing
data in a LAN


#### HUB
- A Hub is a very basic networking device.
- It broadcasts data to every device connected to it — like shouting a message in a room.
- It does NOT check who the data is for.
- Operates at Layer 1 (Physical Layer) of the OSI model.
- Example:

    - If a computer sends data to Printer, the Hub sends that same data to all other devices (PC1, PC2, Laptop, etc.).


#### BRIDGE


- A Bridge connects two LAN segments and reduces traffic.

- A bridge checks the MAC address and decides whether to forward or block traffic.
- Helps separate one big LAN into smaller collision domains.
- Operates at Layer 2 (Data Link Layer).
- A Bridge can connect these two LANs and filter traffic between them.


#### SWITCH
- A Switch is a smart device used in almost every LAN today.
- Switch reads MAC addresses and sends data only to the intended device.
- Creates a separate connection for each device → no collisions.
- Operates at Layer 2, some advanced switches also operate at Layer 3.

- Example:
    - If PC1 sends data to PC3:

    - Switch forwards the packet only to PC3.

    - Other PCs do not receive that data.



#### Layer 7 – Application
- You open Chrome and go to YouTube. Browser uses HTTP/HTTPS to communicate. This is the “language” between browser ↔ website.

#### Layer 6 – Presentation
- Browser handles:

    - encryption (HTTPS)
    compression
    formatting
#### Layer 5 – Session
- Controls:
    - login session
    connection management
    cookies/token communication
    
#### Layer 4 – Transport (TCP/UDP)
- Here we add port numbers.

- Example:

    - HTTP uses TCP port 80
    - HTTPS uses TCP port 443
    - TCP ensures:

    - No errors
    Reliable delivery
    In-order packets
    Think of TCP like a courier service with tracking.

#### Layer 3 – Network (IP Layer)
- Adds IP addresses:

    - Source IP = your computer
    Destination IP = YouTube servers
    If your PC doesn’t know the route:

    - It uses Default Gateway (your router).
    Router decides where packets go next.

#### Layer 2 – Data Link (MAC Layer)
 - Adds MAC addresses:

    - Source MAC = your NIC
    Destination MAC = router’s MAC
    Switch uses its MAC Table to forward traffic to the right port.

    - Layer 2 only works inside your local network.

#### Layer 1 – Physical Layer
- Actual transmission:

    - Ethernet cable
    - Fiber/Wi-Fi
    - Electrical/optical signals
    - This is raw bits (1s and 0s) crossing the wire.

#### Default Gateway
- Default Gateway is the router that forwards your device’s traffic to other networks when the destination is outside your local network.
    ```bash
   -  Your devices:

    Laptop → 192.168.1.10

    Mobile → 192.168.1.20

    TV → 192.168.1.30

    - Your Wi-Fi router:

    192.168.1.1 ← This is the default gateway

    - When your laptop wants to open google.com:

     “I don’t know where Google is. I will send this to my default gateway.”

    Router → Sends it to the internet  
    ```


#### Broadcast Traffic
- Destination = Everyone
- Sent to ALL devices in the LAN
- Examples:

    - ARP request → “Who has IP 192.168.1.10?”

    - DHCP Discover → “Who can give me an IP?”

    - Every device receives it.

    - Broadcast MAC address = FF:FF:FF:FF:FF:FF

#### Unknown Unicast Traffic
- Destination = ONE device
- But switch does NOT know which port that device is on
- So it sends (floods) to all ports
- Example:

    - PC1 sends data to MAC AA:BB:CC:DD:EE:FF
    - Switch DOES NOT know the MAC → Unknown

    - So the switch floods it to everyone until:

    - It learns the correct port from the reply

#### Multicast Traffic
- Destination = a Group of devices

- But switches don’t know exactly which ports belong to the group.
- So many switches treat it as broadcast (unless IGMP snooping is enabled).

- Example:

    - Video streaming  



#### ARP Request = A broadcast message asking:
- Who has this IP? Tell me your MAC address.”**

- A device uses ARP Request when it knows the IP of the destination but does not know its MAC address.

- arp -a → show ARP table (IP ↔ MAC). Check for correct MAC for a target IP.
- ipconfig /all → see NIC MAC, IP, default gateway.



#### Router

- A Router is a networking device that connects different networks and forwards data between them using IP addresses.

- It works at OSI Layer 3 (Network Layer).
- It uses routing to decide where to send packets.




#### ICMP
-  Internet Control Message Protocol
- ICMP is a network layer protocol used for sending error messages and testing connectivity. Tools like ping and traceroute use ICMP to check if a device is reachable




#### VLAN (Virtual Local Area Network)
-  A VLAN (Virtual Local Area Network) is a way to logically divide a single physical network into multiple separate, isolated networks.
    ```bash
    -you have 1 switch with 8 ports:

    [1][2][3][4][5][6][7][8]


    You decide:

    Ports 1,2,3,4 → VLAN 10 (HR Team)

    Ports 5,6,7,8 → VLAN 20 (Finance Team)

    The switch will behave like:

    VLAN 10 = a separate mini network  
    VLAN 20 = another separate mini network


    Even though all devices plug into one switch, the switch keeps their traffic separate.

    HR cannot talk to Finance unless you use a router.

    ```
#### border router

- A border router is a router placed at the edge (border) of a network that connects your internal network to an external network, usually:

    - The Internet, or

    - Another company/branch network, or

    - An ISP (Internet Service Provider)   


#### DHCP
- DHCP = Dynamic Host Configuration Protocol
- It is a service that automatically gives IP addresses to devices in a network.  


- DHCP Process (Very Easy)
 -  Called DORA:

    | Step                | Meaning          | Simple Explanation                      |
    | ------------------- | ---------------- | --------------------------------------- |
    | **D – Discover**    | Find DHCP server | Device shouts: “Any DHCP server here?”  |
    | **O – Offer**       | Server offers IP | DHCP replies: “I can give you this IP!” |
    | **R – Request**     | Device accepts   | Device says: “Okay, I want that IP.”    |
    | **A – Acknowledge** | Confirmation     | Server says: “IP assigned, go ahead!”   |


####  SNMP

- SNMP = Simple Network Management Protocol

- It is a protocol used to monitor and manage network devices like:

   - Routers

   - Switches

    - Firewalls

    - Servers

    - Printers

    - Access Points

    - SNMP helps you check the health of devices and control them remotely.    


#### How SNMP Works (Very Easy)

- SNMP Agent

    - Runs inside devices

    - Collects data (CPU, RAM, status, traffic)
- SNMP Manager

    - Usually a monitoring tool

    - Example: Nagios, Zabbix, SolarWinds

    - It asks the device for data

    - Shows it on a dashboard


#### VPN = Virtual Private Network
- A VPN creates a secure, encrypted tunnel over the Internet so your data can travel safely from one place to another.