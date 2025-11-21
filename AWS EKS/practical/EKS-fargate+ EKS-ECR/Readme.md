# Deployed Web Application on Amazon EKS Fargate with Public Access via ALB Ingress

#### Create EKS Fargate Cluster (us-west-2)
```bash
eksctl create cluster \
  --name fargate-demo \
  --region us-west-2 \
  --fargate
```
![alt text](image.png)
![alt text](image-1.png)

#### Create Namespace
```bash
kubectl create namespace demo
```
![alt text](image-2.png)

#### Create Fargate Profile
```bash
eksctl create fargateprofile \
  --cluster fargate-demo \
  --name fp-default \
  --namespace demo
```
![alt text](image-3.png)
![alt text](image-4.png)

#### Create Deployment YAML 
```bash

deploy-app.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: demo-app
  namespace: demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: demo-app
  template:
    metadata:
      labels:
        app: demo-app
    spec:
      containers:
        - name: demo-app
          image: 075285241029.dkr.ecr.us-west-2.amazonaws.com/demo-app:latest
          ports:
            - containerPort: 80
```

- Apply:
```bash
kubectl apply -f deploy-app.yaml
```
![alt text](image-5.png)

- Create Service YAML (ClusterIP)
```bash
service.yaml
apiVersion: v1
kind: Service
metadata:
  name: demo-service
  namespace: demo
spec:
  type: ClusterIP
  selector:
    app: demo-app
  ports:
    - port: 80
      targetPort: 80
```

- Apply:
```bash
kubectl apply -f service.yaml
```
![alt text](image-6.png)

#### Install AWS ALB Ingress Controller
```bash
 #Required for Internet access

eksctl utils associate-iam-oidc-provider --cluster fargate-demo --approve
```
![alt text](image-7.png)
#### Install IAM Policy:

```bash
curl -o alb-iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
```
#### Create the IAM policy
```bash
  aws iam create-policy \
  --policy-name AWSLoadBalancerControllerIAMPolicy \
  --policy-document file://alb-iam-policy.json

# arn = arn:aws:iam::075285241029:policy/AWSLoadBalancerControllerIAMPolicy
```
![alt text](image-8.png)

#### Create IAM Role and service account :
```bash
eksctl create iamserviceaccount \
  --cluster fargate-demo \
  --namespace kube-system \
  --name aws-load-balancer-controller \
  --attach-policy-arn arn:aws:iam::075285241029:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve \
  --override-existing-serviceaccounts

```
![alt text](image-9.png)
![alt text](image-10.png)
![alt text](image-11.png)
#### Install ALB Controller:
```bash
helm repo add eks https://aws.github.io/eks-charts
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=fargate-demo \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller
```
![alt text](image-12.png)
![alt text](image-13.png)
#### Create Ingress (ALB)
```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: demo-ingress
  namespace: demo
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
spec:
  ingressClassName: alb
  rules:
    - http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: demo-service
                port:
                  number: 80
```
- Apply:
```bash
kubectl apply -f ingress.yaml
```
![alt text](image-14.png)
#### Get ALB URL
```bash
kubectl get ingress -n demo
```
![alt text](image-15.png)

![alt text](image-17.png)
![alt text](image-16.png)

