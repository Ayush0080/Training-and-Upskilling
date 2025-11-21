# AWS Fargate

- AWS Fargate is a serverless compute engine for containers.
- It lets you run containers without managing EC2 instances, nodes, or servers.
  - You only define:

     - CPU

    - Memory

    - Container image

    - Networking

    - And AWS runs it automatically


- Fargate Profile

    - A Fargate Profile tells EKS which pods should run on Fargate instead of EC2 nodes.
    - It acts like a rule/selector for scheduling pods onto Fargate.


- A Fargate Profile contains:

    - Namespace (required)

    - All pods in this namespace will run on Fargate (unless further filtered).

    - Label selectors (optional)

    - Only pods matching these labels will run on Fargate.

    - IAM Role for Pods

    - Subnets where the Fargate pods will run

    - Execution Role to pull images / write logs






