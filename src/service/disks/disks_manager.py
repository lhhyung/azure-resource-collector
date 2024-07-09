from service.disks.connector import DisksConnector


def collect_disks():
    disks_connector = DisksConnector()
    disks_list = disks_connector.get_disks_list()

    for disk in disks_list:
        print(disk)
