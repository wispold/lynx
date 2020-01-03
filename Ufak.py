import sys
from time import sleep

def delay(a):
    for i in a:
        for b in i:
            print(b, end='')
            sleep(0.045)
        sleep(0.75)
        print("")

def intro():

#GİRİŞ

    a = ["Merhaba dünyalı, geleceğindeki kötü talihini yenebilmen için seni seçtik.",
         "Geçmişindeki anahtar seçimleri tekrar gözden geçirerek hayatta kal.",
         "İyi Şanslar",
         ""]
    delay(a)
    name = input('Adın nedir dünyalı?: ')
    sleep(0.5)
    a = [f'Merhaba {name}']
    delay(a)
    age = int(input('Kaç yaşındasın?: '))
    sleep(1)

#YAŞ KONTROLÜ
    
    if age >= 70:
        a = ["Bu işler için çok yaşlısın.",
             "Emekli olup gençlere yer açma zamanı geldi."]
        delay(a)
        sys.exit()
    elif 70 > age >= 18:
        a = ["Lisede ders sırasında uyukladığın zamana döndük.",
             "Sağ tarafındaki sevgilin sana bir kağıt uzatıyor.",
             "Ne yapacaksın?"]
        delay(a)
        x = input('al, alma: ')
        y = z = None
        sleep(1)
    elif 14 < age < 18:
        a = ["İlkokulda gürültülü bir teneffüsteyiz.",
             "Müdürün kızı Aylayı tahtaya yazacak mısın?"]
        delay(a)
        x = z = None
        y = input('evet, hayır: ')
        sleep(1)
    elif 11 <= age <= 14:
        a = ["Sokakta oyun oynuyorsunuz ve top arabanın altında sıkıştı.",
             "Ne yapacaksın?"]
        delay(a)
        x = y = None
        z = input('topu al, başkasını gönder: ')
        sleep(1)
    elif age <= 10:
        print("Evine dön çocuk!")
        sleep(2)
        sys.exit()

#PATH >= 18
    
    #NODE 1
        
    if x=='al':
        a = ["Klasik canımlı cicimli aşk notlarından biri.",
             "Gülümsemeyle karşılık verdin ve önüne döndün.",
             "Tahtayı öğretmen sıranın önünde durduğu için göremediğini fark ettin."]
        delay(a)
        x1 = input('kağıdı sakla, sessiz kal: ')
        sleep(1)
    elif x=='alma':
        a = ["Kağıdı almayıp uyuklamaya devam ettin.",
             "Sinirlenen sevgilin seni öğretmene ispiyonladı."]
        delay(a)
        x1 = input('yalan söyle, kabul et: ')
        sleep(1)
    else:
        x1 = x2 = x3 = 0

    #NODE 2

    if x1=='kağıdı sakla':
        a = ["Kağıdı sakladın.",
             "Öğretmen bir süre daha seni süzerek derse geri döndü."]
        delay(a)
        x2 = input('uyumaya devam et, derse dön: ')
        sleep(1)
    elif x1=='sessiz kal':
        a = ["Öğretmen elini avucu açık bir şekilde sana uzatır."]
        delay(a)
        x2 = input('kağıdı ver, özür dile: ')
        sleep(1)
    else:
        x2 = 0

    
    if x1=='yalan söyle':
        a = ["Yalanın inandırıcı değildi.",
             "Bir gün yok yazıldın.",
             "Sevgilin ile kavga ettiniz.",
             "Ancak o tüm hatanın sende olduğunu söylüyor."]
        delay(a)
        x3 = input('ayrıl, barış: ')
        sleep(1)
    elif x1=='kabul et':
        a = ["Öğretmen başında biter"]
        delay(a)    
        x3 = input('sessiz kal, özür dile: ')
        x2 = None
        sleep(1)
    else:
        x3 = 0
    
    #ENDİNG
    
    if x2=='uyumaya devam et':
        a = ["Ders sonuna kadar güzel rüyalar gördün.",
             "Ancak gelecek için önemli bir bilgiyi kaçırdın.",
             "Ne yazık ki geleceğin değişmedi.",
             "GAME OVER"]
        delay(a)
    elif x2=='derse dön':
        a = ["Hayatta kalma ile ilgili ufak ve yararlı bir şey öğreniyorsun.",
             "Bu ufak bilgi gelecekte güvende olmanı sağlıyor.",
             "YOU WON"]
        delay(a)
    
    if x2=='kağıdı ver':
        a = ["Müdür sizi odasına çağırdı.",
             "Uzun bir nutuktan sonra aileniz ile konuştu.",
             "Aileniz size nakil etti",
             "Geleceğin tehlikesinden uzak bir yere taşındınız",
             "YOU WON!"]
        delay(a)
    elif x2=='özür dile':
        a = ["Özrün kabul edildi"]
        delay(a)
        x2 = input('uyumaya devam et, derse dön: ')
        if x2=='uyumaya devam et':
            a = ["Ders sonuna kadar güzel rüyalar gördün.",
             "Ancak gelecek için önemli bir bilgiyi kaçırdın.",
             "Ne yazık ki geleceğin değişmedi.",
             "GAME OVER"]
            delay(a)
        elif x2=='derse dön':
            a = ["Hayatta kalma ile ilgili ufak ve yararlı bir şey öğreniyorsun.",
             "Bu ufak bilgi gelecekte güvende olmanı sağlıyor.",
             "YOU WON"]
            delay(a)
    else:
        x2 = 0
        
    if x3=='ayrıl':
        a = ["Depresyona girdin.",
             "Geleceğin eskisinden daha da kötüleşti.",
             "GAME OVER"]
        delay(a)
    elif x3=='barış':
        a = ["Barıştınız.",
             "Ancak o kısa tartışma sırasında dikkatinizi dersinize veremediniz.",
             "Gelecek için önemli bir bilgiyi kaçırdın.",
             "Ne yazık ki geleceğin değişmedi.",
             "GAME OVER"]
        delay(a)

    if x3=='sessiz kal':
        a = ["Sınıftan atıldın.",
             "Gelecek için önemli bir bilgiyi kaçırdın.",
             "Ne yazık ki geleceğin değişmedi.",
             "GAME OVER"]
        delay(a)
    elif x3=='özür dile':
        a = ["Sınıftan atıldın.",
             "Gelecek için önemli bir bilgiyi kaçırdın.",
             "Ne yazık ki geleceğin değişmedi.",
             "GAME OVER"]
        delay(a)
    else:
        x3 = 0

    if age < 18:
        x1 = x2 = x3 = None

