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

        stage('Terraform Apply') {
            steps {
                sh '''
                    cd ./Infrastructure
                    terraform apply --auto-approve'''
            }
        }

        // stage('Terraform Destroy') {
        //     steps {
        //         sh '''
        //             cd ./Infrastructure
        //             terraform destroy --auto-approve'''
        //     }
        // }

        stage('Configure kubectl') {
            steps {
                sh 'aws eks update-kubeconfig --region us-west-2 --name dev_cluster'
            }
        }

        stage('Establish Connection With EKS') {
            steps {
                script {
                    def eksContext = sh(returnStdout: true, script: 'kubectl config get-contexts --output name | grep dev_cluster').trim()
                    sh """
                        aws eks --region us-west-2 update-kubeconfig --name dev_cluster
                        kubectl config get-contexts
                        kubectl config use-context ${eksContext}
                        kubectl config current-context
                        kubectl cluster-info
                        kubectl get nodes -n dev-namespace
                        kubectl get pods -n dev-namespace
                        kubectl get svc -n dev-namespace
                    """
                }
            }
        }

        stage('Deploy Helm Chart') {
            steps {
                sh '''
                    helm ls -a
                    helm upgrade --install k8-helm k8-helm'''
            }
        }

        // stage('Setup Python Environment') {
        //     steps {
        //         script {
        //             // Define the Python version and environment name
        //             def pythonVersion = '3.8.12'
        //             def venvName = 'myenv'
        //             // Use the withPythonEnv step to manage the Python environment
        //             withPythonEnv([pyenvRoot: tool(name: 'Pyenv', type: 'hudson.plugins.pyenv.PyenvInstallation')]) {
        //                 // Activate the virtual environment and set the Python version
        //                 sh "pyenv global ${pythonVersion}"
        //                 sh "python --version"
        //                 sh "python -m venv ${venvName}"
        //                 sh "source ${venvName}/bin/activate"
        //                 sh "pip install kubernetes requests"
        //             }
        //         }
        //     }
        // }

        // stage('Setup Python Environment') {
        //     steps {
        //         pyenv('myenv') {
        //             sh 'python --version'
        //             sh 'pip install kubernetes requests'
        //              }
        //     }
        // }
    //  stage('Setup Python Environment') {
    //      steps {
    //          sh '''
    //             su - ubuntu -c "sudo apt update && sudo apt install -y python3-venv"
    //             su - ubuntu -c "python3 -m venv myenv && source myenv/bin/activate"
    //          '''
    //      }
    //  }

        // stage('Setup Python Environment') {
        //     steps {
        //         sh '''
                //         export SUDO_ASKPASS=/usr/local/bin/askpass.sh
                // sudo -A apt install -y python3-venv
                    // apt install -y python3-venv
                        // python3 -m venv myenv
        //             apt install python3-venv -y
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

    }
}
