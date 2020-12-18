# Simple Port Scanner
# Ravi Nori
# 12/20/2020
# Usage : iterates over a range of hosts and pings to see if host is up
# Example: automated ping over a series of  hosts (Class C)

import platform  # For getting the operating system name
import subprocess  # For executing a shell command


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0
