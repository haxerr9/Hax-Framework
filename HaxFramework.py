# Tool By hax / haxer
import os
import subprocess
import pyfiglet
import itertools
import random
from wordlistgen import genWordlist
from wordlistgen import totalPass

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

Wordlist Generator Help Menu:
    Ex. Usage:
        -> wlgen [WORDS] [OPTIONS ](No spaces, seperate words by ";")
        -> wlgen name;surname;age -min=6 -max=12

    Options:
        -> -min=[MIN LENGTH] / --min-length=[MIN LENGTH]        = Specify the min lenght for each generated password.
        -> -max=[MAX LENGTH] / --max-length=[MAX LENGTH]        = Specify the max lenght for each generated password.
   
    

"""

print("Welcome To \n", banner, "\nConsole!\n\n### Made By Arda Utku Kalmaz - @hax9999 / @_haxerr ###")
print(hMenu)


print(" --> HaxFramework Loaded. Type 'help' for help menu. ")

def hScan(IP, COMMANDS):
    command = f"nmap {IP} {COMMANDS}"
    result = os.system(command)

    print(result)


while True:
    cmd = input("\nHF_2.0>>> ")

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

    elif cmd.startswith("wlgen "):
        cmdParts = cmd.split()

        words = cmdParts[1]
        minLen = None
        maxLen = None

        for part in cmdParts:
            if part.startswith("--min-length") or part.startswith("-min"):
                minLen = int(part.split('=')[1])

            elif part.startswith("--max-length") or part.startswith("-max"):
                maxLen = int(part.split('=')[1])

        if minLen != None and maxLen != None:
            genWordlist(words, minLen, maxLen)
            totalPass()
    


    else:
        print("\n[!] Not A Valid Command !")
