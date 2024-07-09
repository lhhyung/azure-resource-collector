from libs.connector import AzureSdkConnector


class DisksConnector(AzureSdkConnector):
    def __init__(self):
        super().__init__()

    def get_disks_list(self):
        return self.compute_client.disks.list()