import re,requests,pyfiglet
print(f"            INFO                              {pyfiglet.figlet_format('TikTok')}")
print("[<\>] BY BLACK MIROR")
print("~"*30)
head={
'Host': 'www.tiktok.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Te': 'trailers',
'Connection': 'close',
}
user=input("[?] Type The user:\n")
req=requests.get(f'https://www.tiktok.com/@{user}?lang=en',headers=head)
try:
	inf_user=re.findall('''"user":{(.*?)}''',req.text)[0]
	inf_stat=re.findall('''"stats":{(.*?)},''',req.text)[0]
	print(inf_stat,inf_user)
except:
	print("[!] Error (User Not Found/normal Error) ")


