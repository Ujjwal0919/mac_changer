import subprocess
import random as r
import re
from get_nic import getnic
import optparse


# __________________________________________________________________________________________________-
#  [+][+][+][+][+] Function to change the mac address  [+][+][+][+][+]
def mac_changer(interface1, new_mac1):
    print("[+] Changing Mac Address of interface " + interface1 + "to " + new_mac1)
    subprocess.call(["ifconfig", interface1, "down"])
    subprocess.call(["ifconfig", interface1, "hw", "ether", new_mac1])
    subprocess.call(["ifconfig", interface1, "up"])


# _________________________________________________________________________________________________
def random_mac():
    bytes = []
    l1 = []
    for i in range(10):
        l1.append(str(i))
    l2 = ['A', 'B', 'C', 'D', 'E', 'F']
    l1.extend(l2)
    # randomly generating 12 digits for mac address
    for i in range(12):
        bytes.append(l1[r.randint(0, 15)])
    # joining 2 continuous bytes
    l2 = []
    for i in range(0, 11, 2):
        l2.append(bytes[i] + bytes[i + 1])
    # joining all the parts of mac address
    rand_mac = ':'.join(l2)
    return rand_mac


# ___________________________________________________________________________________________________________________

def input_function():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Enter the interface to change its mac value")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter the new mac address for the interface ")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please make sure that you enter the interface use --help for info"
                     )
        exit()
    interface = options.interface
    # checking if the entered interface is available or not
    sys_interfaces = getnic.interfaces()
    flag = 0
    for i in sys_interfaces:
        if i == interface:
            flag = 1
            break;
    if flag == 0:
        print("Entered interface is not available")
        sys.exit()
    # _______________________________________________________________________________________________

    #       takes mac address as a input and check for iif it is correct mac address or not
    if options.new_mac:
        new_mac = options.new_mac
        mac_flag = 0
        chars = new_mac.split(':')
        # if number of colons are not correct
        if len(chars) != 6:
            mac_flag = 1

        # to store all the decimal values for hexadecimal parts of mac address
        l1 = []
        for i in chars:
            try:
                l1.append(int(i, 16))
            except:
                mac_flag = 1
        for i in l1:
            if i > 255 or i < 0:
                mac_flag = 1
        if mac_flag == 1:
            print("Entered mac in not in correct format")
            exit()
    else:
        try:
            new_mac = random_mac()
        except:
            print("Error in changing mac address please try again")

    mac_changer(interface, new_mac)


# __________________________________________________________________________________________________

input_function()
