from service.resource_groups.connector import ResourceGroupsConnector


def collect_resource_groups():
    resource_groups_connector = ResourceGroupsConnector()
    resource_groups_list = resource_groups_connector.get_resource_groups_list()

    column_width = 40
    print("Resource Group".ljust(column_width) + "Location")
    print("-" * (column_width * 2))

    for resource_group in list(resource_groups_list):
        print(f"{resource_group.name:<{column_width}}{resource_group.location}")
