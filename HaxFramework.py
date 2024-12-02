# Tool By hax / haxer
import os
import subprocess
import pyfiglet

bannerText = "       Hax Framework"
banner = pyfiglet.figlet_format(bannerText)

hMenu = """

        --- Hax Framework Help Menu ---

Scan Help Menu:
    Ex. Usage:
        -> scan [IP]

"""

print("Welcome To \n", banner, "\nConsole!")
print(hMenu)


def scan(IP):
    command = f"nmap {IP} -sCV -O -A -T4 -v"
    result = os.system(command)

    print(result)

print(" --> HaxFramework Loaded. Type 'help' for help menu. ")

while True:
    cmd = input("\nHaxFramework_0.1 >>> ")

    if cmd == "help" or cmd == "Help":
        print(hMenu)

    elif cmd.startswith("scan "):
        cmdParts = cmd.split()
        
        ipAddr = cmdParts[1]
        scan(ipAddr)

    else:
        print("\n[!] Not A Valid Command !")
