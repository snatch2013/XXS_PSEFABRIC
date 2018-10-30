import ipaddress

def cidr_to_netmask(cidr):
    ip = ipaddress.ip_network(cidr)
    return str(ip.network_address), str(ip.netmask), str(ip.network_address + 1)
