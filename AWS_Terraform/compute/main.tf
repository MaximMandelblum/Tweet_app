#-----compute/main.tf
resource "aws_key_pair" "tf_auth" {
  key_name   = "${var.key_name}"
  public_key = "${file(var.public_key_path)}"
}

resource "aws_instance" "tf_server_docker" {
  count         = "${var.instance_count}"
  instance_type = "${var.instance_type}"
  ami           = "${var.ami_string}"

  tags {
    Name = "tf_server-docker-${count.index +1}"
  }

  key_name               = "${aws_key_pair.tf_auth.id}"
  vpc_security_group_ids = ["${var.security_group}"]
  subnet_id              = "${element(var.subnets, count.index)}"
}

resource "aws_eip" "ip" {
  count = "${var.instance_count}"
  instance = "${element(aws_instance.tf_server_docker.*.id, count.index)}"
}

data "aws_availability_zones" "allzones" {}

resource "aws_elb" "elb1" {
name = "terraform-elb"
#availability_zones = ["${data.aws_availability_zones.allzones.names}"]
security_groups = ["${var.elb_sec_group}"]
subnets         = ["${element(var.subnets, count.index)}"]



listener {
instance_port = 8082
instance_protocol = "http"
lb_port = 80
lb_protocol = "http"
}
health_check {
healthy_threshold = 2
unhealthy_threshold = 2
timeout = 3
target = "HTTP:8082/"
interval = 30
}

instances = ["${aws_instance.tf_server_docker.*.id}"]
cross_zone_load_balancing = true
idle_timeout = 400
connection_draining = true
connection_draining_timeout = 400

tags {
Name = "terraform-elb"
}
}

