import platform
import wmi


# return the system information
def get_system_info_dict():
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]
    """Return the system information."""
    return {
        'system': {
            'system_name': platform.system(),
            'node': platform.node(),
            'system_version': platform.version(),
            'processor': platform.processor(),
            'system_type': my_system.SystemType,
        }
    }


info = get_system_info_dict()

for k, v in info.items():
    print(f"{k}: {v}")