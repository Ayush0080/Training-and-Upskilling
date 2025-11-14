# Kubernetes

- container orchestration - manages and deploys thousands of containers in a cluster

- Cluster :

  - cluster is the highest level of the hierarchy. It is a collection of physical or virtual machines that are all working together to run your containerized applications. A cluster consists of at least one Control Plane and one or more Nodes. The control plane manages the cluster, and the nodes run the applications.

- Node
  - node (formerly called a "minion") is a worker machine in the Kubernetes cluster. It can be a physical server, a virtual machine, or a container that runs the applications. Every node has a kubelet agent, which communicates with the control plane and ensures that the containers on that node are running correctly.

- Pod
  - A pod is the smallest and most basic unit of deployment in Kubernetes. A pod is a single instance of a running application. It's a group of one or more containers that share the same network, storage, and lifecycle. For example, a pod might contain a web application container and a "sidecar" container that collects its logs.

- There are two primary types of nodes in a Kubernetes cluster: the Control Plane and the Worker Nodes.

   - Control Plane Components : 

     The control plane is the brain of the cluster. It is responsible for managing the state of the cluster, making decisions, and responding to events. The main components of the control plane are:

      1. kube-apiserver: This is the front end for the control plane. It exposes the Kubernetes API and validates and configures data for the API objects, such as pods, services, and deployments.

      2. etcd: A distributed, key-value store that stores the cluster's configuration and state. It is the single source of truth for all cluster data.

      3. kube-scheduler: This component watches for newly created pods and assigns them to a worker node. It considers factors such as resource requirements, hardware constraints, and workload-specific requirements to make its decision.

       4. kube-controller-manager: This component runs a set of controller processes. For example, the ReplicationController ensures that the specified number of pods for a replica set is always running.

       5. cloud-controller-manager: This component is a cloud-specific control loop. It handles interactions with the underlying cloud provider's APIs, such as provisioning load balancers or managing storage volumes.


- Worker Node Components : 

     - Worker nodes (also called "Minions" in the past) are the machines that run your containerized applications. They contain the following components:

       1. kubelet: An agent that runs on each worker node. It communicates with the control plane and ensures that the containers in a pod are running and healthy. It handles the PodSpec (YAML manifest) and makes sure the containers are launched and managed correctly.

       2. kube-proxy: A network proxy that runs on each worker node. It manages network rules on the node, enabling communication to your pods from both inside and outside the cluster. It ensures that traffic is routed correctly to the services.

       3. Container Runtime: This is the software that is responsible for running the containers. A popular example is containerd, which is the default runtime for Kubernetes, but other options like CRI-O and Docker are also supported.

####  Minikube :

-  Minikube is a lightweight tool that allows you to run a single-node Kubernetes cluster on your local machine. It's designed specifically for developers and those learning Kubernetes, as it simplifies the process of setting up and managing a cluster without the complexity and resource requirements of a full-scale, multi-node production environment.

 
   | Kind | Version |
   |---|---|
   | Pod | v1 | 
   | Service | v1 |
   | Replicaset | apps/v1 |
   | Deployment | apps/v1 |




#### ReplicaSets
 - ReplicaSet is a Kubernetes controller that ensures a specified number of identical Pod replicas are running at all times. Its main job is to maintain the desired number of Pods for a given application, which provides high availability and fault tolerance.


#### Deployments
-  Deployment is a high-level Kubernetes object that provides a declarative way to manage stateless applications. It's the most common way to deploy and update applications in a Kubernetes cluster.

   - While a ReplicaSet ensures that a specific number of Pods are running, a Deployment adds more powerful features on top of that, such as:

      - Rolling Updates: A Deployment allows you to update your application without any downtime. It gracefully replaces old Pods with new ones, ensuring the application remains available throughout the update process.

     - Rollbacks: If a new version of your application has issues, you can easily roll it back to a previous, stable version with a single command.

     - Scaling: A Deployment can be scaled up or down to change the number of Pod replicas, and it manages the underlying ReplicaSet to maintain the desired state.


#### Services 

- target port : This is the port on the Pod's container where your application is actually listening. The Service routes all incoming traffic from its port to this targetPort on the backend Pods. This is the port your application is configured to use internally (e.g., a web server listening on 8080).
  
- port : This is the port on the Service itself. It's the port that other components inside the cluster (like other Pods) use to access your service. It is a virtual port managed by Kubernetes. 

