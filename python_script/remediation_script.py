# import logging
# from kubernetes import client, config
# import time

# # Configure logging
# logging.basicConfig(filename='remediation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# def remediate_insecure_images():
#     config.load_kube_config("~/.kube/config")
#     v1 = client.CoreV1Api()

#     all_pods = v1.list_pod_for_all_namespaces().items
#     for pod in all_pods:
#         for container in pod.spec.containers:
#             image = container.image
#             if image.startswith("insecure/"):
#                 # Implement remediation steps for insecure image usage (e.g., pulling a patched image)
#                 patched_image = "secured/image:latest"
#                 container.image = patched_image
#                 container.image_pull_policy = "Always"
#                 try:
#                     v1.replace_namespaced_pod(name=pod.metadata.name, namespace=pod.metadata.namespace, body=pod)
#                     logging.info(f"Remediated insecure image for Pod '{pod.metadata.name}'")
#                 except client.rest.ApiException as e:
#                     logging.error(f"Failed to remediate insecure image for Pod '{pod.metadata.name}': {e}")

# def remediate_exposed_services():
#     config.load_kube_config("~/.kube/config")
#     v1 = client.CoreV1Api()

#     services = v1.list_service_for_all_namespaces().items
#     for service in services:
#         if service.spec.type == "LoadBalancer":
#             if service.status.load_balancer.ingress:
#                 # Implement remediation steps for exposed services (e.g., change service type to ClusterIP)
#                 service.spec.type = "ClusterIP"
#                 try:
#                     v1.replace_namespaced_service(name=service.metadata.name, namespace=service.metadata.namespace, body=service)
#                     logging.info(f"Remediated exposed service '{service.metadata.name}'")
#                 except client.rest.ApiException as e:
#                     logging.error(f"Failed to remediate exposed service '{service.metadata.name}': {e}")

# def remediate_rbac():
#     config.load_kube_config("~/.kube/config")
#     rbac_v1 = client.RbacAuthorizationV1Api()

#     cluster_roles = rbac_v1.list_cluster_role().items
#     for cluster_role in cluster_roles:
#         if cluster_role.rules is not None:  # Check if rules is not None
#             for rule in cluster_role.rules:
#                 if rule.resources or rule.verbs:
#                     # Implement remediation steps for RBAC issues (e.g., remove unnecessary permissions)
#                     cluster_role.rules = []

#                     # Retry logic to handle conflicts
#                     retries = 3
#                     while retries > 0:
#                         try:
#                             rbac_v1.replace_cluster_role(name=cluster_role.metadata.name, body=cluster_role)
#                             logging.info(f"Remediated RBAC ClusterRole '{cluster_role.metadata.name}'")
#                             break  # Exit the loop if the update succeeds
#                         except client.rest.ApiException as e:
#                             if e.status == 409:  # Conflict
#                                 retries -= 1
#                                 time.sleep(1)  # Wait for a short time before retrying
#                             else:
#                                 logging.error(f"Failed to remediate RBAC ClusterRole '{cluster_role.metadata.name}': {e}")
#                                 raise  # Re-raise other exceptions


# if __name__ == "__main__":
#     logging.info("Remediation script started.")
#     remediate_insecure_images()
#     remediate_exposed_services()
#     remediate_rbac()
#     logging.info("Remediation script completed.")


# import logging
# from kubernetes import client, config
# import time

# # Configure logging
# logging.basicConfig(filename='remediation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# def remediate_insecure_images():
#     config.load_kube_config("~/.kube/config")
#     v1 = client.CoreV1Api()

#     all_pods = v1.list_pod_for_all_namespaces().items
#     for pod in all_pods:
#         for container in pod.spec.containers:
#             image = container.image
#             if image.startswith("insecure/"):
#                 # Implement remediation steps for insecure image usage (e.g., pulling a patched image)
#                 patched_image = "secured/image:latest"
#                 container.image = patched_image
#                 container.image_pull_policy = "Always"
#                 try:
#                     v1.replace_namespaced_pod(name=pod.metadata.name, namespace=pod.metadata.namespace, body=pod)
#                     logging.info(f"Remediated insecure image for Pod '{pod.metadata.name}'")
#                 except client.rest.ApiException as e:
#                     logging.error(f"Failed to remediate insecure image for Pod '{pod.metadata.name}': {e}")

# def remediate_exposed_services():
#     config.load_kube_config("~/.kube/config")
#     v1 = client.CoreV1Api()

#     services = v1.list_service_for_all_namespaces().items
#     for service in services:
#         if service.spec.type == "LoadBalancer":
#             if service.status.ingress:
#                 # Implement remediation steps for exposed services (e.g., change service type to ClusterIP)
#                 service.spec.type = "ClusterIP"
#                 try:
#                     v1.replace_namespaced_service(name=service.metadata.name, namespace=service.metadata.namespace, body=service)
#                     logging.info(f"Remediated exposed service '{service.metadata.name}'")
#                 except client.rest.ApiException as e:
#                     logging.error(f"Failed to remediate exposed service '{service.metadata.name}': {e}")

