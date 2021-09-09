# Sesli-Asistan-Python
Bu Uygulamada Sesli Asistan kullanarak Türkiye'de bulunan illerinin kısaca bilgileri verilmektedir.
Uygulamanın gelişimi devam etmektedir. Sizlerin yorum ve fikirlerini beklemekteyim.

# Uygulamada 
Uygulamayı kodlarken fazlaca class ve metot kullandım.Bunun sebebi farklı metotlar farklı .py sayfalrında gerekli olduğu için.
#
Main.py dosyasından uygulamanın çalışması için gerekli döngü ve nesneler tanımlandı. İleriye dönük eklemeler yapmak için main 'i ayrı yapmak istedim.
#
Komut_sec.py Dosyasında ise Kullanıcının söyleyeceği komutlar belirlendi ve gerekli kütüphanelerin import işlemi yapıldı.Kullanıcıdan gelen komtların ayırt edilmesi için gerekli algoritma yazıldı.Kodlar yorum satırlarıyla anlatılmakta.
#
Komut_uygula.py dosyasında sesli asistana ne yaptırmak istiyorsak onu metotlar halinde kodladım. Yapmak istediğim işlemlerin kütüphanelerini import ederek başladım. Sistemi konuşturmak için Gtts, playsound kütüphanesini kullandım. Metot kalıp bir metottur uygulamalarınızda direk olarak kullanabilirsiniz.

Kullanıcını sesini anlayabilmek için speech_recognition kütüphanesini ve bu kütüphanenin içinde olan metotları kullandım.

İnternetten Arama yapmak için webbrowser , googlesearch kütüphanelerini kullandım. Bu metotta iki seçenek vardır. Bu seçeneklerden biri kullanıcının istediği arama sözcüğünü google da arayıp arama sonuclarını gösteren seçenek. Diğer seçenek ise arama sonuçlarının en üstteki 5 sonunçtan random olarak birini seçmesidir. Kullanılan kütüphaneleri metotları kodda yorum satırı olarak anlatılmaktadır.

İlleri tanıttığımız kısım ise iki ayrı py dosyasının gerçekleştirmiş olduğu metotlar ile oluşmaktadır.
Komut_uygula.py dosyasının içindeki iller metot'u iki türkiye_iller.py ve türkiye_iller_db.py dosyalarına bağlantılıdır. Burada Bilgileri internet sitelerinden çekip veri tabanına kayıt ettikten sonra sesli asistana ekleyabildim. Database oluşturup iki ayrı tabloda illerin adlarına göre ihtiyaç duyulan bilgileri çekip veri tabanına kaydettim. Kodlar Yorum satırlarında açıklandı.
türkiye_iller.py dosyasında internetten verileri çekebilmeniz için metotların nesnesini oluşturmanız gerekli. Ben çalıştrırken bir kere çalıştırıp veri tabanına kayıt işlemi gerçekleştirdikten sonra nesneleri sildim. Arayüz tasarımı yaapılırken gerekli düzenlemeler yapılacaktır.


