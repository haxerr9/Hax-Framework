# Script Made By hax / haxer
import requests

def fuzz(url, wordlist, filters):
    with open (f"{wordlist}", "r") as dirs:
        for i in dirs:
            dir = i.strip()
            newUrl = f"{url}{dir}"

            req = requests.get(newUrl)

            filter = int(filters)

            resLen = len(req.content)
            resCode = req.status_code


            if filter != None:
                if int(resCode) == filter:
                    print(f"/{dir} >>>", resCode, f"LEN={resLen}")

            elif filter == None:
                print(f"/{dir} >>> Response: ", resCode, f"LEN={resLen}")

