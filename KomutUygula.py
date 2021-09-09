# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:24:38 2021

@author: User
"""

#from komutsec import Komutsec
import urllib.request
import json
import sys
import requests
from gtts import gTTS
from lxml import html
from random import randint
from playsound import playsound
from türkiye_iller_db import *
from googlesearch import search
import pandas as pd
import numpy as np
import time 
import os
import webbrowser
import speech_recognition as sr

class uygula():
    def iller(self,data):
                          # daha önceden oluşturmuş olduğumuz ve internetten gerekli verileri çekerek tablolarını doldurduğumuz veri tabanından kullanıcının istemiş olduğu il ile alakalı bilgileri almak için tasarlandı bu metot.
        self.seslendirme("BİLGİLER ALINIYOR")
        time.sleep(1)
        data1=data[0].capitalize() # kullanıcıdan gelen isteğin yani il in ilk harfini büyük harf yapıyoruz.Sebebi veritabanına kayıtlı olurken illerin ilk harfinin büyük olması.
        self.baglanti=sqlite3.connect("Turkiye_iller.db") # veri tabanına bağlandık
        self.cursor=self.baglanti.cursor() # imlec oluşturduk.
        sorgu="SELECT il_adı,vali,nufus,il_bilgi from iller JOIN wiki_iller on iller.il_adı=wiki_iller.il_adi WHERE il_adı=?"
        self.cursor.execute(sorgu,(data1,))  # yukarıda veri tabanında olan iki tabloyu birleştirip ihtiyacımız olan il bilgilerini almak için şartlı arama gerçekleştirdik. execute modülü ile kullanıcının istediği ili direk olarak veri tabanından çektik.
        veri=self.cursor.fetchall()
        for i in veri:      # tablo halinde gelen verileri parçaladık.
            iladı=veri[0][0]
            ilvali=veri[0][1]
            ilnüfus=veri[0][2]  
            ilbilgi=veri[0][3]
            self.seslendirme(iladı)  # Seslendirme işlemini sırayla yaptık.Farklı bir seçenek olarak döngü halinde de yapabilirdik.
            time.sleep(1)
            self.seslendirme("İL VALİSİ")
            self.seslendirme(ilvali)
            time.sleep(1)
            self.seslendirme("İL HAKKINDA KISA BİLGİ")
            self.seslendirme(ilbilgi)
            
    def arama(self,data2):
       self.seslendirme(" ARAŞTIRMA YAPILIYOR")
       time.sleep(1)
       self.cumle=' '
       sonuc=[ ]
       for i in range(len(data2)):  # Burada arama yapılacak kelimeler birleşik geldiği için Kelime aralarına birer boşluk koyduk..
          self.cumle=self.cumle+data2[i]
          for j in range(0,1):
              self.cumle=self.cumle+' ' 
       # Burda istenilen arama işlemini google da ilk beş sayfadan random olarak açıyor.
       for i in search(self.cumle,tld='co.in',lang='tr',num=10,stop=5,pause=2):
           print(i)
           sonuc.append(i)
       webbrowser.open(sonuc[randint(0,4)])
       #url="https://google.com/search?q="+self.cumle 
       #webbrowser.get().open(url)
        
     
    def seslendirme(self,yazi):
        tts = gTTS(yazi, lang='tr')
        rand=randint(1,100000)
        file = 'audio-'+str(rand)+'.mp3'
        tts.save(file)
        playsound(file)
        os.remove(file)
        #print(yazi)
        
    def mikrofon(self):
        print('SİZİ DİNLİYORUM')
        r =sr.Recognizer()
        with sr.Microphone() as source:   
            #print('Nasıl Yardımcı olabilirim')
            r.adjust_for_ambient_noise(source) # sesin odaklanması için
            #audio=r.record(source,duration=5)
            audio=r.listen(source)
            data=" "
        try:
            data=r.recognize_google(audio,language='tr')
            #print(data)
        except sr.UnknownValueError:
            print("SİSTEM SESİNİ ALGILAYAMADI")
        except sr.RequestError as e:
            print("SİSTEM KONUŞMA TANIMA SİSTEMİ HİZMET VEREMEDİ; {0}".format(e))
        return data
                
        
        