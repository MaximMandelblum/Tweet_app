#-----compute/variables.tf

variable "key_name" {}

variable "public_key_path" {}

variable "instance_count" {}

variable "instance_type" {}

variable "security_group" {}

variable "subnets" {
  type = "list"
}

variable "ami_string" {}


variable "elb_sec_group" {}

