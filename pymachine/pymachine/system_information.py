import platform
import wmi


# return the system information
def get_system_info_dict():
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]
    """Return the system information."""
    return {
        'platform': platform.platform(),
        'system': platform.system(),
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'manufacturer': my_system.Manufacturer,
        'modal': my_system.Model,
        'name': my_system.Name,
        'NumberOfProcessors': my_system.NumberOfProcessors,
        'systemType': my_system.SystemType,
        'systemFamily': my_system.SystemFamily
    }


info = get_system_info_dict()

for k, v in info.items():
    print(f"{k}: {v}")
