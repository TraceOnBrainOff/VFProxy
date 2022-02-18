import requests
import string
import random
from urllib.parse import quote_plus
import datetime
import os

class VFProxy():
    def __init__(self):
        mail_domain = random.choice(["@gmail.com", "@hotmail.com", "@outlook.com", "@comcast.net", "@aol.com", "@yandex.com", "@icloud.com", "@yahoo.com", "@mail.com"])
        self.email = (''.join(random.choice(string.ascii_uppercase) for i in range(10))+mail_domain)
        self.user_agent = 'Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36'
    def download_file(self, voice_name="Jerkface", text="Test", *, encode=False, save_wav=True):
        #<emphasis level=\"strong\"><prosody rate=\"+5%\"> for the funny voice + Shouty
        url = "https://api.voiceforge.com:443/swift_engine?HTTP-X-API-KEY=9a272b4&voice={0}&msg={1}&email={2}".format(voice_name, quote_plus(text), self.email)
        today = datetime.datetime.now()
        file_name = str("{0} - {1}".format(voice_name, today.strftime("%m-%d-%Y %H-%M-%S")))
        
        if os.path.isdir("outputs")==False:
            os.mkdir("outputs")
        if os.path.isdir("outputs_mp3")==False:
            os.mkdir("outputs_mp3")
        r = requests.get(url)
        open("outputs/{0}.wav".format(file_name), 'wb').write(r.content)
        if save_wav:
            print("WAV_LOCATION:{0}".format("/outputs/{0}.wav".format(file_name)))
        if encode:
            os.system("lame -q0 -b128 --resample 16 \"outputs/{0}\" \"outputs_mp3/{1}\"".format(file_name+'.wav', file_name+'.mp3'))
            print("MP3_LOCATION:{0}".format("outputs_mp3/{0}".format(file_name+'.mp3')))
        if save_wav==False:
            os.system("rm \"outputs/{0}.wav\"".format(file_name))
