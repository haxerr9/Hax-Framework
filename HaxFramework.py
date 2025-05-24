# Tool By hax / haxer
import os
import time
import subprocess
import pyfiglet
import itertools
import random

from wordlistgen import genWordlist
from wordlistgen import totalPass

from portscan import portscan
from portscan import defaultPorts

from fuzzer import fuzz

bannerText = "     Hax Framework"
banner = pyfiglet.figlet_format(bannerText)

hMenu = """

        --- Hax Framework Help Menu ---

Misc:
    -> clear        = Clear the terminal
    -> t [COMMAND]  = Execute a terminal command.
    -> exit         = Exit.   

Port Scanner:
    Usage:
        -> scan [IP / HOST] [COMMANDS]
        -> scan 192.168.1.1 -p 80

    Options:
        -> -p [PORT(s)]         = Specify ports for scanning (default=most-used 1000 ports)

Wordlist Generator:
    Usage:
        -> wlgen [WORDS] [OPTIONS ](No spaces, seperate words by ";")
        -> wlgen john;doe;32 -min=6 -max=12

    Options:
        -> -min [MIN LENGTH] / --min-length [MIN LENGTH]        = Specify the min lenght for each generated password.
        -> -max [MAX LENGTH] / --max-length [MAX LENGTH]        = Specify the max lenght for each generated password.

Web Fuzzer:
    Usage:
        -> fuzz [URL] [WORDLIST]
        -> fuzz -u https://exmaple.com/ -w wordlist.txt -f 200

    Options:
        -> -u [URL]              = Specify an URL to scan.
        -> -w [WORDLIST]         = Specify a wordlist file for scan.
        -> -f [FILTER]           = Specify filters to apply for response code.
   
"""


print("Welcome To \n", banner, "\n\n### Made By Arda Utku Kalmaz - @hax9999 / @_haxerr ###")
time.sleep(0.2)
print(hMenu)


print(" --> HaxFramework Loaded. Type 'help' for help menu. ")

try:
    while True:
        cmd = input("\nhf-v5.5>>> ")


        # // HELP MENU //
        if cmd == "help" or cmd == "Help":
            print(hMenu)

        # // EXIT COMMAND //
        elif cmd == "exit" or cmd == "Exit":
            break

        # // CLEAR COMMAND //
        elif cmd == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
        
        # // TERMINAL COMMANDS //
        elif cmd.startswith("t "):
            cmdParts = cmd.split()
            command = " ".join(cmdParts[1:])
            os.system(command)
        
        # // PORT SCAN COMMANDS
        elif cmd.startswith("pscan "):
            cmdParts = cmd.split()

            try:
                hostAddr = cmdParts[1]
                ports = int(cmdParts[3])     
            except IndexError:
                ports = None

            if ports != None:
                portscan(hostAddr, ports)
            
            elif ports == None:
                print("[?] No Ports Specified; Scanning Most-Used 1000 Ports By Default...\n")
                portscan(hostAddr, defaultPorts)

        # // WORDLIST GENERATOR COMMANDS // 
        elif cmd.startswith("wlgen "):
            cmdParts = cmd.split()

            words = cmdParts[1]
            minLenStr = cmdParts[cmdParts.index("-min") + 1] or cmdParts[cmdParts.index("--min-length") + 1]
            maxLenStr = cmdParts[cmdParts.index("-max") + 1] or cmdParts[cmdParts.index("--max-length") + 1]

            minLen = int(minLenStr)
            maxLen = int(maxLenStr)

            if words and minLen and maxLen != None:
                genWordlist(words, minLen, maxLen)
                totalPass()

            elif words and minLen and maxLen == None:
                print("\n[!] Blank Variables !")

        # // FUZZER COMMANDS //
        elif cmd.startswith("fuzz "):
            cmdParts = cmd.split()

            url = cmdParts[cmdParts.index("-u") + 1]
            wordlist = cmdParts[cmdParts.index("-w") + 1]
            filters = cmdParts[cmdParts.index("-f") + 1]
            
            if url and wordlist != None:
                fuzz(url, wordlist, filters)

            elif url and wordlist == None:
                print("\n[!] Blank Variables !")

        else:
            print("\n[!] Not A Valid Command !")

except KeyboardInterrupt:
    print("\n[?] Exiting...")
