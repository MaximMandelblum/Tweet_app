aws_region = "us-east-1"
accessip = "0.0.0.0/0"
vpc_cidr = "172.34.0.0/16"
public_cidrs = [
    "172.34.32.0/20",
    "172.34.0.0/20"
    ]

key_name = "terraform_key" 
public_key_path = "/home/centos/.ssh/id_rsa.pub"
server_instance_type = "t2.micro" 
instance_count = 1
ami_string = "ami-02eac2c0129f6376b"
