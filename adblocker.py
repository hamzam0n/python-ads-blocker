import sys
import requests
import platform
import colorama
from colorama import Fore, Style


def howToUse():
	print()
	print("	python3  adblocker.py <option>")
	print(Fore.BLUE + "		option: ")
	print(Style.RESET_ALL+"			[+] block => To block ads")
	print("			[+] unblock => To unblock ads")
	print(Fore.RED + "		ex: ")
	print(Style.RESET_ALL+"				 sudo python3  adblocker.py block")
	print("				 sudo python3  adblocker.py unblock")
	print(Fore.YELLOW +"\n","	PS: You need to run this code as *root* or *administrator* to run it successfully","\n"+Style.RESET_ALL)
	print()

host_path=""
default_windows = """# Copyright (c) 1993-2009 Microsoft Corp. 
# 
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should\n
# be placed in the first column followed by the corresponding host name.\n
# The IP address and the host name should be separated by at least one\n
# space.\n
#
# Additionally, comments (such as these) may be inserted on individual\n
# lines or following the machine name denoted by a '#' symbol.\n
#\n
# For example:\n
#
#      102.54.94.97     rhino.acme.com          # source server\n
#       38.25.63.10     x.acme.com              # x client host\n
\n
# localhost name resolution is handled within DNS itself.\n
#	127.0.0.1       localhost\n
#	::1             localhost\n
										"""

default_linux= """127.0.0.1	localhost 
127.0.1.1	mail.hamzam0n.com 


# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
"""

if len(sys.argv) != 2 : 
	howToUse()
	exit()
if not sys.argv[1].lower()   in("block","unblock"):
	howToUse()
	exit()

URL = "https://pgl.yoyo.org/as/serverlist.php?showintro=1&mimetype=plaintext"
page = requests.get(URL)
if "linux" in platform.platform().lower():
	host_path = "/etc/hosts"
	default = default_linux

elif "windows" in platform.platform().lower():
	host_path = r"c:\windows\system32\drivers\etc\hosts"
	default = default_windows


if sys.argv[1].lower() == "block" :
	file_content = default+str(page.content).replace("\\n"," \n")
	message = "   [+] Ads Are Blocked Now"
elif sys.argv[1].lower() == "unblock" :
	file_content = default
	message = "   [+] Ads Are Unblocked Now"
else :
	howToUse()
	exit()

try : 
	file = open(host_path, 'w+')
	file.write(file_content)
	file.close()
	print(Fore.YELLOW +"\n",message,"\n")
except : 
	print(Fore.YELLOW +"\n","	[+] You need to run this code as *root* or *administrator* to run it successfully","\n"+Style.RESET_ALL)


