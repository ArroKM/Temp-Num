# Coded By AseCx
# XiuzCode
import os, re
from time import sleep
try:
	from bs4 import BeautifulSoup as ser
except ImportError:
	os.system("python3 -m pip install -q bs4")
try:
	import requests as get
except ImportError:
	os.system("python3 -m pip install -q requests")

class Nomor:
	def __init__(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		logo()
		url = "https://www.temp-mails.com/lan/id/number"
		self.get_1(url)

	def get_1(self, url):
		ambil = ser(get.get(url).text, "html.parser")
		parser = ambil.find("div", id="content")
		fnomor = parser.find_all("div", class_="own-num")
		nom = [res.text for res in fnomor]
		print("="*31)
		for me in nom:
			num = me.replace("\n", "")
			print(f' \x1b[1;92m(\x1b[1;91m+\x1b[1;92m)\x1b[1;96m>> \x1b[1;97m{num}\t✅ \x1b[1;94mON\x1b[1;91m')
		print("="*31)
		print(" \x1b[1;96mGUNAKAN NOMOR YANG TERSEDIA")
		print(" \x1b[1;96mJANGAN LUPA CEK KONTAK MASUK NYA")
		print("\x1b[1;91m="*31)
		print(" \x1b[1;92m(\x1b[1;96mA\x1b[1;92m) \x1b[1;97mKONTAK MASUK")
		print(" \x1b[1;92m(\x1b[1;96mB\x1b[1;92m) \x1b[1;97mTENTANG KAMI")
		print(" \x1b[1;92m(\x1b[1;91mE\x1b[1;92m) \x1b[1;97mKELUAR")
		print("\x1b[1;91m="*31)
		pil = input(" \x1b[1;96mPILIH NO : \x1b[1;92m")
		print("\x1b[1;91m="*31)
		if pil == "A" or pil == "a":
			self.pesan(url)
		elif pil == "B" or pil == "b":
			logo()
			tentang()
		else:
			exit("\n \x1b[1;97mTERIMA KASIH ..")

	def pesan(self, url):
		print("\n \x1b[1;96mMENUNGGU PESAN MASUK ...")
		while True:
			try:
				ambi = ser(get.get(url).content, "html.parser")
				tabl = ambi.find("div", id="tablenumber")
				tim = tabl.find("td", class_="sms-date").text
				fro = tabl.find("td", class_="sms-from").text
				to = tabl.find("td", class_="sms-to").text
				sear = tabl.find("button", attrs={"class":"btn btn-primary open-msg-btn"})
				pes = re.findall("data-text=\"(.*?)\"", str(sear))
				if str(tim) == "1 detik yang lalu":
					print("\n\x1b[1;91m>>>>>>>>>\x1b[1;92m(\x1b[1;94mPESAN MASUK\x1b[1;92m)\x1b[1;91m<<<<<<<<<\n")
					print(" \x1b[1;96mDATE  : \x1b[1;97m"+tim)
					print(" \x1b[1;96mFROM  : \x1b[1;97m"+fro)
					print(" \x1b[1;96mTO    : \x1b[1;97m+"+to)
					print(" \x1b[1;96mPESAN : \x1b[1;97m"+pes[0].replace("&amp;lt#&amp;gt",""))
					print("\n\x1b[1;91m>>>>>>>>>\x1b[1;92m(    \x1b[1;94mEND    \x1b[1;92m)\x1b[1;91m<<<<<<<<<\n")
					sleep(1)
					continue
				else:
					continue
			except IndexError:
				continue

def logo():
	print('''
\x1b[1;94m╭━━━━┳━━━┳━╮╭━┳━━━\x1b[1;91m┳━╮ ╭┳╮ ╭┳━╮╭━╮
\x1b[1;94m┃╭╮╭╮┃╭━━┫┃╰╯┃┃╭━╮\x1b[1;91m┃┃╰╮┃┃┃ ┃┃┃╰╯┃┃
\x1b[1;94m╰╯┃┃╰┫╰━━┫╭╮╭╮┃╰━╯\x1b[1;91m┃╭╮╰╯┃┃ ┃┃╭╮╭╮┃
\x1b[1;94m  ┃┃ ┃╭━━┫┃┃┃┃┃╭━━\x1b[1;91m┫┃╰╮┃┃┃ ┃┃┃┃┃┃┃
\x1b[1;94m  ┃┃ ┃╰━━┫┃┃┃┃┃┃  \x1b[1;91m┃┃ ┃┃┃╰━╯┃┃┃┃┃┃
\x1b[1;94m  ╰╯ ╰━━━┻╯╰╯╰┻╯  \x1b[1;91m╰╯ ╰━┻━━━┻╯╰╯╰╯
  \x1b[105m\x1b[37;1mCODED BY ASECX FROM XIUZCODE\x1b[0m''')

def tentang():
	print("\x1b[1;91m="*31)
	print('''\x1b[1;96m AUTHOR   : \x1b[1;97mASE-XC
\x1b[1;96m GITHUB   : \x1b[1;97mhttps://github.com/ArroKM
\x1b[1;96m SUPPORT  : \x1b[1;97mXIUZCODE
\x1b[1;96m FACEBOOK : \x1b[1;97mhttps://www.facebook.com/zain.mistyc''')
	print("\x1b[1;91m="*31)
	input("\n\x1b[1;92m ENTER UNTUK KEMBALI ()> ")
	Nomor()

if __name__=="__main__":
	try:
		Nomor()
	except KeyboardInterrupt:
		print("\n \x1b[1;97mTERIMA KASIH ..")
