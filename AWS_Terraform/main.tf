provider "aws" {
  region                  = "${var.aws_region}"
  shared_credentials_file = "/home/centos/AWS/.aws/credentials"
  profile                 = "terraform"
}

# Deploy Networking Resources

module "networking" {
  source       = "./networking"
  vpc_cidr     = "${var.vpc_cidr}"
  public_cidrs = "${var.public_cidrs}"
  accessip     = "${var.accessip}"
}



module "compute" {
  source          = "./compute"
  instance_count  = "${var.instance_count}"
  key_name        = "${var.key_name}"
  public_key_path = "${var.public_key_path}"
  instance_type   = "${var.server_instance_type}"
  subnets         = "${module.networking.private_subnets}"
  security_group  = "${module.networking.public_sg}"
  elb_sec_group   = "${module.networking.elbsg}"
  ami_string = "${var.ami_string}" 
}
