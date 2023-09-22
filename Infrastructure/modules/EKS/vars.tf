variable "cluster_name" {}

variable "cluster_version" {}

variable "cluster_role_arn" {}

variable "cluster_subnet_id" {}

variable "cluster_security_group_ids" {}

variable "cluster_dependency_attachment" {
    type = list(string)
}


variable "worker_node_name" {}

variable "worker_node_role_arn" {}

variable "worker_node_subnet_id" {}

variable "worker_node_dependency_attachment" {
    type = list(string)
}
