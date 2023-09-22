output "cluster_arn" {
  value = aws_iam_role.eks_cluster_role.arn
}

output "worker_arn" {
  value = aws_iam_role.eks_cluster_role.arn
}


output "EKSClusterPolicy" {
  value = aws_iam_role_policy_attachment.AmazonEKSClusterPolicy.id
}

output "AmazonEKSServicePolicy" {
  value = aws_iam_role_policy_attachment.AmazonEKSServicePolicy.id
}

output "AmazonEKSVPCResourceController" {
  value = aws_iam_role_policy_attachment.AmazonEKSVPCResourceController.id
}

output "AmazonEKSWorkerNodePolicy" {
  value = aws_iam_role_policy_attachment.eks_worker_node_policy.id
}

output "AmazonEC2ContainerRegistryReadOnly" {
  value = aws_iam_role_policy_attachment.eks_ecr_read_only_policy.id
}







output "WorkerNodes_Policy" {
  value = aws_iam_policy_attachment.WorkerNodes_Policy.id
}

output "CNI_Policy" {
  value = aws_iam_policy_attachment.CNI_Policy.id
}

output "ECR_Policy" {
  value = aws_iam_policy_attachment.ECR_Policy.id
}