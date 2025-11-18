## Kubernetes - Secrets

- Kubernetes Secrets let you store and manage sensitive information, such as passwords, OAuth tokens, and ssh keys.
- Storing confidential information in a Secret is safer and more flexible than putting it directly in a Pod definition or in a container image.

- to refer secret
    ```bash
        name: DB_PASSWORD
                    valueFrom:
                        secretKeyRef:
                        name: mysql-db-password
                        key: db-password

    ```


## Kubernetes - Init Containers


- ``Init Containers`` are special containers in a Pod that run first, before the main application container starts.
They are used to perform initial setup tasks that must complete successfully before the main container runs.
- Init Containers run before App containers
- Init containers can contain utilities or setup scripts not present in an app image.
- We can have and run multiple Init Containers before App Container.
- Init containers are exactly like regular containers, except:
    - Init containers always run to completion.
    - Each init container must complete successfully before the next one starts.
- If a Pod's init container fails, Kubernetes repeatedly restarts the Pod until the init container succeeds.
- However, if the Pod has a restartPolicy of Never, Kubernetes does not restart the Pod.

    ```bash
    spec:
        initContainers:
            - name: init-db
            image: busybox:1.31
            command: ['sh', '-c', 'echo -e "Checking for the availability of MySQL Server deployment"; while ! nc -z mysql 3306; do sleep 1; printf "-"; done; echo -e "  >> MySQL DB Server has started";']
    ```


## Kubernetes Probes

#### Liveness Probe
- Checks if the container is alive or stuck.

- Purpose : 
    - If the container is unhealthy, K8s will restart it automatically.

    - Example Use

        - App stuck in infinite loop

        - Deadlock

        - App becomes unresponsive


```bash
     # at container level
        livenessProbe:
            exec:
              command:
                - /bin/sh
                - -c
                - nc -z localhost 8095
            initialDelaySeconds: 60
            periodSeconds: 10
            

```
| Field                       | Meaning                                                    |
| --------------------------- | ---------------------------------------------------------- |
| **initialDelaySeconds: 60** | Wait 60 seconds after pod starts before first health check |
| **periodSeconds: 10**       | After that, check pod health every 10 seconds              |


#### Readiness Probe
- Checks if the container is ready to serve traffic.

- Purpose : 

    - When NOT ready → Removed from Service ENDPOINTS

    - No traffic will be sent to it.

    - Use Case

       -  App still loading configuration

        - Waiting for DB connection

        - Cache building

```bash
         # at container level
          readinessProbe:
            httpGet:
              path: /usermgmt/health-status
              port: 8095
            initialDelaySeconds: 60
            periodSeconds: 10     

```
| Field                       | Meaning                                                    |
| --------------------------- | ---------------------------------------------------------- |
| **initialDelaySeconds: 60** | Wait 60 seconds after pod starts before first health check |
| **periodSeconds: 10**       | After that, check pod health every 10 seconds              |


#### Startup Probe
- Checks if the container has successfully started.
- Startup Probe gives your application extra time to start, so that Kubernetes does NOT kill it too early.
- It disables the liveness probe until the app is fully started.

- Purpose:

    - Gives slow-starting applications more time before K8s kills them with a liveness probe.

    - Used along with livenessProbe.

    - Use Case

        - Java apps (Spring Boot)

        - Big Node.js apps

        - Heavy initialization


## Kubernetes-Requests-Limits

- Request = Minimum guaranteed resources for a container

  - When you set a request, you tell Kubernetes:

     - container needs at least this much CPU/Memory to run

     - Kubernetes scheduler will place your pod on a node that has at least that much resources available.
- Example :
    ```bash
    # container level
    resources:
    requests:
        cpu: "200m"       # 0.2 CPU
        memory: "256Mi"   # 256 MB

    # Pod needs minimum 0.2 CPU and 256 MB RAM to be scheduled.    
    ```

- Limit = Maximum amount of CPU & Memory a container is allowed to use

     - Do not allow my container to use more than this

-  Example :

    ```bash
    # container level
    resources:
    limits:
        cpu: "1"          # 1 CPU
        memory: "512Mi"   # 512 MB

        # Pod cannot use more than 1 full CPU

       # Pod cannot use more than 512 MB RAM
    ```
- If container tries to use more than limit:
    - CPU → throttle CPU usage will be throttled (slow down)
    - RAM → kill pod OOMKilled (killed by Kubernetes)


## Kubernetes-Namespaces
- A Kubernetes Namespace is a virtual cluster inside a physical Kubernetes cluster.
It provides logical isolation between Kubernetes resources such as:
  - Pods
  - Services
  - Deployments
  - ConfigMaps
  - Secrets
  - PVCs
  - NetworkPolicies
  - ResourceQuotas

- Namespaces help organize, isolate, and manage resources in a shared cluster.

##### Kubernetes automatically creates 4 default namespaces when a cluster is created.
-  default

    - All your resources (Pods, Deployments, Services) go here if you don’t specify any namespace.

    - Think of it as the work area.

- kube-system

    - Contains system components installed by Kubernetes.

    - Example resources:

        - kube-dns / CoreDNS

        - kube-proxy

        - kube-scheduler

        - kube-controller-manager

   - Never deploy your applications here.

- kube-public

    - Publicly accessible namespace.

    - Contains a ConfigMap that holds cluster info:

        - cluster-info

    - Anyone (even unauthenticated users) can read it.

- kube-node-lease

    - Stores heartbeat leases for each node.

    - Used by kubelet to let Kubernetes know the node is alive.

    - Makes node failure detection faster.





#### Namespaces-LimitRange-default


- A LimitRange is a Kubernetes object that sets default CPU/Memory requests & limits for containers inside a namespace.

    ```bash

    apiVersion: v1
    kind: LimitRange
    metadata:
    name: my-limits
    namespace: dev1
    spec:
    limits:
    - type: Container
        default:
        cpu: "500m"
        memory: "1Gi"
        defaultRequest:
        cpu: "250m"
        memory: "512Mi"
        min:
        cpu: "100m"
        memory: "256Mi"
        max:
        cpu: "1"
        memory: "2Gi"


    ```