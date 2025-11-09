# Networking 


### VPC

- A VPC (Virtual Private Cloud) is your own isolated network inside AWS, similar to a private data center in the cloud.
  - You can define your IP address range, subnets, routing, and security to control how resources (like EC2, RDS, etc.) communicate with each other and with the internet.


#### CIDR Block

- CIDR stands for Classless Inter-Domain Routing.
It defines the IP address range (network size) used in your VPC or Subnet  


#### Subnet

- A Subnet is a smaller slice of your VPC CIDR block — a subdivision of the network.
- You place AWS resources (EC2, RDS, etc.) inside subnets.


   - Each subnet:

       -  Belongs to only one Availability Zone (AZ)

       -  Has its own route table (directly or by association)

       -  Can be Public (connected to Internet Gateway) or Private (no internet access directly)


##### Public Subnet
- A Public Subnet is a subnet that has a direct route to the Internet through an Internet Gateway (IGW).

- That means any resource (e.g., EC2 instance) inside this subnet can send and receive traffic from the internet, if:

   -  It has a public IP or Elastic IP

    - The route table for the subnet includes a route to the IGW

- Public Subnet Characteristics
    | Feature                     | Description                                     |
    | --------------------------- | ----------------------------------------------- |
    | **Internet access**         | Yes (directly via IGW)                          |
    | **Route Table**             | Has route to Internet Gateway (0.0.0.0/0 → IGW) |
    | **Use case**                | Host web servers, bastion hosts, load balancers |
    | **Public IP required**      | Yes (for inbound internet access)               |
    | **Security groups / NACLs** | Must allow inbound/outbound internet traffic    |
    ```bash

    [Internet]
        │
        ▼
    +---------------+
    | Internet GW   |
    +---------------+
        │
        ▼
    +-----------------------+
    | Public Subnet (10.0.1.0/24) |
    |  • EC2: Web Server     |
    |  • Public IP: Yes      |
    +-----------------------+

    ```
##### Private Subnet

- A Private Subnet is a subnet that does NOT have a route to the Internet Gateway.

- Resources in a private subnet:

   -  Cannot be accessed directly from the Internet.

   -  Can still access the Internet indirectly (for software updates, etc.) through a NAT Gateway in a public subnet

-  Private Subnet Characteristics 

    | Feature             | Description                                     |
    | ------------------- | ----------------------------------------------- |
    | **Internet access** | No direct access                                |
    | **Route Table**     | No route to IGW (but may route to NAT GW)       |
    | **Use case**        | Host databases, backend apps, internal services |
    | **Public IP**       | Not assigned                                    |
    | **Security**        | Safer — isolated from public traffic            |


    ```bash

                        +----------------+
                        | Internet GW    |
                        +----------------+
                                │
                        +----------------+
                        | NAT Gateway    |
                        | (in Public Subnet) |
                        +----------------+
                                │
            ┌─────────────────────────────┐
            │                             │
    +-----------------------+   +-----------------------+
    | Public Subnet         |   | Private Subnet        |
    |  - NAT Gateway        |   |  - Database Server    |
    |  - Web Server (EC2)   |   |  - App Server         |
    +-----------------------+   +-----------------------+

    ```

    