# def remediate_rbac():
#     config.load_kube_config("~/.kube/config")
#     rbac_v1 = client.RbacAuthorizationV1Api()

#     cluster_roles = rbac_v1.list_cluster_role().items
#     for cluster_role in cluster_roles:
#         if cluster_role.rules is not None:  # Check if rules is not None
#             for rule in cluster_role.rules:
#                 if rule.resources or rule.verbs:
#                     # Implement remediation steps for RBAC issues (e.g., remove unnecessary permissions)
#                     cluster_role.rules = []

#                     # Retry logic to handle conflicts
#                     retries = 3
#                     while retries > 0:
#                         try:
#                             rbac_v1.replace_cluster_role(name=cluster_role.metadata.name, body=cluster_role)
#                             logging.info(f"Remediated RBAC ClusterRole '{cluster_role.metadata.name}'")
#                             break  # Exit the loop if the update succeeds
#                         except client.rest.ApiException as e:
#                             if e.status == 409:  # Conflict
#                                 retries -= 1
#                                 time.sleep(1)  # Wait for a short time before retrying
#                             else:
#                                 logging.error(f"Failed to remediate RBAC ClusterRole '{cluster_role.metadata.name}': {e}")
#                                 raise  # Re-raise other exceptions


# if __name__ == "__main__":
#     logging.info("Remediation script started.")
#     remediate_insecure_images()
#     remediate_exposed_services()
#     remediate_rbac()
#     logging.info("Remediation script completed.")

import logging
from kubernetes import client, config
import time

# Configure logging
logging.basicConfig(filename='remediation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def remediate_insecure_images():
    kubeconfig_path = "~/.kube/config"  # Replace with the actual path to your kubeconfig
    config.load_kube_config(config_file=kubeconfig_path)
    v1 = client.CoreV1Api()

    all_pods = v1.list_pod_for_all_namespaces().items
    for pod in all_pods:
        for container in pod.spec.containers:
            image = container.image
            if image.startswith("insecure/"):
                # Implement remediation steps for insecure image usage (e.g., pulling a patched image)
                patched_image = "secured/image:latest"
                container.image = patched_image
                container.image_pull_policy = "Always"
                try:
                    v1.replace_namespaced_pod(name=pod.metadata.name, namespace=pod.metadata.namespace, body=pod)
                    logging.info(f"Remediated insecure image for Pod '{pod.metadata.name}'")
                except client.rest.ApiException as e:
                    logging.error(f"Failed to remediate insecure image for Pod '{pod.metadata.name}': {e}")

def remediate_exposed_services():
    kubeconfig_path = "~/.kube/config"  # Replace with the actual path to your kubeconfig
    config.load_kube_config(config_file=kubeconfig_path)
    v1 = client.CoreV1Api()

    services = v1.list_service_for_all_namespaces().items
    for service in services:
        if service.spec.type == "LoadBalancer":
            if service.status.load_balancer.ingress:
                # Implement remediation steps for exposed services (e.g., change service type to ClusterIP)
                service.spec.type = "ClusterIP"
                try:
                    v1.replace_namespaced_service(name=service.metadata.name, namespace=service.metadata.namespace, body=service)
                    logging.info(f"Remediated exposed service '{service.metadata.name}'")
                except client.rest.ApiException as e:
                    logging.error(f"Failed to remediate exposed service '{service.metadata.name}': {e}")

def remediate_rbac():
    kubeconfig_path = "~/.kube/config" # Replace with the actual path to your kubeconfig
    config.load_kube_config(config_file=kubeconfig_path)
    rbac_v1 = client.RbacAuthorizationV1Api()

    cluster_roles = rbac_v1.list_cluster_role().items
    for cluster_role in cluster_roles:
        if cluster_role.rules is not None:  # Check if rules is not None
            for rule in cluster_role.rules:
                if rule.resources or rule.verbs:
                    # Implement remediation steps for RBAC issues (e.g., remove unnecessary permissions)
                    cluster_role.rules = []

                    # Retry logic to handle conflicts
                    retries = 3
                    while retries > 0:
                        try:
                            rbac_v1.replace_cluster_role(name=cluster_role.metadata.name, body=cluster_role)
                            logging.info(f"Remediated RBAC ClusterRole '{cluster_role.metadata.name}'")
                            break  # Exit the loop if the update succeeds
                        except client.rest.ApiException as e:
                            if e.status == 409:  # Conflict
                                retries -= 1
                                time.sleep(1)  # Wait for a short time before retrying
                            else:
                                logging.error(f"Failed to remediate RBAC ClusterRole '{cluster_role.metadata.name}': {e}")
                                raise  # Re-raise other exceptions

if __name__ == "__main__":
    logging.info("Remediation script started.")
    remediate_insecure_images()
    remediate_exposed_services()
    remediate_rbac()
    logging.info("Remediation script completed.")
