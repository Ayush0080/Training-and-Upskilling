## installation


- created docker compose file and deployed
  ![alt text](image.png)

- to check login password 
  ```bash
  docker logs -f c552cb522b09 (# container id)
  # or
  docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword


  ```  
    ![alt text](image-1.png)



## Created job
![alt text](image-2.png)
![alt text](image-4.png)
![alt text](image-5.png)



## Add parameters in job
![alt text](image-6.png)
![alt text](image-9.png)
![alt text](image-8.png)
![alt text](image-10.png)


