module "vpc_net" {
  source = "./modules/VPC"

  vpc_name = "dev_vpc"
}

module "security_group" {
  source = "./modules/SECURITY_GROUP"

  security_group_name     = "dev_security_group"
  vpc_id                  = module.vpc_net.vpc_id
}

module "iam" {
  source = "./modules/IAM"

  cluster_rolename      = "dev_cluster_role"
  worker_node_rolename  = "dev_worker_node_role"
  worker_node_instance_profile = "worker_node_profile"
}


module "eks" {
  source = "./modules/EKS"

  cluster_name               = "dev_cluster"

  cluster_version            = "1.24"

  cluster_role_arn           = module.iam.cluster_arn

  cluster_security_group_ids = module.security_group.sg_id

  cluster_subnet_id          = [
                                module.vpc_net.private_subnet_1a_id, module.vpc_net.private_subnet_1b_id,
                                module.vpc_net.public_subnet_1a_id, module.vpc_net.public_subnet_1b_id
                               ]

  cluster_dependency_attachment   = [ 
                                      module.iam.EKSClusterPolicy, 
                                      module.iam.AmazonEKSServicePolicy, 
                                      module.iam.AmazonEKSVPCResourceController,
                                      module.iam.AmazonEKSWorkerNodePolicy,
                                      module.iam.AmazonEC2ContainerRegistryReadOnly
                                    ]
  
  worker_node_name = "dev_worker_node"

  worker_node_role_arn = module.iam.worker_arn

  worker_node_subnet_id = [module.vpc_net.private_subnet_1a_id, module.vpc_net.private_subnet_1b_id]

  worker_node_dependency_attachment = [module.iam.WorkerNodes_Policy, 
                                       module.iam.CNI_Policy,
                                       module.iam.ECR_Policy]

}


/* The following configuration is used to interact with the Kubernetes cluster 
that you've created with EKS from your local server */

data "aws_eks_cluster" "cluster" {
  name = module.eks.cluster_id
}

data "aws_eks_cluster_auth" "cluster_auth" {
  name = module.eks.cluster_id
}

provider "kubernetes" {
  host                   = data.aws_eks_cluster.cluster.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.cluster.certificate_authority.0.data)
  token                  = data.aws_eks_cluster_auth.cluster_auth.token
  load_config_file       = false
}