import psutil

nic_info = psutil.net_if_addrs()
for interface, address in nic_info.items():
    print(f"인터페이스: {interface}")
    for addr in address:
        print(f" - {addr.family.name}, {addr.address}")
