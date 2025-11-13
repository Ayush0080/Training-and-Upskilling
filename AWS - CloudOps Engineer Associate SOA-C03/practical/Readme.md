## CloudWatch - unified CloudWatch 

#### collect metrics and logs from ec2 with the cloudwatch agent

- create role to able to send logs and metrics to cloudwatch
  ![alt text](image.png)
  ![alt text](image-1.png)
  ![alt text](image-9.png)

- created EC2 instance
  ![alt text](image-2.png)  
  ![alt text](image-3.png)
  ![alt text](image-4.png)

- now installing httpd on this ec2
   ![alt text](image-5.png)

- installing CW-agent on this EC2  
  ![alt text](image-6.png)
  ![alt text](image-7.png) 
  ![alt text](image-10.png)

  ![alt text](image-11.png)


- ssm:AmazonCloudWatch-linux
   -  means: “Fetch the CloudWatch Agent configuration stored in Systems Manager Parameter Store under the name AmazonCloudWatch-linux.”

   ![alt text](image-12.png)
   ![alt text](image-13.png)
   ![alt text](image-14.png)



###### failed during second phase validation, showing this:
```bash
Error running agent: Error loading config file /opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.toml:
error parsing socket_listener, open /usr/share/collectd/types.db: no such file or directory
```
 - Root Cause

- The agent uses a CollectD plugin for advanced metric collection (for example, CPU, memory, disk, etc.).
Some configurations — especially if you enabled “CollectD” metrics or “Socket Listener” in the setup wizard — expect the file: /usr/share/collectd/types.db

- This file belongs to the collectd package, which is not installed by default on Amazon Linux 2 or Ubuntu EC2 instances.
- Fix Steps
  - Install CollectD
     ```bash
      sudo yum install -y collectd
     ```



## SSM - AWS Systems Manager


#### fleet server
 - Fleet Manager is a console-based tool within AWS Systems Manager (SSM) that helps you manage and monitor your fleet of servers (EC2 and on-premise) — without SSH or RDP.

- Example Scenario
    ```bash
        Let’s say you need to:

        Check a log file (/var/log/httpd/access_log)

        Restart Apache service

         Open Fleet Manager → Instance → File System → /var/log/httpd → View the file
         Then go to Processes → Restart or stop Apache process

        All without logging in via SSH.

        - created EC2 instand with no perssion of SG and also assign role for SSm and use amazon linux AMi so there alredy installed SSM agent on it
    ```
  ![alt text](image-15.png)
  ![alt text](image-16.png)
  ![alt text](image-17.png)
  ![alt text](image-18.png)
  ![alt text](image-19.png)
  ![alt text](image-20.png)


#### SSM - RUN command using document


- created document on ssm for installing httpd and using the document and run command installing on created ec2

    ![alt text](image-21.png)
    ![alt text](image-22.png)
    ![alt text](image-23.png)
    ![alt text](image-24.png)
    ![alt text](image-25.png)
    ![alt text](image-26.png)

 - run this script one at time so chosse one and by percentage
   ![alt text](image-27.png) 
   ![alt text](image-28.png) 
   ![alt text](image-29.png) 
   ![alt text](image-30.png)
   ![alt text](image-31.png)


## CloudFormation  

- created EC2 using CloudFormation

  ![alt text](image-32.png)
  ![alt text](image-33.png)
  ![alt text](image-34.png)
  ![alt text](image-35.png)
  ![alt text](image-36.png)



- update and delete stack

  ![alt text](image-37.png)
  ![alt text](image-38.png)
  ![alt text](image-39.png)
  ![alt text](image-40.png)
  ![alt text](image-41.png)




## Serverless Cost Optimization Notifier

- Create an IAM role with trust policy allowing Lambda, then attach two things:

   - AWS managed policy: AWSLambdaBasicExecutionRole (for CloudWatch logs)

   - Inline policy allowing Cost Explorer read + SNS publish.

      ```bash
            {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "ce:GetCostAndUsage",
            "ce:GetCostAndUsageWithResources",
            "ce:GetDimensionValues",
            "ce:GetCostForecast"
          ],
          "Resource": "*"
        },
        {
          "Effect": "Allow",
          "Action": [
            "sns:Publish"
          ],
          "Resource": "arn:aws:sns:<REGION>:<ACCOUNT_ID>:cost-alert-topic*"
        }
      ]
     }
      ```
    
    