- nodeport : This is a port on the node itself, in the range of 30000-32767, that is open to external traffic. The NodePort Service type exposes your application on this port on every node in the cluster. This allows you to access the service from outside the cluster using any node's IP address and this port.



    ```bash
    # Check cluster info
    kubectl cluster-info
    #Check client/server version
    kubectl version
    # List all pods
    kubectl get pods
    kubectl get pods -A           # all namespaces
    kubectl get po -o wide        # detailed
    # Describe a pod (deep details)
    kubectl describe pod <pod-name>
    # Create a pod
    kubectl run mypod --image=nginx
    # Delete a pod
    kubectl delete pod mypod
    # Exec inside a pod
    kubectl exec -it <pod-name> -- bash
    # Get pod logs
    kubectl logs <pod-name>
    kubectl logs -f <pod-name>   # follow logs
    # List namespaces
    kubectl get ns
    # Delete namespace
    kubectl delete namespace dev
    # list pod in namespace
    kubectl -n dev get pods
    # Pod logs
    kubectl logs <pod>
    #Logs of a container inside pod
    kubectl logs <pod> -c <container-name>
    # List nodes
    kubectl get nodes
    # Describe node
    kubectl describe node <node-name>
    # Apply manifest
    kubectl apply -f deployment.yaml
    # Delete manifest
    kubectl delete -f deployment.yaml
    ```


 - Every Kubernetes manifest contains 4 mandatory top-level fields:    

    | Field          | Meaning                                                    |
    | -------------- | ---------------------------------------------------------- |
    | **apiVersion** | Specifies API version (e.g., apps/v1, v1)                  |
    | **kind**       | Resource type (e.g., Pod, Deployment, Service)             |
    | **metadata**   | Name, labels, namespace, annotations                       |
    | **spec**       | Actual configuration (containers, replicas, volumes, etc.) |

    ```bash
    apiVersion: v1
    kind: Pod
    metadata:
    name: mypod
    spec:
    containers:
        - name: nginx
        image: nginx:latest
    ```

- ``apiVersion``
   - Defines which Kubernetes API version is used.

    | Resource   | apiVersion             |
    | ---------- | ---------------------- |
    | Pod        | `v1`                   |
    | Service    | `v1`                   |
    | Deployment | `apps/v1`              |
    | Ingress    | `networking.k8s.io/v1` |
    | CronJob    | `batch/v1`             |
    | ConfigMap  | `v1`                   |

 
- ``kind``
  - Specifies which Kubernetes resource the YAML will create.

    ```bash
    Pod
    Deployment
    Service
    Ingress
    ConfigMap
    Secret
    Namespace
    PersistentVolume
    PersistentVolumeClaim
    StatefulSet
    DaemonSet
    Job
    CronJob
    ```
 
- ``metadata``
   - Contains identifying information.
    ```bash
    metadata:
    name: myapp
    namespace: dev
    labels:
        app: frontend
        tier: prod
    annotations:
        owner: xyz
        description: "This is test pod"

    ``` 
    | Field           | Meaning                                |
    | --------------- | -------------------------------------- |
    | **name**        | resource name                          |
    | **namespace**   | default = default                      |
    | **labels**      | used by selectors (important!)         |
    | **annotations** | metadata info (not used for selection) |

- ``spec``
   - This section defines the desired state.
    ```bash
    spec:
    containers:
        - name: nginx
        image: nginx:1.27
        ports:
            - containerPort: 80
        env:
            - name: ENV
            value: prod
    ```




    ```bash
    apiVersion: apps/v1
    kind: Deployment
    metadata:
    name: myapp-deploy
    spec:
    replicas: 3
    selector:
        matchLabels:
        app: myapp
    template:
        metadata:
        labels:
            app: myapp
        spec:
        containers:
            - name: app-container
            image: nginx:latest
            ports:
                - containerPort: 80
            env:
                - name: ENV
                value: prod



    ```   

    | Field            | Meaning              |
    | ---------------- | -------------------- |
    | **replicas**     | # of pods            |
    | **selector**     | labels to match pods |
    | **template**     | pod specification    |
    | **containers[]** | container details    |
    | **image**        | image used           |
    | **ports**        | exposed ports        |

    ```bash

    apiVersion: v1
    kind: Service
    metadata:
    name: myapp-service
    spec:
    type: NodePort
    selector:
        app: myapp
    ports:
        - port: 80
        targetPort: 80
        nodePort: 30080


    ```

    | Field      | Meaning                           |
    | ---------- | --------------------------------- |
    | type       | ClusterIP, NodePort, LoadBalancer |
    | selector   | maps service → pods               |
    | port       | service port                      |
    | targetPort | container port                    |
    | nodePort   | host port (30000–32767)           |
