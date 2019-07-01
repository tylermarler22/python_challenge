import re
def search(fileName):
    ips = []
    file = open(fileName,"r")
    for line in file:
        addresses = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)
        for address in addresses:
            ips.append(address)
    file.close()
    return ips