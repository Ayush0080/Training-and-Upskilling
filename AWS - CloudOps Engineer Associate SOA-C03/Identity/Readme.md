## IAM Access Analyzer

- It continuously scans resource policies (like those on S3, IAM roles, KMS keys, etc.) and tells you if anyone outside your AWS account or Organization has access to them.

- Think of it as your "who can access my stuff?" detector inside AWS.


    | Resource                          | What It Detects                 | Example Finding                                               |
    | --------------------------------- | ------------------------------- | ------------------------------------------------------------- |
    | **S3 Bucket Policy**              | Public or cross-account access  | "This bucket allows public read access (Principal: *)"        |
    | **IAM Role Trust Policy**         | Cross-account role assumption   | "Role `ProdAdminRole` can be assumed by account 222222222222" |
    | **KMS Key Policy**                | External account access         | "External account 333333333333 has decrypt permission"        |
    | **SQS Queue or SNS Topic Policy** | Access from another AWS account | "Queue policy allows account 444444444444 to send messages"   |


## Federation

- Identity Federation means allowing users from an external identity provider (IdP) — like your company’s Active Directory, Okta, Google Workspace, or Azure AD — to access AWS resources without creating IAM users in AWS.

- In short: “Sign in elsewhere, get access to AWS temporarily.”

    | Federation Type               | Technology                                     | Used For                                                                                        |
    | ----------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------- |
    | **SAML 2.0 Federation**       | Security Assertion Markup Language (XML-based) | Enterprise logins to AWS Console or CLI (SSO via corporate IdP like Okta, Azure AD, ADFS)       |
    | **Amazon Cognito Federation** | OpenID Connect (OIDC), OAuth 2.0, or SAML      | Web/mobile app authentication for end users (like Google, Facebook, Apple, or your company SSO) |


## IAM Policy Simulator

- The AWS IAM Policy Simulator is a tool that lets you test and troubleshoot IAM and resource-based policies — without actually performing the actions in your AWS environment.

- It helps you simulate the effect of IAM policies (user, group, role, or resource policies) to see whether a specific action on a specific resource would be allowed or denied.


    | Scenario                                         | Why You’d Use It                                                |
    | ------------------------------------------------ | --------------------------------------------------------------- |
    |  Troubleshooting “Access Denied” errors        | Check which policy or SCP is blocking access.                   |
    |  Testing new IAM policies safely               | Validate before deploying to production.                        |
    |  Learning how policies combine                 | Understand how allow/deny from multiple policies work together. |
    |  Validating SCP or permission boundary effects | See if organization or boundary restrictions apply.             |
    |  Automation                                    | Integrate with CI/CD to test permissions automatically.         |
