#pip3 install scapy

import scapy.all as scapy
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP or Range")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("Please specify an target. Please use --help for more information.")
    return options


def scan(ip):
    apr_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/apr_req
    answered = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

    clients = []
    for i in answered:
        client_dict = {"ip": i[1].psrc, "mac": i[1].hwsrc}
        clients.append(client_dict)
    return clients


def print_res(results):
    print("IP\t\t\tMAC Address\n---------------------------------------")
    for client in results:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_args()
print_res(scan(options.target))
