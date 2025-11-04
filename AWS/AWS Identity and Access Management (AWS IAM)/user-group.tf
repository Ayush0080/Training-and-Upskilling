
provider "aws" {
  region = "us-east-1"
}


resource "random_password" "upskill_pwd" {
  length  = 12
  special = true
}

resource "aws_iam_user" "upskill" {
  name          = "upskill"
  force_destroy = true
}


resource "aws_iam_user_login_profile" "upskill_profile" {
  user                    = aws_iam_user.upskill.name
  password_length          = 12
  password_reset_required  = false
}

resource "aws_iam_group" "admin" {
  name = "admin"
}


resource "aws_iam_group_policy_attachment" "admin_policy" {
  group      = aws_iam_group.admin.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

resource "aws_iam_user_group_membership" "add_upskill_to_admin" {
  user   = aws_iam_user.upskill.name
  groups = [aws_iam_group.admin.name]
}


output "user_login_info" {
  value = {
    username         = aws_iam_user.upskill.name
    password         = aws_iam_user_login_profile.upskill_profile.password
    console_login_url = "https://signin.aws.amazon.com/console"
  }
  sensitive = true
}
