#!/usr/bin python
# -*- coding: utf-8 -*-
#thenurhabib

from logging import exception
import os
import sys

# Tool Information
__Name__ = "fstScan"
__Discription__ = "Massive Vulnerability scanner"
__Author__ = "Md. Nur habib"
__Version__ = "1.0"

#  Style
reset='\033[0m'
bold='\033[01m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
cyan='\033[36m'
yellow='\033[93m'


# print Banner
print(f"""{bold}{yellow}
    ____     __  _____                
   / __/____/ /_/ ___/_________ _____ 
  / /_/ ___/ __/\__ \/ ___/ __ `/ __ \\ {__Version__}
 / __(__  ) /_ ___/ / /__/ /_/ / / / / 
/_/ /____/\__//____/\___/\__,_/_/ /_/ {red}
                        @thenurhabib{reset}
""")

# Main Function
def fullVulnerabilityScan():
    try:
        print(f"\n{bold}{blue}")
        domainName = input(f"[-] Enter Domain Name : {reset}{cyan}")
        print("")

        #NMAP
        print(f"{bold}{blue}Start Network Scanning {red}(Please it takes some time){reset} \n")
        os.system(f"nmap -A {domainName}")
        print("")
        print("")

        #SQLMAP
        print(f"{blue}{bold}Crawling every URL and find SQL Vulnerability.\n{reset}")
        os.system(f"sqlmap -u {domainName} --a --batch ")
        print("")

        #nikto
        print(f"{blue}{bold}Scanning Server for Vulnerability.\n{reset}")
        os.system(f"nikto -h{domainName}")
        print("")

        #subfinder
        print(f"{blue}{bold}Find all Subdomains.\n{reset}")
        os.system(f"subfinder -d {domainName}")
        print("")

        #skipfish 
        print(f"{blue}{bold}Other Vulnerability scanning...\n{reset}")
        os.system(f"skipfish -o fstscan {domainName}")
        print("")
    except exception as errorFound:
        (f"An Error Occurred : {errorFound}")
        sys.exit


# call Main Function
if __name__ == "__main__":
    fullVulnerabilityScan()