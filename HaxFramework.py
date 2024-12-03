# Tool By hax / haxer
import os
import subprocess
import pyfiglet

bannerText = "      Hax Framework"
banner = pyfiglet.figlet_format(bannerText)

hMenu = """

        --- Hax Framework Help Menu ---

Terminal Commands:
    -> clear        = Clear the terminal
    -> t [COMMAND]  = Execute a terminal command.
    -> exit         = Exit.   

Host Scan Help Menu:
    Ex. Usage:
        -> scan [IP / HOST] [COMMANDS]
        -> scan 192.168.1.1 -sC -sV -A -p80 

    Options:
        -> -sS / --syn-scan         = TCP SYN scan.
        -> -sA / --ack-scan         = ACK scan.
        -> -sW / --window-scan      = Window scan.
        -> -sM / --maimon-scan      = Maimon scan.
        -> -sU / --udp-scan         = UDP scan.
        -> -sC / --script-scan      = Scan with NMAP scripts.
        -> -sV / --service-version  = Scan services and versions on ports.
        -> -p  / --port             = Scan given ports (Default 1000).
        -> -O  / --os-scan          = Enable OS detection while scanning.
        -> -A  / --all              = Enable OS detection, version detection, script scanning, and traceroute.


"""

print("Welcome To \n", banner, "\nConsole!\n\n### Made By Arda Utku Kalmaz - @hax9999 / @_haxerr ###")
print(hMenu)


def hScan(IP, COMMANDS):
    command = f"nmap {IP} {COMMANDS}"
    result = os.system(command)

    print(result)

print(" --> HaxFramework Loaded. Type 'help' for help menu. ")

while True:
    cmd = input("\nHF_0.1>>> ")

    if cmd == "help" or cmd == "Help":
        print(hMenu)

    elif cmd == "exit" or cmd == "Exit":
        break

    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
     
    elif cmd.startswith("t "):
        cmdParts = cmd.split()
        command = " ".join(cmdParts[1:])
        os.system(command)
    

    elif cmd.startswith("scan "):
        cmdParts = cmd.split()

        ipAddr = cmdParts[1]
        options = " ".join(cmdParts[2:])
        
        hScan(ipAddr, options)


    else:
        print("\n[!] Not A Valid Command !")
