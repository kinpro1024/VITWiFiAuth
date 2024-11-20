#Welcome to kinpro1024's Script, and forget having to put in Wi-Fi credentials every damn hour
#Made with 🩷 for you.

import requests
import sys
import UsernameANDPassword

session = requests.Session()

login_url = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "phc.prontonetworks.com",
    "Origin": "http://phc.prontonetworks.com",
    "Referer": "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://phc.prontonetworks.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}

payload = {
    "userId": UsernameANDPassword.get_username(),
    "password": UsernameANDPassword.get_password(),
    "serviceName": "ProntoAuthentication",
    "Submit22": "Login"
}

#POST request to send credentials
response = session.post(login_url, headers=headers, data=payload)

if response.status_code == 200:
    print("Login attempt sent successfully.")
    sys.exit()
else:
    print("Login failed with status code:", response.status_code)
    sys.exit()

#MonarchAutomationSystems?