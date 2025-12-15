## Jenkins pipeline

- go to the jenkins home page selcer new item
![alt text](image.png)

- give name of pipeline an Select an item type as pipeline
![alt text](image-1.png)


- in Configure section select pipeline
![alt text](image-2.png)

- now created one demo pipeline script that's create directory and file and also append content of echo command output and save 

    ![alt text](image-3.png)


- bulid the peipeline

    ![alt text](image-4.png)
    ![alt text](image-5.png)  



### Jenkins workspace

- Jenkins workspace is the file system location where Jenkins executes a job and keeps all files related to that job.

- Clean before build

```bash
cleanWs()

```
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)



### Build Artifacts
-  Build artifacts are the output files produced by a Jenkins build that you want to save, share, or deploy later.


- this file firstly clear workspace and store newly created Build Artifacts 
![alt text](image-10.png)


### Combining multiple shell steps (sh) into one
![alt text](image-11.png)

