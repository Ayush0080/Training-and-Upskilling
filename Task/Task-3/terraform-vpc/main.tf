provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source = "./modules/vpc"

  vpc_cidr       = var.vpc_cidr    # Inputs passed
  public_subnets = var.public_subnets
  private_subnets = var.private_subnets
}

module "security_group" {
  source = "./modules/security-group"

  vpc_id = module.vpc.vpc_id # Module Dependency
}

module "ec2" {
  source = "./modules/ec2"

  public_subnet_id  = module.vpc.public_subnet_ids[0]
  private_subnet_id = module.vpc.private_subnet_ids[0]

  bastion_sg_id = module.security_group.bastion_sg_id
  private_sg_id = module.security_group.private_sg_id

  key_name = var.key_name
}
