from service.disks.connector import DisksConnector


def collect_disks():
    disks_connector = DisksConnector()
    disks_list = disks_connector.get_disks_list()

    column_width = 40
    print("disks_list")
    print("-" * (column_width * 2))

    for disk in disks_list:
        print(disk)

    print()
