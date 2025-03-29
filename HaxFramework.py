# Tool By hax / haxer
import os
import time
import subprocess
import pyfiglet
import itertools
import random
from wordlistgen import genWordlist
from wordlistgen import totalPass
from bruteforce import bruteForce
from portscan import portscan

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
        -> scan 192.168.1.1 -p 80

    Options:
        -> -p [PORT(s)]         = Specify ports for scanning (default=most-used 1000 ports)

Wordlist Generator Help Menu:
    Ex. Usage:
        -> wlgen [WORDS] [OPTIONS ](No spaces, seperate words by ";")
        -> wlgen name;surname;age -min=6 -max=12

    Options:
        -> -min=[MIN LENGTH] / --min-length=[MIN LENGTH]        = Specify the min lenght for each generated password.
        -> -max=[MAX LENGTH] / --max-length=[MAX LENGTH]        = Specify the max lenght for each generated password.
   
"""


#
"""
Brute Force Help Menu [INSTAGRAM ONLY (For now)]:
    Ex. Usage:
        -> bforce [URL] [PASSLIST] [USERNAME]
        -> bforce --url https://example.com/login -w wordlist.txt -u admin

    Options:
        -> --url [URL]                  = Specify URL for brute force attack.
        -> -w / --wordlist [PATH]       = Specify a password list file (".txt" extension).
        -> -u / --username [USERNAME]   = Specify a username for brute force attack.
   

        
"""
#


print("Welcome To \n", banner, "\nConsole!\n\n### Made By Arda Utku Kalmaz - @hax9999 / @_haxerr ###")
time.sleep(0.2)
print(hMenu)


print(" --> HaxFramework Loaded. Type 'help' for help menu. ")

while True:
    cmd = input("\nHF_3.1>>> ")

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

        hostAddr = cmdParts[1]
        options = " ".join(cmdParts[2:])

        if options.startswith("-p"):
            ports = options.replace("-p", "").strip()
            scanPorts = ports.split(",")
            scanPorts = [int(port) for port in scanPorts]
        
        else:
            print("[?] No Ports Specified; Scanning Most-Used 1000 Ports By Default...\n")
            defaultPorts = [
    7, 9, 13, 17, 19, 20, 21, 22, 23, 25, 27, 53, 67, 69, 70, 79, 80, 88, 110, 111, 
    113, 119, 123, 135, 137, 138, 139, 143, 161, 162, 177, 179, 194, 220, 389, 443, 
    444, 445, 464, 465, 513, 514, 515, 523, 526, 530, 531, 532, 540, 543, 544, 545, 
    547, 548, 554, 563, 587, 591, 593, 611, 631, 636, 639, 646, 647, 648, 649, 650, 
    666, 667, 668, 669, 670, 671, 672, 674, 688, 690, 691, 692, 693, 694, 700, 701, 
    702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 
    718, 719, 720, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 
    735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 
    751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 
    767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 
    783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 
    799, 800, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 
    822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 
    838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 853, 860, 873, 
    883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 
    899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 
    915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 
    931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 
    947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 
    963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 
    979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 
    995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 
    1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 
    1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 
    1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 
    1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 
    1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 
    1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 
    1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 
    1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 
    1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 
    1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 
    1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 
    1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 
    1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 
    1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 
    1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 
    1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 
    1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228, 1229, 
    1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 
    1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 
    1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 
    1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 
    1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 
    1295, 1296, 1297, 1298, 1299, 1300
]  
            scanPorts = defaultPorts

        portscan(hostAddr, scanPorts)

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

    #elif cmd.startswith("bforce "):
    #    cmdParts = cmd.split()

    #    url = cmdParts[cmdParts.index("--url") + 1]
    #    passList = cmdParts[cmdParts.index("-w") + 1]
    #    username = cmdParts[cmdParts.index("-u") + 1]
    
    #    bruteForce(url, passList, username)

    else:
        print("\n[!] Not A Valid Command !")
