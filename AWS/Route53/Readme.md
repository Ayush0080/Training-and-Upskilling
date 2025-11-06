| **Term**                | **Full Form / Meaning** | **Explanation**                                                                                                                                         | **Example / Notes**                                               |
| ----------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **DNS**                 | *Domain Name System*    | Translates human-readable names (like `www.example.com`) into IP addresses (`192.0.2.1`). Route 53 is Amazon’s DNS service.                             | When a user types your domain, DNS finds the IP of your server.   |
| **Domain Name**         | —                       | A unique, human-readable name registered for your website/application.                                                                                  | `example.com`, `myapp.io`                                         |
| **Registrar**           | —                       | A company/service where you register your domain name. Route 53 can act as a registrar too.                                                             | GoDaddy, Route 53 Domains, Namecheap                              |
| **Hosted Zone**         | —                       | A container for DNS records of a domain. It tells Route 53 how to route traffic for that domain.                                                        | If you have `example.com`, Route 53 creates a hosted zone for it. |
| **Public Hosted Zone**  | —                       | Routes traffic on the **public internet**.                                                                                                              | `example.com` (accessible globally)                               |
| **Private Hosted Zone** | —                       | Routes traffic **within your VPC only** (for internal apps).                                                                                            | `internal.corp.local` accessible only inside AWS VPC              |
| **Record (Record Set)** | —                       | A DNS entry inside a hosted zone that maps a domain/subdomain to a value (like an IP or another domain).                                                | `www.example.com → 192.0.2.1`                                     |
| **Record Type**         | —                       | Defines the kind of DNS mapping.                                                                                                                        | See below for all record types.                                   |
| **A Record**            | *Address Record*        | Maps a domain/subdomain to an IPv4 address.                                                                                                             | `api.example.com → 203.0.113.10`                                  |
| **AAAA Record**         | *IPv6 Address Record*   | Maps a domain/subdomain to an IPv6 address.                                                                                                             | `example.com → 2001:db8::1234`                                    |
| **CNAME Record**        | *Canonical Name Record* | Maps one domain name to another (alias).                                                                                                                | `www.example.com → example.com`                                   |
| **MX Record**           | *Mail Exchange Record*  | Directs email traffic to your mail server.                                                                                                              | `10 mail.example.com`                                             |
| **TXT Record**          | *Text Record*           | Stores arbitrary text data (often for verification, SPF, DKIM, etc.).                                                                                   | `"v=spf1 include:_spf.google.com ~all"`                           |
| **NS Record**           | *Name Server Record*    | Points to the authoritative name servers for your domain.                                                                                               | `ns-123.awsdns-45.org`                                            |
| **SOA Record**          | *Start of Authority*    | Contains information about the domain like admin email, serial number, refresh time, etc.                                                               | Auto-created by Route 53 for every hosted zone.                   |
| **Alias Record**        | —                       | AWS-specific record type that acts like a CNAME but works at the **root domain** (`example.com`) and supports AWS resources (like ELB, CloudFront, S3). | `example.com → ALB DNS name`                                      |
| **TTL**                 | *Time To Live*          | The time (in seconds) that a DNS resolver caches a record before checking again.                                                                        | `TTL = 300` means record cached for 5 minutes.                    |
| **Health Check**        | —                       | Monitors the health of your endpoints (HTTP, TCP, or CloudWatch alarms). Used for failover or multivalue routing.                                       | Marks record unhealthy if app returns 5xx.                        |
| **Routing Policy**      | —                       | Determines how Route 53 responds to DNS queries (simple, weighted, latency-based, etc.).                                                                | `example.com` → uses latency-based routing between regions.       |
| **Traffic Flow**        | —                       | A visual editor for creating complex routing policies (combining latency, geolocation, failover, etc.).                                                 | Used in large-scale multi-region deployments.                     |
| **Alias Target**        | —                       | The AWS resource you point an alias record to.                                                                                                          | e.g., `ALIAS example.com → myloadbalancer.amazonaws.com`          |
| **Delegation Set**      | —                       | A group of name servers Route 53 assigns to your hosted zone.                                                                                           | Used when you have multiple hosted zones with same NS.            |
| **Resolver**            | —                       | The DNS service (often your ISP or AWS) that queries Route 53 to find the IP address.                                                                   | `8.8.8.8` (Google), or AWS resolver in VPC.                       |
| **Forwarding Rules**    | —                       | In Private DNS, used to forward queries to external DNS servers.                                                                                        | Forward `*.corp.local` to on-prem DNS.                            |



### Common Record Types
 | **Type**        | **Purpose**                       | **Example**                             |
| --------------- | --------------------------------- | --------------------------------------- |
| **A**           | IPv4 address                      | `app.example.com → 192.0.2.1`           |
| **AAAA**        | IPv6 address                      | `api.example.com → 2001:db8::1`         |
| **CNAME**       | Alias to another domain           | `www.example.com → example.com`         |
| **MX**          | Email routing                     | `mail.example.com`                      |
| **TXT**         | Text info (SPF/DKIM/verification) | `"v=spf1 include:_spf.google.com ~all"` |
| **NS**          | Name servers                      | `ns-xx.awsdns-yy.com`                   |
| **SOA**         | Authority info                    | Auto-created for every hosted zone      |
| **Alias (AWS)** | AWS resource alias (no IP needed) | `example.com → ELB or CloudFront`       |


| **Record Name**          | **Type**  | **Value / Target**  | **Purpose**    |
| ------------------------ | --------- | ------------------- | -------------- |
| `example.com`            | A (Alias) | ALB DNS name        | Website        |
| `api.example.com`        | A         | EC2 public IP       | API endpoint   |
| `mail.example.com`       | MX        | Mail server         | Email handling |
| `_amazonses.example.com` | TXT       | Verification string | SES validation |


