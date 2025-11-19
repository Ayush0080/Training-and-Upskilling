# AWS - Classic Load Balancer 
## Create EKS Node Group in Private Subnets

- We are going to create a node group in VPC Private Subnets
- We are going to deploy workloads on the private node group wherein workloads will be running private subnets and load balancer gets created in public subnet and accessible via internet.


-  Creates EKS Cluster using eksctl

```bash
# Create Cluster
eksctl create cluster --name=eksdemo1 \
                      --region=us-east-1 \
                      --zones=us-east-1a,us-east-1b \
                      --without-nodegroup 

# Get List of clusters
eksctl get cluster                  

```
![alt text](image.png)
![alt text](image-1.png)

- Created & Associate IAM OIDC Provider for our EKS Cluster
   - To enable and use AWS IAM roles for Kubernetes service accounts on our EKS cluster, we must create & associate OIDC identity provider.


 ```bash
  eksctl utils associate-iam-oidc-provider \
    --region us-east-1 \
    --cluster eksdemo1 \
    --approve

 ```  
 ![alt text](image-2.png)


- Created EKS Node Group in Private Subnets
   - Key option for the command is ``--node-private-networking``

 ```bash
eksctl create nodegroup --cluster=eksdemo1 \
                        --region=us-east-1 \
                        --name=eksdemo1-ng-private1 \
                        --node-type=t3.medium \
                        --nodes-min=2 \
                        --nodes-max=4 \
                        --node-volume-size=20 \
                        --ssh-access \
                        --ssh-public-key=kube-demo \
                        --managed \
                        --asg-access \
                        --external-dns-access \
                        --full-ecr-access \
                        --appmesh-access \
                        --alb-ingress-access \
                        --node-private-networking                      
 ```  


- External IP Address should be none if our Worker Nodes created in Private Subnets
![alt text](image-3.png)


- Installed  EKS Pod Identity Agent to use EKS Pod Identity to grant AWS IAM permissions to pods through Kubernetes service accounts.
![alt text](image-7.png)


## Created RDS Database
#### Create DB Security Group

- Create security group to allow access for RDS Database on port 3306
- Security group name: eks_rds_db_sg
- Description: Allow access for RDS Database on Port 3306
- VPC: eksctl-eksdemo1-cluster/VPC
- Inbound Rules
    - Type: MySQL/Aurora
    - Protocol: TPC
    - Port: 3306
    - Source: Anywhere (0.0.0.0/0)
    - Description: Allow access for RDS Database on Port 3306
- Outbound Rules
  - Leave to defaults
![alt text](image-4.png)

#### Create DB Subnet Group in RDS

- Go to RDS -> Subnet Groups
- Click on Create DB Subnet Group
    - Name: eks-rds-db-subnetgroup
    - Description: EKS RDS DB Subnet Group
    - VPC: eksctl-eksdemo1-cluster/VPC 
    - Availability Zones: us-east-1a, us-east-1b
    - Subnets: 2 subnets in 2 AZs --> private subnet
     - Click on Create
![alt text](image-5.png)
![alt text](image-6.png)
![alt text](image-8.png)

#### Create RDS Database

- Go to Services -> RDS
- Click on Create Database
    - Choose a Database Creation Method: Standard Create
    - Engine Options: MySQL
    - Edition: MySQL Community
    - Version: 5.7.22 (default populated)
    - Template Size: Free Tier
    - DB instance identifier: usermgmtdb
    - Master Username: dbadmin
    - Master Password: 
    - Confirm Password: 
    - DB Instance Size: leave to defaults
    - Storage: leave to defaults
    - Connectivity
        - VPC: eksctl-eksdemo1-cluster/VPC
        - Additional Connectivity Configuration
            - Subnet Group: eks-rds-db-subnetgroup
            - Publicyly accessible: YES (for our learning and troubleshooting - if required)
        - VPC Security Group: Create New
            - Name: eks-rds-db-securitygroup
         - Availability Zone: No Preference
        - Database Port: 3306
  - Rest all leave to defaults
- Click on Create Database

![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
![alt text](image-12.png)
![alt text](image-13.png)
![alt text](image-14.png)


- Created Kubernetes externalName service Manifest and Deploy
![alt text](image-15.png)

    ```bash
    kubectl apply -f kube-manifests/01-MySQL-externalName-Service.yml

    ```
![alt text](image-16.png)

- Connect to RDS Database using kubectl and create usermgmt schema/db

```bash
kubectl run -it --rm --image=mysql:latest --restart=Never mysql-client -- mysql -h usermgmtdb.c0lo6i6iophi.us-east-1.rds.amazonaws.com -u dbadmin -#passws

mysql> show schemas;
mysql> create database usermgmt;
mysql> show schemas;
mysql> exit

```

![alt text](image-17.png)


#### created AWS Classic Load Balancer Kubernetes Manifest & Deploy with web app

![alt text](image-21.png)
![alt text](image-20.png)
![alt text](image-24.png)
![alt text](image-22.png)




