variable "public_subnet_id" {}
variable "private_subnet_id" {}
variable "bastion_sg_id" {}
variable "private_sg_id" {}
variable "key_name" {}
variable "ami_id" {
  description = "AMI ID for EC2 instances"
  type        = string
  default = "ami-00ca570c1b6d79f36"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

