from libs.connector import AzureSdkConnector


class ResourceGroupsConnector(AzureSdkConnector):
    def __init__(self):
        super().__init__()

    def get_resource_groups_list(self):
        return self.resource_client.resource_groups.list()
