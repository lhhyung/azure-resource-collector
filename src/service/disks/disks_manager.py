from service.disks.connector import DisksConnector


def collect_disks():
    disks_connector = DisksConnector()
    disks_list = disks_connector.get_disks_list()

    column_width = 40

    print("disks_list")
    print("Name".ljust(column_width) + "Storage Type".ljust(column_width) + "Size(GB)".ljust(
        column_width) + "Owner".ljust(column_width) + "Resource Group".ljust(column_width) + "Location".ljust(
        column_width))
    print("-" * (column_width * 6))

    for disk in disks_list:
        name = disk.name[:column_width].ljust(column_width)
        storage_type = disk.sku.name.ljust(column_width)
        size_gb = str(disk.disk_size_gb).ljust(column_width)
        owner = disk.managed_by.split('/')[-1].ljust(column_width)
        resource_group = disk.id.split('/')[4].ljust(column_width)
        location = disk.location.ljust(column_width)

        print(name + storage_type + size_gb + owner + resource_group + location)

    print()