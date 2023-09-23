# Project README

## Table of Contents
- [Project Overview](#project-overview)
- [Infrastructure Provisioning](#infrastructure-provisioning)
- [Application Deployment](#application-deployment)
- [Testing](#testing)
- [Continuous Integration/Continuous Deployment (CI/CD)](#continuous-integrationcontinuous-deployment-cicd)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project is designed to provision an Amazon Elastic Kubernetes Service (EKS) cluster using Terraform, deploy Kubernetes applications using Helm charts, and ensure security and compliance by performing automated auditing and remediation of configurations. Below are the key components and technologies used in this project:

## Project Architecture

![Screenshot from 2023-09-22 23-23-24](https://github.com/abdulmalik-devs/terraform-k8-helm-python/assets/62616273/ce754258-d609-4fbd-bc4f-656fb2c9848e)

## Python Script OutPut

https://github.com/abdulmalik-devs/terraform-k8-helm-python/assets/62616273/5dbbaab1-8039-471b-b41d-3f12f14ac646

## Jenkins Deployment

https://github.com/abdulmalik-devs/terraform-k8-helm-python/assets/62616273/0c6d255c-84ec-4d87-90f0-ad94e7239b06

- **Infrastructure Provisioning**: Terraform is used to provision an EKS cluster with two worker nodes.

- **Application Deployment**: Helm charts are used to manage the deployment of various Kubernetes resources such as Service Accounts, Namespaces, Network Policies, PodSecurityPolicies, and applications like the ELK stack. This ensures consistent, version-controlled application deployments.

- **Testing**: Python unit tests are written for auditing and remediation scripts. The audit script checks for RBAC permissions, insecure container images, and exposed services. The remediation script provides warnings and errors for sysadmins to correct these configurations.

- **Continuous Integration/Continuous Deployment (CI/CD)**: Jenkins is employed as the CI/CD tool to automate the building, testing, and deployment of the infrastructure and applications. Jenkins pipelines are used for end-to-end automation.

## Infrastructure Provisioning
Terraform is used to define and provision the AWS resources for the EKS cluster and worker nodes. This includes defining VPC configurations, IAM roles, and security groups. Make sure you have the AWS CLI configured with appropriate credentials and Terraform installed. Here are the basic steps:

1. Navigate to the `terraform` directory.
2. Run `terraform init` to initialize the Terraform working directory.
3. Run `terraform apply` to create the infrastructure.
4. After provisioning, run `terraform output` to get the cluster configuration details.

## Install and Conigure Kubect

```shell
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
``` 


## Establish connection to EKS Cluster

```shell
aws eks --region <your-region> update-kubeconfig --name <cluste-name>
kubectl config get-contexts
kubectl config use-context <context-name>
kubectl config current-context
kubectl cluster-info
``` 

## Application Deployment
Helm charts are used for Kubernetes application deployments. The Helm charts for your applications, including the ELK stack, are stored in a directory structure. Follow these steps to deploy applications:

## Install & Configure Helm Chart

```shell
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm -y
``` 

1. Navigate to the `helm-charts` directory.
2. Deploy a Helm chart using the `helm install` command, e.g., `helm install my-elk-stack ./elk-stack`. Customize chart values as needed.

## Testing
Python unit tests are available for auditing and remediation scripts. You can run these tests locally or integrate them into your CI/CD pipeline. To run the tests:

1. Navigate to the `python_script` directory.
2. Setup Python Environment using the below commands

```shell
sudo apt update
sudo apt install python3-venv
mkdir ~/myenv
python3 -m venv ~/myenv
source ~/myenv/bin/activate
pip install kubernetes requests
``` 


3. Run the unit test, e.g., `python3 -m unittest <test_script.py>`.
4. Run the audit script, e.g., `python3 -m unittest <audit_script.py>`.
5. Run the unit script, e.g., `python3 -m unittest <remediation_script.py>`.

## Continuous Integration/Continuous Deployment (CI/CD)
Jenkins is used for automating CI/CD pipelines. Jenkins pipelines are defined to automate tasks such as provisioning infrastructure, deploying applications, and running tests. Here are the key steps:

1. Set up a Jenkins server and configure it to work with your source code repository.
2. Define Jenkins pipeline stages for your project, including infrastructure provisioning, application deployment, and testing.
3. Configure Jenkins pipeline triggers, such as webhook integrations with your source code repository.
4. Monitor pipeline runs and review build/test logs and deployment status.

## Usage
This project can be used as a template for deploying Kubernetes applications on EKS while ensuring security and compliance. Customize the Terraform configurations, Helm charts, and Python scripts to meet your specific application and security requirements.

## Contributing
Contributions to this project are welcome! If you have ideas for improvements or find issues, please open a GitHub issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.