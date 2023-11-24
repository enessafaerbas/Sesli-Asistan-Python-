# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:11:34 2021

@author: User
"""
from komutuygula import uygula
import urllib.request
import json
import sys
import requests
from gtts import gTTS
from playsound import playsound
from lxml import html
from random import randint
import pandas as pd
import numpy as np
import time 
import os

uygula=uygula()

nasılsın= ["naber","haber","ne yapıyorsun","ne","yapıyorsun","nasılsın","napıyon","nabıyon","ne" ,"var"," ne"," yok"]
cvp_nasılsın = ["iyiyim","çok iyiyim","iyi olmaya çalışıyorum"]
kapat=["görüşürüz","kendini kapat","kapat","tamamdır"]
arama=["ara","yap","google'da","aç","araştır","açarmısın","google'ı","araştırırmısın","araştırma","bul"]
iller=["adana","adıyaman","afyonkarahisar","afyon","ağrı","amasya","ankara","antalya","artvin","aydın","balıkesir","bilecik","bingöl","bitlis","bolu","burdur","bursa","çanakkale","çankırı","çorum","denizli","diyarbakır","edirne","elazığ","erzincan","erzurum","eskişehir","gaziantep","giresun","gümüşhane","hakkari","hatay","mersin","kars","kastamonu","kayseri","kırklareli","kırşehir","kocaeli","konya","kütahya","malatya","manisa","kahramanmaraş","maraş","mardin","muğla","muş","nevşehir","niğde","ordu","rize","sakarya","samsun","siirt","sinop","sivas","tekirdağ","tokat","trabzon","tunceli","şanlıurfa","urfa","uşak","van","yozgat","zonguldak","aksaray","bayburt","karaman","kırıkkale","batman","şırnak","bartın","ardahan","ığdır","yalova","karabük","kilis","osmaniye","düzce"]
iller2=["Isparta","ısparta","isparta","İsparta","ISPARTA","İSTANBUL","istanbul","ıstanbul","Istanbul","İstanbul","İZMİR","İzmir","izmir","Izmır","ızmır"]
komutlar =[nasılsın,kapat,arama,iller,iller2]
# I ı i harflerinde sıkıntı çektiğim için ısparta izmir ve istanbul kelimeleri için ayrı bir dizi yaptım. Isparta için işe yaradı fakat izmir ve istanbul için işe yaramadı.
class Komutsec():
    # init fonkisyonu komutsec nesnesi oluştuğunda çalışmakta. 
    def __init__(self,data):
        self.data1=data.lower() # cümledeki harflarin hepsini büyük harf yapmakta.
        self.data2=self.data1.split() # cümleyi kelime kelime ayormakta
        print(self.data2)
        
        # Burda sisteme daha önceden verilmiş komutların kullanıcı tarafından verilen komutla eşitliği karşılaştırılıyor.
    def sec(self):          
        for i in range(len(komutlar)):
            for j in range(len(komutlar[i])):
                if komutlar[i][j] in self.data2:
                    self.komutkontrol(komutlar[i][j],self.data2)
                    
       # Burada ise sec ten gelen komutların method yönlendirilmesi yapılmakta.         
    def komutkontrol(self,ko,data2):
        if ko in nasılsın:  
            uygula.seslendirme(cvp_nasılsın[randint(0,3)])
        if ko in kapat:
            uygula.seslendirme('Sistem kapanıyor')
            sys.exit()
        if ko in arama: # araştırılmak istenen kelimeleri komuttan ayırmak için pop komutu kullanıldı. Mesela Beşiktaş ı araştır. Buradaki araştır kelimesi çıkarıldı ve google da direk aratılmak istenilen konu aratıldı.
            for i in range(len(arama)): 
                for j in range(len(data2)):
                    if (arama[i]==data2[j]):
                        data2.pop(j)
            uygula.arama(self.data2)        # burada artık uygulama methoduna gidiliyor.  
        if ko in iller:
            uygula.iller(data2)
        if ko in iller2:
            uygula.iller(data2)
        
            
 
                
                
                
                
                
            
            
            
                
            
        
                    
        
        
        
        
        
    
    
    
    
    
    
    
