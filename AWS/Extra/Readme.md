# IAM Permission Boundary
- A permission boundary is a limit (or maximum scope) on the permissions that an IAM user or IAM role can have — even if you attach policies that try to give more access.

    | Component                 | What it does                          | Example             |
    | ------------------------- | ------------------------------------- | ------------------- |
    | **IAM Policy**            | Grants permissions                    | “Allow EC2 and S3”  |
    | **Permission Boundary**   | Restricts maximum allowed permissions | “Allow only S3”     |
    | **Effective Permissions** | Intersection of both                  | “Only S3” allowed |

- You are an AWS admin, and you create users for your team:
  - user1 (developer)
  - user2 (tester)

  - You want user1 to create IAM roles, but you don’t want him to accidentally create a role with AdministratorAccess (too much power).
  - user1 can create roles, but those roles must never have more permissions than I allow.”
  - That limit you set is called a Permission Boundary.


