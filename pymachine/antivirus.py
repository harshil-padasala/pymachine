import windows_tools.antivirus as antivirus

result = antivirus.get_installed_antivirus_software()

info = []
antivirus = {}
for item in result:
    info.append(item)

for item in info:
    item_name = item['name']
    antivirus[item_name] = item

# print(antivirus)

antivirus_info = {'antivirus': antivirus}
print(antivirus_info)
