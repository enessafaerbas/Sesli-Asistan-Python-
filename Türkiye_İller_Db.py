# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:47:59 2021

@author: User
"""


import numpy as np
import sqlite3
import time
"""
Veri Tabanı HAkkında Özet:
    Türkiye_iller adında veri tabanını oluşturduk ve İki ayrı tablo ekledik.
    Daha sonra bu sayfanın yönlendirmesini türkiye_iller.py soyasına ekledim ve orada tabloları doldurdum.
"""
# illerin Tarih bilgilerini veri tabanına kaydettiğimiz kısım
class bilgiler():
    
    def __init__(self,il_adi,il_bilgi):
        self.il_adi=il_adi
        self.il_bilgi=il_bilgi
        
class db_olus():
    
    def __init__(self):
        self.baglanti_olus()    
    
    def baglanti_olus(self):
        self.baglanti=sqlite3.connect("Turkiye_iller.db") 
        self.cursor=self.baglanti.cursor()
        sorgu="Create Table if not exists iller(il_adı TEXT,il_bilgi TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def bilgi_ekle(self,sonuc): # sonuc değerini nesne olarak belirledik ve metot u çağırırken nesne olarak göndericez.
        sorgu="Insert into iller values(?,?)"        # verileri bilgiler class ından aldığımız için böyle bir yöntem kullandık.
        self.cursor.execute(sorgu,(sonuc.il_adi,sonuc.il_bilgi)) 
        self.baglanti.commit()
        

        # Wikipedia dan gelen bilgilerin veri tabana kaydı.
class wiki_bilgiler():
    
    def __init__(self,il_adi,yuz_olcumu,nufus,plaka,vali):
        self.il_adi=il_adi
        self.yuz_olcumu=yuz_olcumu
        self.nufus=nufus
        self.plaka=plaka
        self.vali=vali
        
class db_wiki():    
    def __init__(self):
        self.db_baglan()
    
    def db_baglan(self):
        self.baglanti=sqlite3.connect("Turkiye_iller.db")
        self.cursor=self.baglanti.cursor()
        sorgu="Create Table if not exists wiki_iller(il_adi TEXT,yuz_olcumu INT,nufus INT,plaka INT,vali TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
        
    def wiki_bilgi_ekle(self,sonuc):
        sorgu="Insert into wiki_iller values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(sonuc.il_adi,sonuc.yuz_olcumu,sonuc.nufus,sonuc.plaka,sonuc.vali))        
        self.baglanti.commit()
 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        