from service.virtual_machines.connector import VirtualMachinesConnector


def collect_virtual_machines():
    virtual_machines_connector = VirtualMachinesConnector()
    virtual_machines_list = virtual_machines_connector.get_virtual_machines_list()

    column_width = 40

    print("virtual_machines_list")
    print("Name".ljust(column_width) + "Subscription".ljust(column_width) + "Resource Group".ljust(column_width) + "Location".ljust(column_width))
    print("-" * (column_width * 4))

    for vm in virtual_machines_list:
        vm_name = vm.name
        subscription_id = vm.id.split('/')[2]
        resource_group = vm.id.split('/')[4]
        location = vm.location

        print(
            f"{vm_name:<{column_width}}{subscription_id:<{column_width}}{resource_group:<{column_width}}{location:<{column_width}}")

    print()

