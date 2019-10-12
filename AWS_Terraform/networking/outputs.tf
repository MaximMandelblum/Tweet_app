#-----networking/outputs.tf

output "private_subnets" {
  value = "${aws_subnet.tf_private_subnet.*.id}"
}

output "public_sg" {
  value = "${aws_security_group.tf_public_sg.id}"
}

output "elbsg" {
  value = "${aws_security_group.elbsg.id}"
}

