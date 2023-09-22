resource "aws_security_group" "dev_security_group" {
  name        = var.security_group_name
  description = "Cluster communication with worker nodes"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "dev_cluster_security_group"
  }
}

resource "aws_security_group_rule" "cluster_internal" {
  description       = "Allow nodes to communicate with each other"
  from_port         = 0
  to_port           = 0
  protocol          = "-1"
  security_group_id = aws_security_group.dev_security_group.id
  source_security_group_id = aws_security_group.dev_security_group.id
  type              = "ingress"
}

resource "aws_security_group_rule" "cluster_cni" {
  description       = "Allow workstation / CNI Plugin to communicate with the API Server"
  from_port         = 443
  to_port           = 443
  protocol          = "tcp"
  security_group_id = aws_security_group.dev_security_group.id
  cidr_blocks       = ["0.0.0.0/0"]
  type              = "ingress"
}