#PATH 14 < < 18

    #NODE 1

    if y=='evet':
        a = ["Ders zili çalar ve öğretmen içeri girer.",
             "Ancak öğretmen tahtatki isimleri dikkate almaz.",
             "Aylanın sırıttğını fark edersin."]
        delay(a)
        y1 = input('öğretmeni uyar, sessiz kal: ')
        sleep(1)
    elif y=='hayır':
        a = ["Ders zili çalar ve öğretmen içeri girer.",
             "Sınıf arkadaşlarının rahatsız edici bakışlarına maruz kalırsın.",
             "Aylanın gülümsediğini fark edersin.",
             "Öğretmene Aylanın ismini verecek misin?"]
        delay(a)
        y1 = input('evet, hayır: ')
        sleep(1)
    else:
        y1 = 0

    #NODE 2

    if y1=='öğretmeni uyar':
        a = ["Öğretmen sana aldırmadan derse devam eder.",
             "Teneffüste müdürün odasına çağrılırsın.",
             "Ayla'dan özür dilemen istenir."]
        delay(a)
        y2 = input('özür dile, özür dileme: ')
        y3 = None
        sleep(1)
    elif y1=='sessiz kal':
        a = ["Ders devam eder",
             "Teneffüste, Ayla senini kışkırtır.",
             "Tepki gösterecek misin?"]
        delay(a)
        y2 = None
        y3 = input('evet, hayır: ')
        sleep(1)
    elif y1=='evet':
        a = ["Öğretmen Aylayı mecburen cezalandırır.",
             "Müdürün odasına çağrılırsın.",
             "Okuldan atıldın ve başka bir okula transfer oldun.",
             "Hayatta kalma ile ilgili ufak ve yararlı bir şey öğreniyorsun.",
             "Bu ufak bilgi gelecekte güvende olmanı sağlıyor.",
             "YOU WON"]
        delay(a)
    elif y1=='hayır':
        a = ["Ders devam eder",
             "Teneffüste, Ayla senini kışkırtır.",
             "Tepki gösterecek misin?"]
        delay(a)
        y2 = None
        y3 = input('evet, hayır: ')
        sleep(1)
    else:
        y2 = y3 = 0

    #ENDİNG

    if y2=='özür dile':
        a = ["Özrün kabul edildi.",
             "Teneffüste, Ayla senini kışkırtır.",
             "Tepki gösterecek misin?"]
        delay(a)
        y3 = input('evet, hayır: ')
        sleep(1)
    elif y2=='Özür dileme':
        a = ["Okuldan uzaklaştırma cezası aldın.",
             "Bu sırada geleceğin önemli bir bilgiyi öğrenme fırsatını kaçırdın.",
             "GAME OVER"]
        delay(a)
    else:
        y3 = 0
    
    if y3=='evet':
        a = ["Müdürün odasına çağrılırsın.",
             "Okuldan atıldın ve başka bir okula transfer oldun.",
             "Hayatta kalma ile ilgili ufak ve yararlı bir şey öğreniyorsun.",
             "Bu ufak bilgi gelecekte güvende olmanı sağlıyor.",
             "YOU WON"]
        delay(a)
    elif y3=='hayır':
        a = ["Geleceğin için önemli bir bilgiyi öğrenme şansını elde ettin.",
             "Ancak özgüvenini kaybettiğin için bu bilgiyi uygulamaya koyamadın.",
             "GAME OVER"]
        delay(a)

    if age >= 18 or 11 <= age <= 14:
        y1 = y2 = y3 = None

