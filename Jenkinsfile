pipeline {
    agent any
    
    environment {
        EKS_CLUSTER_NAME = "dev_cluster"
        AWS_DEFAULT_REGION = 'us-west-2'
    }
    
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        
        stage('Checkout from Git') {
            steps {
                git branch: 'main', url: 'https://github.com/abdulmalik-devs/terraform-k8-helm-python.git'
            }
        }

        stage('Terraform Init') {
            steps {
                sh '''
                    cd ./Infrastructure
                    terraform init -reconfigure'''
            }
        }

        stage('Terraform Plan') {
            steps {
                sh '''
                    cd ./Infrastructure
                    terraform plan'''
            }
        }

        // stage('Provision EKS Cluster') {
        //     steps {
        //         withAWS(credentials: 'AWS_Credentials', region: AWS_DEFAULT_REGION) {
        //             sh '''
        //                 cd ./Infrastructure
        //                 terraform init
        //                 terraform apply -auto-approve
        //             '''
        //         }
        //     }
        // }

        // stage('Configure kubectl') {
        //     steps {
        //         sh 'aws eks update-kubeconfig --region us-west-2 --name $EKS_CLUSTER_NAME'
        //     }
        // }


        // stage('Deploy Helm Chart') {
        //     steps {
        //         sh 'helm upgrade --install k8-helm ./python_script/k8-helm'
        //     }
        // }

        // stage('Setup Python Environment') {
        //     steps {
        //         sh '''
        //             sudo apt update
        //             sudo apt install python3-venv -y
        //             mkdir ~/myenv
        //             python3 -m venv ~/myenv
        //             source ~/myenv/bin/activate
        //         '''
        //     }
        // }

        // stage('Install Python Dependencies') {
        //     steps {

        //         sh 'pip install kubernetes requests'

        //     }
        // }

        // stage('Static Code Analysis') {
        //     steps {
        //         sh 'pylint tests/unit/*.py'
        //         sh 'pylint tests/audit/*.py'
        //         sh 'pylint tests/remediation/*.py'
        //     }
        // }


        // stage('Run Python Unit Test') {
        //     steps {
        //         sh 'python -m unittest discover -s ./python_script -p "test_script.py"'
        //     }
        // }

        // stage('Run Python Audit Test') {
        //     steps {
        //         sh 'python -m unittest discover -s ./python_script -p "audit_script.py"'
        //     }
        // }

        
        // stage('Run Python Remediation Test') {
        //     steps {
        //         sh 'python -m unittest discover -s ./python_script-p "remediation_script.py"'
        //     }
        // }


        // stage('Artifact Management') {
        //     steps {
        //         sh 'aws s3 cp python_script/audit.log s3://your-bucket-name'
        //         sh 'aws s3 cp python_script/remediation.log s3://your-bucket-name'
        //     }
        // }


        // stage('Notifications') {
        //     steps {
        //         slackSend channel: '#your-channel', message: 'Pipeline completed successfully!', tokenCredentialId: 'your-credential-id'
        //     }
        // }
    }
}
