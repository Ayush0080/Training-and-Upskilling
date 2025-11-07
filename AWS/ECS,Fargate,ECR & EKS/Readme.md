### Amazon ECS 

- Amazon ECS (Elastic Container Service) is a fully managed container orchestration service provided by AWS.
   - In simple terms:
       - ECS helps you run, manage, and scale Docker containers easily without worrying about servers.



| Component           | Description                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Cluster**         | A logical group of compute resources (EC2 instances or Fargate) where your containers run.                   |
| **Task Definition** | A blueprint (JSON file) describing which Docker container to run, what image to use, ports, CPU/memory, etc. |
| **Task**            | A running instance of a Task Definition (actual container).                                                  |
| **Service**         | Ensures that the specified number of tasks are always running and can load-balance traffic.                  |
| **ECS Agent**       | A small process on each EC2 instance that communicates with ECS control plane.                               |
| **ECS Scheduler**   | Decides where to place new tasks within the cluster.                                                         |


##### ECS launch type

| Type                    | Description                                                                   | Use Case                                                         |
| ----------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **EC2 Launch Type**     | You manage EC2 instances (cluster nodes) that run your containers.            | When you need control over underlying servers.                   |
| **Fargate Launch Type** | Serverless mode — you don’t manage servers; AWS runs your containers for you. | When you just want to run containers, not manage infrastructure. |
