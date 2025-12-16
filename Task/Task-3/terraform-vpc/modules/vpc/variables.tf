variable "vpc_cidr" {}
variable "public_subnets" {}
variable "private_subnets" {}

variable "availability_zones" {
  description = "List of AZs to use"
  type        = list(string)
  default     = ["ap-south-1a", "ap-south-1b"]
}
