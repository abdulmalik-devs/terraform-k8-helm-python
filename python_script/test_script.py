import unittest
from unittest.mock import patch, MagicMock
from audit_script import check_rbac, check_insecure_images, check_exposed_services
from remediation_script import remediate_insecure_images, remediate_exposed_services, remediate_rbac
import logging  # Import the 'logging' module
import warnings

warnings.filterwarnings("ignore")

class TestAuditScript(unittest.TestCase):

    @patch("kubernetes.client.RbacAuthorizationV1Api")
    @patch("logging.info")  # Patch the logging.info function
    def test_check_rbac(self, mock_log, mock_rbac_api):
        mock_cluster_role = MagicMock()
        mock_cluster_role.metadata.name = "test-role"
        mock_rule = MagicMock()
        mock_rule.resources = ["pods"]
        mock_cluster_role.rules = [mock_rule]
        mock_rbac_api.return_value.list_cluster_role.return_value.items = [mock_cluster_role]

        # Call the function
        check_rbac()

        # Assert that the expected message is printed
        expected_output = "ClusterRole 'test-role' allows resource access."
        mock_log.assert_called_with(expected_output)

    @patch("kubernetes.client.CoreV1Api")
    @patch("logging.info")  # Patch the logging.info function
    def test_check_insecure_images(self, mock_log, mock_v1):
        mock_pod = MagicMock()
        mock_pod.metadata.name = "test-pod"
        mock_container = MagicMock()
        mock_container.image = "insecure/image"
        mock_pod.spec.containers = [mock_container]
        mock_v1.return_value.list_pod_for_all_namespaces.return_value.items = [mock_pod]

        # Call the function
        check_insecure_images()

        # Assert that the expected message is printed
        expected_output = "Pod 'test-pod' has insecure image 'insecure/image'."
        mock_log.assert_called_with(expected_output)

    @patch("kubernetes.client.CoreV1Api")
    @patch("logging.info")  # Patch the logging.info function
    def test_check_exposed_services(self, mock_log, mock_v1):
        mock_service = MagicMock()
        mock_service.metadata.name = "test-service"
        mock_service.spec.type = "LoadBalancer"
        mock_service.status.load_balancer.ingress = ["1.2.3.4"]
        mock_v1.return_value.list_service_for_all_namespaces.return_value.items = [mock_service]

        # Call the function
        check_exposed_services()

        # Assert that the expected message is printed
        expected_output = "Service 'test-service' is exposed externally."
        mock_log.assert_called_with(expected_output)

class TestRemediationScript(unittest.TestCase):

    @patch("kubernetes.client.CoreV1Api")
    @patch("logging.info")  # Patch the logging.info function
    def test_remediate_insecure_images(self, mock_log, mock_v1):
        mock_pod = MagicMock()
        mock_pod.metadata.name = "test-pod"
        mock_container = MagicMock()
        mock_container.image = "insecure/image"
        mock_pod.spec.containers = [mock_container]
        mock_v1.return_value.list_pod_for_all_namespaces.return_value.items = [mock_pod]

        # Call the function
        remediate_insecure_images()

        # Assert that the container image is updated
        expected_image = "secured/image:latest"
        self.assertEqual(expected_image, mock_container.image)

    @patch("kubernetes.client.CoreV1Api")
    @patch("logging.info")  # Patch the logging.info function
    def test_remediate_exposed_services(self, mock_log, mock_v1):
        mock_service = MagicMock()
        mock_service.metadata.name = "test-service"
        mock_service.spec.type = "LoadBalancer"
        mock_service.status.load_balancer.ingress = ["1.2.3.4"]
        mock_v1.return_value.list_service_for_all_namespaces.return_value.items = [mock_service]

        # Call the function
        remediate_exposed_services()

        # Assert that the service type is updated
        expected_type = "ClusterIP"
        self.assertEqual(expected_type, mock_service.spec.type)

    @patch("kubernetes.client.RbacAuthorizationV1Api")
    @patch("logging.info")  # Patch the logging.info function
    def test_remediate_rbac(self, mock_log, mock_rbac_api):
        mock_cluster_role = MagicMock()
        mock_cluster_role.metadata.name = "test-role"
        mock_rule = MagicMock()
        mock_rule.resources = ["pods"]
        mock_cluster_role.rules = [mock_rule]
        mock_rbac_api.return_value.list_cluster_role.return_value.items = [mock_cluster_role]

        # Call the function
        remediate_rbac()

        # Assert that the cluster role rules are empty
        self.assertEqual([], mock_cluster_role.rules)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    result = runner.run(unittest.makeSuite(TestAuditScript))
    if result.wasSuccessful():
        print("All tests in TestAuditScript passed successfully.")

    result = runner.run(unittest.makeSuite(TestRemediationScript))
    if result.wasSuccessful():
        print("All tests in TestRemediationScript passed successfully.")

warnings.resetwarnings()

