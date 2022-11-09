from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from datetime import datetime, timedelta
import random,requests,json
from bs4 import BeautifulSoup

aev = Client("bot")

agnt = {"User-Agent":"Mozilla/5.0 (Linux; Android 11; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"}
api = "http://ip-api.com/json/"
api2 = "https://ipapi.co/"
api4 = "https://ipinfo.io/"

def komut(x,y):
	@aev.on_message(filters.command(x))
	def filtre(bot,msj):
		msj.reply(y)

def cevap(x,y):
	@aev.on_message(filters.text & filters.group)
	def cvp(bot,msj):
		a = msj.text
		for j in x:
			if a == j:
				msj.reply(y)
	
def cevap_in(x,y):
		@aev.on_message(filters.text & filters.group)
		def cvp(bot,msj):
			a = msj.text
			for j in x:
				if j in a:
					msj.reply(y)
				

@aev.on_message(filters.command('start'))
def filtre(bot,msj):
	msj.reply("""
• Komutlar •
/aev > İçerikler
/komutlar > Diğer Komutlar
/link > Ana Kanal
/kural > Kurallar
/admin > Adminler
/info > Admin Sosyal Medya
""")
	
komut("aev","""
İçerik Yok""")

komut("komutlar","""
/bilgi > Kendi Bilgilerini Gösterir.
•
/gayolcu % Kaç Gay Olduğunu Hesaplar.
•
/soyle kelime Kelimeni Tekrar Eder.
•
/gotadam Boş Birşey.""")

komut("admin","""
@aevxofficial""")

komut("info","""
İnstagram: @aevxofficial
Telegram: @aevxofficial
YouTube: aevxofficial""")

komut("kural","""
Gay Şakası ×
Ayak Şakası ×
Herhangi Bir Dine & Bir Ülke Liderine Hakarer ×
Mernis/Data/Cc/Silah Konuşmak Vs ×
Uyuşturucu Konuşmak ×
+18 Paylaşım ×
Tehdit Etme ×
Aşağılamak ×
Küfür ( Abartılmadığı Sürece Serbest )
Reklam & Referans Kasmak ×

•Burası Termux Grubu Sadece Termux, Kali ve Başka Terminaller Hakkında Konuşulur.""")

@aev.on_message(filters.chat(-1001505228725) & filters.new_chat_members)
def hg(client,message):
	message.reply_text("""
	Kanalımıza Hoş Geldin.
	' /yardim '
	Bu Komuta Tıklayarak İstediğine Bakabilirsin.
	""")
	
@aev.on_message(filters.command('ipsorgu') & filters.group)
def ipp(bot,msj):
			ip = msj.text.split(None,1)[1]
			data = requests.get(api+ip+"?fields=66846719").json()
			data2 = requests.get(api2+ip+"/json/").json()
			data4 = requests.get(api4+ip+"/json").json()
			r = requests.get(f'https://www.ipsorgu.com/?ip={ip}',headers=agnt)
			s = BeautifulSoup(r.text,"html.parser")
			if data['proxy'] == True:
				vpn = "Var"
			else:
			      vpn = "Yok"
			      
			if data['mobile'] == True:
				tip = "Mobil Veri"
			else:
				tip = "Wifi"
				
			if data['hosting'] == True:
			      host = "Var"
			else:
			      host = "Yok"

			msj.reply(f"""
İp Adresi: {data['query']}
Host: {data4['hostname']}
İp Adresi Tipi: {data2['version']}
ISS: {data['isp']}
Vpn: {vpn}
Bağlantı: {tip}
Organizasyon: {data2['org']}
Host: {host}
Kıta: {data['continent']}
Kıta Kodu: {data['continentCode']}
Ülke: {data['country']}
Ülke Kodu: {data['country']}
Telefon Kodu: {data2['country_calling_code']}
Ülke Başkenti: {data2['country_capital']}
İl & İlçe: {s.find_all("em")[1].text}
İl Plaka: {data['region']}
Kordinat: `{data2['latitude']},{data2['longitude']}`
Zip Kodu: {data['zip']}
Saat Dilimi: {data['timezone']}
Para Birimi: {data2['currency']}
Para İsmi: {data2['currency_name']}
""")

s = "sa slm sea selam".split()
cevap(s,"Aleyküm Selam")
S = "selamın"
cevap_in(s,"Aleyküm Selam")

@aev.on_message(filters.command('bilgi') & filters.group)
def at(bot,msj):
		aev.send_message(msj.chat.id,f"""
Chat İd: `{msj.chat.id}`
İd: `{msj.from_user.id}`
Kullanıcı Adı: @{msj.from_user.username}
Link: {msj.from_user.mention}
""")

@aev.on_message(filters.command('ban') & filters.group)
def at(bot,msj):
		if msj.from_user.id == 1928227208 or msj.from_user.id == 1973112672:
			aev.ban_chat_member(msj.chat.id,msj.reply_to_message.from_user.id)
			aev.send_message(msj.chat.id,f"{msj.reply_to_message.from_user.mention} Banlandı.")
		else:
			aev.send_message(msj.chat.id,"Banlamak İçin Yetkin Yok.")
		
#@aev.on_message(filters.command('sban') & filters.group)
#def at(bot,message):
#		arg = message.text.split()[1]
#		aev.ban_chat_member(message.chat.id,message.reply_to_message.from_user.id + datetime.now() + timedelta(days=1))
#		aev.send_message(message.chat.id,f"{message.reply_to_message.from_user.mention} Şu Kadar Süre Banlandı. Süre: " + arg + "Saniye")
		
@aev.on_message(filters.command('aban') & filters.group)
def kaldir(bot,msj):
		idno = msj.from_user.id
		if idno == 1928227208 or idno == 1973112672:
			aev.unban_chat_member(msj.chat.id,msj.reply_to_message.from_user.id)
			aev.send_message(msj.chat.id,f"{msj.reply_to_message.from_user.mention} Banı Kaldırıldı.")
		else:
			aev.send_message(msj.chat.id,"Banı Kaldırmak İçin Yetkin Yok.")

@aev.on_message(filters.command("gayolcu") & filters.group)
def gayolcu(bot,msj):
	a = random.randint(0,101)
	if a == 100:
		msj.reply(f"%{a} TOP")
	elif a > 70:
		msj.reply(f'%{a} Gel Beraber Oğlan Si-')
	elif a < 20:
		msj.reply(f"%{a} Homofobik Aferin")
	else:
		msj.reply(f'%{a} Gay')

@aev.on_message(filters.command('soyle') & filters.group)
def soyle(bot,msj):
	yazi = msj.text.split(None,1)[1]
	msj.reply(yazi)
	
@aev.on_message(filters.command('myinfo') & filters.group)
def info(bot,msj):
	msj.reply(aev.get_me())

l = "Kg kg KG kG".split()
l.append("kolay gelsin")
l.append("Kolay gelsin")
for x in l:
	@aev.on_message(filters.regex(x))
	def vdeo(bot,message):
		aev.send_video(message.chat.id,
		video='tsk.mp4')


start = "Ana Kanal"
btn =[[InlineKeyboardButton("Git",url="t.me/termux_egitim")]]
@aev.on_message(filters.command('link') & filters.group)
def buton(bot,message):
	text = start
	reply_markup = InlineKeyboardMarkup(btn)
	message.reply(
	text=text,
	reply_markup=reply_markup,
	disable_web_page_preview=True)
	
aev.run()