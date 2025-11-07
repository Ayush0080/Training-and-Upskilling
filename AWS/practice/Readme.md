## High Availability & Scalability

### ALB

- create two EC2 using user data that show istance name 
    ![alt text](image.png)
    ![alt text](image-1.png)


- created ALB ans also created target group
    ![alt text](image-2.png) 
    ![alt text](image-3.png)
    ![alt text](image-4.png)
    ![alt text](image-5.png)
    ![alt text](image-6.png)
    ![alt text](image-7.png)
    ![alt text](image-8.png)
    ![alt text](image-9.png)
    ![alt text](image-10.png)
    ![alt text](image-11.png)






- now change in SG and change only allow access two ec2 uing ALB not directly using public ip of EC2

   - changine inbound rule of SG that atteched to ec2 
       - source = sg of LB

     ![alt text](image-12.png) 
     ![alt text](image-13.png) 
     ![alt text](image-14.png)


-  default Listener rules  redirect all request to to target and now add new rule that if request from /error then give specifice meesage to that

    ![alt text](image-15.png)
    ![alt text](image-16.png)
    ![alt text](image-17.png)
    ![alt text](image-18.png)
     

### NLB

- create two EC2 using user data that show istance name
  ![alt text](image-19.png)

-  created NLB ans also created target group
   ![alt text](image-20.png)
   ![alt text](image-21.png)
   ![alt text](image-22.png)
   ![alt text](image-23.png)
   ![alt text](image-25.png)
   ![alt text](image-34.png)





### ASG

-  created ASG
    ![alt text](image-28.png)
    ![alt text](image-26.png)
    ![alt text](image-27.png)
    ![alt text](image-29.png)
    ![alt text](image-30.png)
    ![alt text](image-31.png)
    ![alt text](image-32.png)
    ![alt text](image-33.png)
    ![alt text](image-35.png)







- created rds  and atteched to EC2 and only able to access using EC2 as i have created Ec2 istance is private using script 

  ![alt text](image-37.png)
  ![alt text](image-38.png)
  ![alt text](image-39.png)

- now deployed flask app in ec2 when i can able to fetch rds data on app 
   ![alt text](image-40.png)

  


### ECS

###### deployed flsk app using ECS



- created image and uploaded to the amzon ECR 
   ![alt text](image-41.png)

   
- now created task  definition  usding created image
   ![alt text](image-42.png)


- created cluster with tasks and services

   ![alt text](image-43.png)
   ![alt text](image-44.png)




### App Runner


- created image and uploaded to the amzon ECR 
   ![alt text](image-41.png)


-  created service using docker image

   ![alt text](image-45.png)
   ![alt text](image-46.png)



  