#PATH 11 <= <= 14

    #NODE 1

    if z=='topu al':
        a = ["Topu almak için arabanın altına girersin.",
             "Topa ellerinle uzanmaya çalışırken araba hareketlenir.",
             "GAME OVER"]
        delay(a)
        z1 = 0
    elif z=='başkasını gönder':
        a = ["Bir arkadaşın topu almak için arabanın altına girer.",
             "Arkadaşın topa ayaklarıyla uzanmaya çalışırken araba hareketlenir.",
             "O sırada arabaya oldukça yakınsın."]
        delay(a)
        z1 = input('arabanın önüne geç, arkadaşını çek, hiç bir şey yapma: ')
        sleep(1)
    else:
        z1 = 0

    #NODE 2

    if z1=='arabanın önüne geç':
        a = ["Arabanın önüne atılırsın.",
             "Ancak arabayı durdurabilecek kadar güçlü değilsin.",
             "GAME OVER"]
        delay(a)
        z2 = None
    elif z1=='arkadaşını çek':
        a = ["Hızlıca atılıp arkadaışının kolundan çekersin.",
             "Çok az bir farkla ezilmekten kurtulur.",
             "Arkadaşının annesi hızlıca olay yerine gelir."]
        delay(a)
        z2 = input('Olanları anlatacak mısın? evet, hayır: ')
        sleep(1)
    elif z1=='hiç bir şey yapma':
        a = ["Arkadaşının annesi hızlıca olay yerine gelir.",
             "Olayın şoku ile eve kaçıp saklanırsın.",
             "Ve bir daha da çıkamazsın.",
             "GAME OVER"]
        z2 = None
        delay(a)
    else:
        z1 = z2 = 0

    if z2=='evet':
        a = ["Annesi olanları duyduğunda seni sorumsuzluk ile suçlar.",
             "Aileleriniz arası bozulur ve kötü gelecekten uzak bir diyara taşınırsınız.",
             "YOU WON"]
        delay(a)
    elif z2=='hayır':
        a = ["Annesi arkadaşını hastaneye götürür.",
             "Yaşananlardan sonra suçluluk duygusu ile arkadaşına sürekli yardımcı olursun.",
             "Ama cenazene mahalle esnafı bile gelmez çünkü arkadaşının çıkardığı dedikodular linç edilmene neden olmuştur.",
             "GAME OVER"]
        delay(a)

    if 14 < age or z=='topu al':
        z1 = z2 = None

#ZERO

    def flee():
        print("Kaçma!")
        sleep(1)
        print("Bam!!!")
        sleep(1)
        print("GAME OVER")
        sleep(2)

    if z1 and z2==0:
        flee()
    elif y1 and y2 and y3==0:
        flee()
    elif x1 and x2 and x3==0:
        flee()

  
intro()
#Fin

count = 0
while True:
    a = input('Tekrar denemek ister misiniz? E/H: ')
    count += 1
    if a.lower() == 'e':
        intro()
    elif a.lower() == 'h':
        print("Şimdi çıkılıyor")
        u = ["o"]
        for i in u*3:
            print(i, end=' ')
            sleep(1)
        sys.exit()
    elif count == 3:
        a = ["さよなら"]
        delay(a)
        u = ["o"]
        for i in u*3:
            print(i, end=' ')
            sleep(1)
        sys.exit()
    else:
        print("Lütfen geçerli bir cevap girin.")
        sleep(1)              