![alt text](image-43.png)


- Created SNS Topic & Subscription 

  ![alt text](image-44.png)
  ![alt text](image-45.png)


- Created Lambda Function and atteched role that created
  ![alt text](image-46.png) 
  ![alt text](image-47.png)


-  set Environment variables
   ![alt text](image-48.png)

- Created an EventBridge (CloudWatch Events) Scheduled Rule
   ![alt text](image-49.png) 
   ![alt text](image-50.png)
   ![alt text](image-51.png)


- tested lamba 
   ![alt text](image-52.png)
   ![alt text](image-53.png)




## servicecatalog


- created role for ServiceCatalogLaunchRole
  ![alt text](image-54.png)

- created simple EC2 web server template (ec2-web.yaml) and upload it to an S3 bucket.
  ![alt text](image-55.png) 

- Created a Portfolio
  ![alt text](image-56.png)


- Created the Product
   ![alt text](image-57.png)
   ![alt text](image-58.png)

- Added Product to Portfolio 
   ![alt text](image-59.png)  


- Added Launch Constraint
  ![alt text](image-60.png)
  ![alt text](image-61.png)
  ![alt text](image-62.png)

-   Give Access to User
    ![alt text](image-63.png)



- now loging with i am user and  launch the product
  ![alt text](image-64.png) 
  ![alt text](image-65.png) 
  ![alt text](image-66.png) 
  ![alt text](image-67.png)
  ![alt text](image-68.png)





## Cross Account vpc peering



- created vpc with 4 subnet(2-pulic and 2 -private)
   ![alt text](image-69.png)


- created  Internet gateway and atteched to created vpc
   ![alt text](image-74.png)

- created NAT gateway in public subnet
  ![alt text](image-75.png)   


- created two Route tables
    - public Route table : associated 2 public subnet
    - private Route table : associated 2 private subnet
      ![alt text](image-70.png)
      ![alt text](image-72.png)
      ![alt text](image-71.png)
      ![alt text](image-73.png)
  


- cretaed two ec2 instances
    - public-ec2 - created in publice subnet
    - private-ec2 - created in private subnet

      ![alt text](image-77.png)
      - in private ec2 sg allow from pub-ec2 sg
      ![alt text](image-78.png)


- now i am successfully able to access internet on ec2 as well able to connect private ec2 and also able to access internet on private ec2
![alt text](image-76.png)



- now created cross region vpc peering
  ![alt text](image-79.png)

- now in to another account accept request
  ![alt text](image-80.png)
  ![alt text](image-81.png)



- edit rout destination = another account vpc cider and target is peering connection
 ![alt text](image-83.png)



- now edited publice ec2 sg to ssh from another account vpc cidr
 ![alt text](image-91.png)



- now i am able to loging into second account ec2 with all secinirio

    - my pub-ec2 to my private-ec2 to another account public-ec2 to private ec2 of second account
    - my pub-ec2 to  another account public-ec2 to private ec2 of second account
    ![alt text](image-86.png)
    ![alt text](image-85.png)


- EventBridge Cross Account
  
- Go to Event Bus - Add resoruce policy to Allow to Account B can put their events into My Account A. 
  ![alt text](image-92.png) 


- Go to Account A and Define EventBridge Rule for EC2 for Status: running
- Assign Resource Policy to EventBridge for Put Event from Account A to Account B by using ARN of EventBridge Default Bus of Account B.
   ![alt text](image-87.png)
   ![alt text](image-88.png)
   ![alt text](image-89.png)
   ![alt text](image-90.png)


- Go to Account B > Create Role for SSM and give permissions.

![alt text](image-93.png)

 
- Create SSM Doc To install nginx

![alt text](image-94.png)

- Create EventBridge Rule in Account B.
- To Trigger SSM Automation in Account A - Choose Target As Account A.

```bash 
  {
    
    "source": ["aws.ec2"],
    "account": ["490909520477"],
    "detail-type": ["EC2 Instance State-change Notification"],
    "detail": { "state": ["running"] }
  }
  ```
  
- Choose target as SSM and Give ARN of SSM Role

  ![alt text](image-95.png)


  


