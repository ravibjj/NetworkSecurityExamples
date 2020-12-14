#!/usr/bin/env python3
# ****** Ravi Nori
# ****** 12/15/2020
# ****** Purpose : script will check to see if the machine is being arp spoofed
import os
import datetime


def extraction():
    arp_table = os.popen("arp -a").read()
    arp_lines = arp_table.splitlines()
    addresses = {}
    for line in range(len(arp_lines)):
        arp_line = arp_lines[line]
        print(arp_line)
        if "ff-ff-ff-ff-ff-ff" or "ff:ff:ff:ff:ff:ff" in arp_line:
            pass
        else:
            if "." not in arp_line:
                break
            ip, mac, _type = arp_line.split()
            print(ip, mac, _type)
            addresses[ip] = mac
            print(addresses.values(), addresses.keys())
    return addresses


# code to check for MAC address duplication
def check_duplication(addresses_dict):
    for ip in addresses_dict:
        mac = addresses_dict[ip]
        addresses_dict[ip] = "00-00-00-00-00-00"
        if mac in addresses_dict.values():
            # calling the log creator function to send the finding
            create_log("Arp spoofed\nDuplicated address = {}".format(mac))


def create_log(message):
    date = datetime.now()
    with open("log.txt", "a") as log:
        log.write(message + "\nDate: {}\n\n".format(date))


def main():
    extraction()

if __name__ == '__main__':
    main()
