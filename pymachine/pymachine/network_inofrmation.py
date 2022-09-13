import subprocess

network = subprocess.check_output(['ipconfig', '/all']).decode('utf-8').split('\n')

new = []

# arrange the string into clear info
for item in network:
    new.append(str(item.split("\r")[:-1]))
for i in new:
    print(i[2:-2])
