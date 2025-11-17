## EKS Pod Identity (PIA = Pod Identity Agent )

- EKS Pod Identity is an AWS feature that allows Kubernetes Pods to securely obtain temporary AWS IAM credentials without requiring IAM Roles for Service Accounts (IRSA) or OIDC providers. It provides native IAM integration directly through the EKS control plane.

  - Your Pod can access AWS services (S3, DynamoDB, SQS, SNS, etc.) without storing credentials,and without creating OIDC provider + IAM trust policies.

- ```service account``` is the identity for pods to authenticate and access Kubernetes resources or cloud services securely.



