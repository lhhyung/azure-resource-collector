from libs.connector import AzureSdkConnector


class VirtualMachinesConnector(AzureSdkConnector):
    def __init__(self):
        super().__init__()

    def get_virtual_machines_list(self):
        return self.compute_client.virtual_machines.list_all()

    # def get_virtual_machines_statuses(self, resource_group, vm_name):
    #     return self.compute_client.virtual_machines.instance_view(resource_group, vm_name).statuses
