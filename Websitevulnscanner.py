import requests

import os

os.system('clear')

print("""\033[92m[+]pogi ako[+]

╔═══════════════════ ══

║Vulnerability scanner║

╚═══════════════════ ══

\033[91m[+]CODED BY PH.BL4CK[+]

""")

domain = str(input("[+]ENTER THE TARGET SITE :\033[91m"))

headers = requests.get(domain).headers

if 'x-frame-Options' in headers:

        print(" \033[91m [NOT VULNERABLE] " + domain)

else:

    print("\033[92m[VULNERABLE] " + domain) 
