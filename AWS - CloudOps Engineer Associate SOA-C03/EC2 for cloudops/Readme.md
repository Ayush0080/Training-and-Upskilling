### EC2 Instance Connect (EIC) Endpoint

- Allows you to connect securely to 
your private EC2 instances
- No Internet Gateway, no NAT 
Gateway, No Internet required
- EIC Endpoint Security Group: must 
allow outbound SSH traffic to target 
instances
- EC2 Instance Security Group: must 
allow inbound SSH traffic from EIC 
Endpoint Security Group

  ![alt text](image.png)   



### CloudWatch Metrics for EC2
- AWS Provided metrics (AWS pushes them):
    - Basic Monitoring (default): metrics are collected at a 5 minute internal
    - Detailed Monitoring (paid): metrics are collected at a 1 minute interval
    - Includes CPU, Network, Disk and Status Check Metrics


- EC2 included metrics 
- CPU: CPU Utilization + Credit Usage / Balance 
- Network: Network In / Out 
- Status Check: 
    - Instance status = check the EC2 VM 
    - System status = check the underlying hardware 
    - Attached EBS status = check attached EBS volumes 
- Disk: Read / Write for Ops / Bytes (only for instance store) • - RAM is NOT included in the AWS EC2 me  


### Unified CloudWatch Agent
- For virtual servers (EC2 instances, on-premises servers, …)
- Collect additional system-level metrics such as RAM, 
processes, used disk space, etc. 
- Collect logs to send to CloudWatch Logs
- No logs from inside your EC2 instance will be sent to 
CloudWatch Logs without using an agent
- Centralized configuration using SSM Parameter Store
- Make sure IAM permissions are correct
- Default namespace for metrics collected by the Unified 
CloudWatch agent is CWA



