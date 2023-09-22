resource "aws_eks_cluster" "dev_cluster" {
  name           = var.cluster_name
  version        = var.cluster_version
  role_arn       = var.cluster_role_arn

  vpc_config {
    security_group_ids = [var.cluster_security_group_ids]
    subnet_ids = "${var.cluster_subnet_id}"
  }

  depends_on = [var.cluster_dependency_attachment]

  tags = {
    Name = "eks-cluster"
  }
}

resource "aws_eks_node_group" "dev_worker_node" {
  cluster_name    = aws_eks_cluster.dev_cluster.name
  node_group_name = var.worker_node_name
  node_role_arn   = var.worker_node_role_arn
  subnet_ids      = var.worker_node_subnet_id

  capacity_type = "ON_DEMAND"
  instance_types = ["c5.xlarge"]

  scaling_config {
    desired_size = 2
    max_size     = 2
    min_size     = 1
  }

  update_config {
    max_unavailable = 1
  }

  depends_on = [var.worker_node_dependency_attachment]

}