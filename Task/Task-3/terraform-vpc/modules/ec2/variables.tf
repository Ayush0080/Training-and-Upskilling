variable "public_subnet_id" {}
variable "private_subnet_id" {}
variable "bastion_sg_id" {}
variable "private_sg_id" {}
variable "key_name" {}
variable "ami_id" {
  description = "AMI ID for EC2 instances"
  type        = string
  default = "ami-068c0051b15cdb816"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

