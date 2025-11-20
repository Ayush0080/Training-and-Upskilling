## AWS Load Balancer Controller - Ingress Basics


#### ingress manifest -key items


- ``ingress annotations`` : Ingress annotations are extra settings you add in your Ingress YAML to control how the ALB (Application Load Balancer) should behave in EKS

```bash
metadata:
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing


```

- ```ingress spec ingress class name```
    - Because you may have multiple Ingress controllers running in the cluster.

    - Example:

        - Nginx Ingress Controller

        - AWS ALB Ingress Controller

        - If you create an Ingress YAML, Kubernetes must know:

        - “Which controller should manage this Ingress?”

    ```bash
        spec:
            ingressClassName: alb

        spec:
            ingressClassName: nginx    

    ```     

- ``spec = Specification``
- It contains the full routing configuration for the Ingress resource.

    ```bash
    spec:
    ingressClassName: alb
    rules:
        - host: myapp.example.com
        http:
            paths:
            - path: /
                pathType: Prefix
                backend:
                service:
                    name: my-service
                    port:
                    number: 80
    ```


***
 - ``Default Backend``

    - Default Backend = Fallback service
    - If no Ingress rule matches, traffic goes to the default backend.
        ```bash
        spec:
        defaultBackend:
            service:
            name: default-service
            port:
                number: 80
        ```
- `` Ingress Rule  ``
    - Ingress Rule = Which host/path should go to which service

   -  Same way, in Ingress:

       -  /api → backend-service

       -  /login → auth-service

       -  /app → frontend-service


        ```bash
        spec:
        rules:
            - host: myapp.com
            http:
                paths:
                - path: /api
                    pathType: Prefix
                    backend:
                    service:
                        name: api-service
                        port:
                        number: 80
                - path: /app
                    pathType: Prefix
                    backend:
                    service:
                        name: frontend-service
                        port:
                        number: 80
        ```


- ``Ingress Target Types in AWS Load Balancer Controller(traffice mode)``


   - ``ingress target type - instance``
      - ALB sends traffic to the EC2 instance node (node’s private IP).
      - Then the kube-proxy forwards traffic to the correct Pod.
        - How it works

            ALB → EC2 Node → Pod

        - When to use

            - If your Pods use hostNetwork: true

            - If your Pods use NodePort

            - When you want traffic to go through the node    


   - ``ingress target type - ip``

     - ALB sends traffic directly to the Pod IP.
     - How it works

       - ALB → Pod (Direct)

        When to use

        - Almost always for EKS

        - For deployments, services with ClusterIP

        - Works with Fargate

        - Better performance

        - Lower latency

        - True pod-level load balancing