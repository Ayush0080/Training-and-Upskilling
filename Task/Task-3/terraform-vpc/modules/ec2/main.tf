resource "aws_instance" "bastion" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.public_subnet_id
  key_name      = var.key_name
  vpc_security_group_ids = [var.bastion_sg_id]

  tags = { Name = "bastion-host" }
}

resource "aws_instance" "private" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.private_subnet_id
  key_name      = var.key_name
  vpc_security_group_ids = [var.private_sg_id]

  tags = { Name = "private-ec2" }
}