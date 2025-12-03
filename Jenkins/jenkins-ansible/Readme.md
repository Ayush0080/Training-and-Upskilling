## Jenkins + Ansible

#### Created Dockerfile using jenkins as base image 
![alt text](image.png)
-  Created docker-compose file 
   - in side that jenkins we installed ansible

  ![alt text](image-1.png)


#### Make the ssh keys permanent on the Jenkins container
- when ansible need to ssh into the host that time need key to authenticat 
![alt text](image-2.png)

- created key-pair
    ```bash
    ssh-keygen -f ansible
    ```
  ![alt text](image-3.png) 
  ![alt text](image-4.png)

- we copy privat key into ``jenkins_home/ansible/`` folder as we mounted this folder into local volume with  jenkins conatiner 
  ![alt text](image-6.png)
  ![alt text](image-5.png)

#### Created Ansible Inventory  
  - created this inventory file in ``jenkins_home/ansible/`` folder as we mounted this folder into local volumewith  jenkins conatiner 
  
#### login into jenkins container 
  ![alt text](image-7.png)

#### try to ping into my ec2
![alt text](image-8.png)
  
#### Create your first Ansible Playbook  
![alt text](image-10.png)

- test the playbook
  ![alt text](image-11.png)
  ![alt text](image-12.png)
  ![alt text](image-13.png)



## Integrate Ansible and Jenkins and run playbook using jenkins

- install ansible plugin 

- test ansible using jenkins
![alt text](image-14.png)
![alt text](image-15.png)

- give path of playbook and inventory file as where jenkins is running
![alt text](image-16.png)
![alt text](image-17.png)


 
