## EKS-Storage-with-RDS-Database


#### Create RDS Database

- vpc of eks cluster
  ![alt text](image.png)

-  Created DB Security Group
   ![alt text](image-1.png)

- Created DB Subnet Group in RDS
  ![alt text](image-2.png)
  ![alt text](image-3.png)

   -  slelect private subnet
      ![alt text](image-4.png) 
      ![alt text](image-5.png)   


- Created RDS Database    
  ![alt text](image-6.png)
  ![alt text](image-7.png)
  ![alt text](image-8.png)
  ![alt text](image-9.png)
  ![alt text](image-10.png)
  ![alt text](image-11.png)
  ![alt text](image-12.png)

####  Create Kubernetes externalName service Manifest and Deploy

![alt text](image-13.png)
![alt text](image-14.png)

- Connect to RDS Database using kubectl and create usermgmt schema/db
```bash
kubectl run -it --rm --image=mysql:latest --restart=Never mysql-client -- mysql -h usermgmtdb.c0lo6i6iophi.us-east-1.rds.amazonaws.com -u admin -pdbpassword11

mysql> show schemas;
mysql> create database usermgmt;
mysql> show schemas;
mysql> exit

```

![alt text](image-15.png)


- Deploy with web app

![alt text](image-16.png)


