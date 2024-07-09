import os
from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient


class AzureSdkConnector:
    def __init__(self):
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', '.env')
        load_dotenv(env_path)
        subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')

        credential = DefaultAzureCredential()

        self.compute_client = ComputeManagementClient(
            credential=credential, subscription_id=subscription_id
        )

        self.resource_client = ResourceManagementClient(
            credential=credential, subscription_id=subscription_id
        )
