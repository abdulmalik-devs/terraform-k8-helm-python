import logging
from kubernetes import client, config

# Configure logging
logging.basicConfig(filename='audit.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def check_rbac():
    config.load_kube_config("~/.kube/config")
    rbac_api = client.RbacAuthorizationV1Api()
    cluster_roles = rbac_api.list_cluster_role().items
    for cluster_role in cluster_roles:
        if cluster_role.rules is not None:  # Check if rules is not None
            for rule in cluster_role.rules:
                if rule.resources or rule.verbs:
                    logging.info(f"ClusterRole '{cluster_role.metadata.name}' allows resource access.")

def check_insecure_images():
    config.load_kube_config("~/.kube/config")
    v1 = client.CoreV1Api()
    all_pods = v1.list_pod_for_all_namespaces().items
    for pod in all_pods:
        for container in pod.spec.containers:
            image = container.image
            if image.startswith("insecure/"):
                logging.info(f"Pod '{pod.metadata.name}' has insecure image '{image}'.")

def check_exposed_services():
    config.load_kube_config("~/.kube/config")
    v1 = client.CoreV1Api()
    services = v1.list_service_for_all_namespaces().items
    for service in services:
        if service.spec.type == "LoadBalancer":
            if service.status.load_balancer.ingress:
                logging.info(f"Service '{service.metadata.name}' is exposed externally.")

if __name__ == "__main__":
    logging.info("Audit script started.")
    check_rbac()
    check_insecure_images()
    check_exposed_services()
    logging.info("Audit script completed.")
