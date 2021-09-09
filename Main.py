# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 09:05:21 2021

@author: User
"""
from komutuygula import uygula
from komutsec import Komutsec
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
import pandas as pd
import numpy as np
import time 

# Gerekli kütüphaneler import edidi

uygula1=uygula() # komutuygula.py dosyasındaki uygula class ının nesnesi oluşturuldu. 
uygula1.seslendirme('Nasıl yardımcı olabilirim')  # oluşan nesne ile tanımlı method kullanıldı.

while True:
    
    datax= uygula1.mikrofon()      # Öncelikle mikrofon dan kullanıcının girdisi dinlendi ve değişkene atıldı.    
    komutsec=Komutsec(datax)  # komutsec.py dosyasındaki class ın nesnesi oluştu ve class içindeki init fonkiyonu çalıştı.Mikrofondan gelen veriyi buraya gönderdik ayrışması için
    komutsec.sec()  # Daha sonra komutsec nesnesinin sec methodunu kullanarak istenilen komutu algıladık.

    
    
    
    
    
    
    
    
    