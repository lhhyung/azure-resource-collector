from service.virtual_machines.connector import VirtualMachinesConnector


def collect_virtual_machines():
    virtual_machines_connector = VirtualMachinesConnector()
    virtual_machines_list = virtual_machines_connector.get_virtual_machines_list()

    column_width = 40
    print("virtual_machines_list")
    print("-" * (column_width * 2))

    for virtual_machine in virtual_machines_list:
        print(virtual_machine)

    print()
