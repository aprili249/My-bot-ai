import requests
import random
from uuid import uuid4
import os, time
from time import sleep
from user_agent import generate_user_agent as ngm_user
import sys
from os import system

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
W="\033[1;37m" # White
P216 = '\x1b[38;5;190m' # أصفر مخضر
RE = '\033[0m'     # إعادة تعيين
logo = f'''

██╗███╗░░██╗░██████╗████████╗░█████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝
{RE} {F}
programmer  ➠ @ixe_m | telegram channel ➠ @TechNGM

'''
print(logo)
try:
    
    CHAT_ID = int(input(f' {C}ID : {RE} '))
    print() 
    TOKEN = input(f' {Y}TOKEN : {RE}')
except:
        
        print('Erro in input ❌')
        exit()
system('clear')

        
                
                        

                                                                          
print(logo)
print()
print()
#nas = '0123456789_abcdefghijkl_mnopqrstuvwxyz'

while True:
    
    URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    

    user = "".join(random.choice('qwertyuiopasdfghjklzxcvbnm.__1234567890')for i in range(5))
    
    
    cookies = {
        'csrftoken': 'RoKKAy5GdaswTq3eX_Hlmy',
        'datr': 'cXDeaXp9ZNHbG0SD45ld5zsV',
        'ig_did': '2DC4EBBF-257A-4898-91F9-8B1BAD9A97B5',
        'mid': 'ad5wcgABAAFNzREeyOZXFsmtq-oM',
        'ps_l': '1',
        'ps_n': '1',
        'dpr': '2.082077741622925',
        'wd': '891x1756',
    }
    
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'csrftoken=RoKKAy5GdaswTq3eX_Hlmy; datr=cXDeaXp9ZNHbG0SD45ld5zsV; ig_did=2DC4EBBF-257A-4898-91F9-8B1BAD9A97B5; mid=ad5wcgABAAFNzREeyOZXFsmtq-oM; ps_l=1; ps_n=1; dpr=2.082077741622925; wd=891x1756',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/emailsignup/?next=',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Linux"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': ngm_user(),
        'x-asbd-id': '359341',
        'x-csrftoken': 'RoKKAy5GdaswTq3eX_Hlmy',
        'x-fb-friendly-name': 'useCAARegistrationFieldValidationQuery',
        'x-fb-lsd': 'AdQqoTUNwbNzUSV6irnhb5aFMQ0',
        'x-ig-app-id': '936619743392459',
        'x-ig-max-touch-points': '2',
    }
    
    data = {
        'av': '0',
        '__d': 'www',
        '__user': '0',
        '__a': '1',
        '__req': 'a',
        '__hs': '20573.HYP:instagram_web_pkg.2.1...0',
        'dpr': '3',
        '__ccg': 'MODERATE',
        '__rev': '1038496790',
        '__s': 'p5nk6x:bb50gx:k73tvc',
        '__hsi': '7634548791663122459',
        '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0qa0FE2awpUO0n24o5-1ywOwv89k2C1FwnE6a0D85m1mzXwae4UaEW2G0AEco5G0zK1swUwtE1wEbUGdwtUdUaob82ZwrUdUbGwmk0KU6O1FwlAcwnJ6goK1sAwHxW1owLwfybyohw5ywuU1FU',
        '__csr': 'gJbkQBORk4kbPYiDsQT_OQxcIPREGFbcOZhald9f_ACGmWBjh5Gn-iiF9tuijmax64ki8Cxqby-qEoxluZnFJl8iiiVaHgx8gCEycxa5aABCBF4y64ogbldBjybiHjHFi28DGe-8yUdEnxeRUkyWy8CryojxuaDgGdwyy98KaybwHAStpEmx-5Ai78HKFE4emcw_wmE46awbR0ae00lSqidzo0NNG4U1O80k2yU5mHwn80gEDg0sc4yK2x0gFA0q1xy1jw2d9A0r20EE42nm4UxgC3S3ul241HU860hm0c6AwiE088o070i07F8',
        '__hsdp': 'goB2A-Mkwj2Ux7-ozBK58xNmMwxBUy4UlgSdxa0YUaEfoiggwhWwjEm81Oxcm06y80xK038C08Lg1VU1-o0obw4hw',
        '__hblp': '05zwAxO4E3PwlU3swtE886ymewLwgE6q1Pw9-1XwZwpE3swcm0CU9E6q3i3e0uu09Aw1m-1fxyS0fYwi8-ewto6y0m20rC0Zo10U1Mo32w21EmxS0Do2Iw4hwmU',
        '__sjsp': 'goB2A-Mkwj2Ux7-ozBK58xTdI88AZUy3ydxa0YUaEfoiggwhWwjEm81Oxcm',
        '__comet_req': '7',
        'lsd': 'AdQqoTUNwbNzUSV6irnhb5aFMQ0',
        'jazoest': '22399',
        '__spin_r': '1038496790',
        '__spin_b': 'trunk',
        '__spin_t': '1777556909',
        '__crn': 'comet.igweb.PolarisCAAIGRegistrationHomepageRoute',
        'qpl_active_flow_ids': '516759801',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useCAARegistrationFieldValidationQuery',
        'server_timestamps': 'true',
        'variables': f'{{"input":{{"fetch_username_suggestions":true,"field_name":"USERNAME","username":{{"sensitive_string_value":"{user}"}}}},"scale":3}}',
        'doc_id': '25391252800555418',
        'fb_api_analytics_tags': '["qpl_active_flow_ids=516759801"]',
    }
    
    response = requests.post('https://www.instagram.com/api/graphql', cookies=cookies, headers=headers, data=data).text
    
    
    
    
    
    




    if '''"error":{"code":null}''' and '''"status":"SUCCESS"''' in response:
        
        print(f' {F} Good user  : {RE} {Y} {user} {RE} ')
        
        god = f'''
    GOOD USER BY : @ixe_m ✅
    ___________________________ 
    ✅ Good user : <code>{user}</code>
    ___________________________
    💻 Def : @ixe_m
    ___________________________
    🔱 Channel : @TechNGM
    ___________________________
    '''
    
        try:
            requests.post(URL, data={
                "chat_id": CHAT_ID,
                "text": god,
                "parse_mode": "HTML"
            }, timeout=5)
        except:
            pass
    
    else:
        print(f' {Z} Bad user :{RE} {X} {user} ')
        
        