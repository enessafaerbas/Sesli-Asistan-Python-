# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:38:05 2021

@author: User
"""
"""
Bu sayfa da Özet olarak : 
    İki farklı sisteden istenilen bilgiler çekildi.Ve veri tabanında iki ayrı tabloya Kaydedildi.
    iki ayrı siteden çekmemin sebebi Wikipedia dan istediğim verilere tam anlamıyla ulaşamadım. Bu sebeple alternatif site bularak 
    verileri oradan çektim.
    Kodları çalıştırırken metotların objesini oluşturmak gerekmekte Veri tabanına kayıt etmek için birer kere çalıştırıldı.
    Verileri Güncel tutmak için sistem geliştirilecek.
"""
from türkiye_iller_db import *
from lxml import *
#import requests  # Yorum satırı yapmamdaki sebep komutuygula kısmmında da requests import etmiş olmam iki tarafta import etmek çakışmaya sebep olmakta.
from bs4 import BeautifulSoup

database=db_olus() 
wiki_database=db_wiki()

class genel():

    def veri_al(self):
        url="https://www.e-yasamrehberi.com/turkiye_il_rehberi.htm"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser")
        #print(r.status_code)
    
        il1 = soup.find("div",attrs={"class":"gridContainer clearfix"}).select("div:nth-of-type(6)>ul>li")
        il2 = soup.find("div",attrs={"class":"gridContainer clearfix"}).select("div:nth-of-type(7)>ul>li")
        il=il1+il2
        
        for i in il:
            il_adi=i.text
            il_link=i.find("a").get("href")
            
            try:
                url1="https://www.e-yasamrehberi.com/"+il_link
                r1=requests.get(url1)
                soup1=BeautifulSoup(r1.content,"html.parser")
                il_bilgi=soup1.find("p",attrs={"class":"lead"}).text
                    
                print(" {} İli Bilgileri \n{}".format(il_adi,il_bilgi))
                il_kayit=bilgiler(il_adi, il_bilgi)  
                database.bilgi_ekle(il_kayit) 
           
            except AttributeError:
                print(" ")


    def veri_al_wikipedia(self):
        url="https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_illeri"
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser")
        print(r.status_code)

        iller_tablo=soup.find("div",attrs={"class":"mw-workspace-container"}).select("table:nth-of-type(2)>tbody>tr>td:nth-of-type(1)>table>tbody")

        i=0
        for iller in iller_tablo:
            il1=iller.select("tr>td:nth-of-type(1)>a")
    
    
            for i in range(len(il1)):
        
                il_adi=iller.select("tr>td:nth-of-type(1)>a")[i].text
                yuz_olcumu=iller.select("tr>td:nth-of-type(2)")[i].text  
                nufus=iller.select("tr>td:nth-of-type(3)")[i].text
                plaka=iller.select("tr>td:nth-of-type(5)")[i].text
                vali=iller.select("tr>td:nth-of-type(7)")[i].text
                print("İl :{}\n Yüz Ölçümü ={}\n Nüfus ={}\n PlakaKodu ={}\n İl Valisi ={}".format(il_adi,yuz_olcumu,nufus,plaka,vali))
                
                wiki_kayıt=wiki_bilgiler(il_adi, yuz_olcumu,nufus,plaka,vali)
                wiki_database.wiki_bilgi_ekle(wiki_kayıt)
                
a=genel()

           
              

        


   


    
    
    
    
