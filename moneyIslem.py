import logModule as log
from getpass import getpass

def paraYatirma(userName,balance):
    paraYatirtxt=f"---------------------------------------\nBakiyeniz: {balance} TL\n---------------------------------------\nLütfen yatırmak istediginiz miktarı giriniz: """
    yatirilan =int(input(paraYatirtxt))
    newAmount=balance+yatirilan
    with open("accounts.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i in range(len(lines)):
     if lines[i].startswith("Kullanıcı adı"):
            userNameControl = lines[i].split(":")[1].strip()
            if userNameControl== userName:
             line_to_update=i+4
             newContent=f"Bakiye            : {newAmount}\n"
             lines[line_to_update] = newContent
             with open("accounts.txt", 'w',encoding='utf-8') as file:
              file.writelines(lines)

def paraGonderme(userNames,balance):
    x=0
    while x<1:
        paraGondertxt=f"---------------------------------------\nBakiyeniz: {balance} TL\n---------------------------------------\nLütfen para göndermek istediğiniz kişinin kullanıcı adını giriniz: """
        userName=input(paraGondertxt) 
        with open("accounts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i in range(len(lines)):
         if lines[i].startswith("Kullanıcı adı"):
                userNameControl = lines[i].split(":")[1].strip()
                if userNameControl== userName:
                 global userBalance
                 userData=log.account_data_getter(userName)       
                 userBalance=userData['balance']
                 a=0
                 while a<1:
                  inputBalance=int(input("Lütfen yatırmak istediğiniz miktarı giriniz: "))   
                  if balance<inputBalance:
                      print("Kendi bakiyenizi aştınız lütfen yenide deneyin")
                  else:
                   userBalance+=inputBalance
                   line_to_update=i+4
                   newContent=f"Bakiye            : {userBalance}\n"
                   lines[line_to_update] = newContent
                   with open("accounts.txt", 'w',encoding='utf-8') as file:
                    file.writelines(lines)
                   with open("accounts.txt", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                   for i in range(len(lines)):
                    if lines[i].startswith("Kullanıcı adı"):
                     userNameControl = lines[i].split(":")[1].strip()
                     if userNameControl== userNames:
                      userData=log.account_data_getter(userNames)       
                      userBalance=userData['balance']
                      userBalance-=inputBalance
                      line_to_update=i+4
                      newContent=f"Bakiye            : {userBalance}\n"
                      lines[line_to_update] = newContent
                      with open("accounts.txt", 'w',encoding='utf-8') as file:
                        file.writelines(lines)       
                   print("İşlem başarılı")
                   a=2
                   x=2
                 
        else :
            print("Kullanıcı adı bulunamadı lütfen yeniden deneyiniz")

def paraCekme(UserNames,balance):
    paraCekmetxt=f"---------------------------------------\nBakiyeniz: {balance}\n---------------------------------------\nÇekmek istediğiniz miktar: " 
    cekilenPara=float(input(paraCekmetxt))
    if cekilenPara>balance:
        print("Çekmek istediğiniz miktar bakiyenizden fazladır lütfen tekrar deneyiniz")
        input()
    else:
        guncelBalance=balance-cekilenPara
        with open("accounts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i in range(len(lines)):
         if lines[i].startswith("Kullanıcı adı"):
                userNameControl = lines[i].split(":")[1].strip()
                if userNameControl== UserNames:
                      line_to_update=i+4
                      newContent=f"Bakiye            : {guncelBalance}\n"
                      lines[line_to_update] = newContent
                      with open("accounts.txt", 'w',encoding='utf-8') as file:
                        file.writelines(lines)
                        print("İşem başarılı\n---------------------------------------")
                        input()       

def altinIslemleri(userNames,golds,balances):
    altinAlis=2743.565
    altinSatis=2742.954
    altinIslemtxt=f"---------------------------------------\nBakiyeniz: {balances} TL\nSahip olduğunuz Altın: {golds} gr\n---------------------------------------\n1-Altın Alış Fiyatı(gr): 2742,954 TL\n2-Altın Satış Fiyatı: 2743,565 TL\n---------------------------------------\n"
    goldChoice=int(input(altinIslemtxt))
    if goldChoice==1:
       goldAmount= float(input("---------------------------------------\nKaç gram Altın almak istersiniz: "))
       golds+=goldAmount
       balances-=altinAlis*goldAmount
       with open("accounts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
       for i in range(len(lines)):
         if lines[i].startswith("Kullanıcı adı"):
                userNameControl = lines[i].split(":")[1].strip()
                if userNameControl== userNames:
                      line_to_update=i+4
                      newContent=f"Bakiye            : {balances}\n"
                      line_to_update2=i+7
                      newContent2=f"Altın Gramı            : {golds}\n"
                      lines[line_to_update] = newContent
                      lines[line_to_update2]=newContent2
                      with open("accounts.txt", 'w',encoding='utf-8') as file:
                        file.writelines(lines)
                        print("İşem başarılı\n---------------------------------------")
                        input()  
    elif goldChoice==2:
       goldsellAmount= float(input("---------------------------------------\nKaç gram Altın satmak istersiniz: "))
       golds-=goldsellAmount
       balances+=goldsellAmount*altinSatis
       with open("accounts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
       for i in range(len(lines)):
         if lines[i].startswith("Kullanıcı adı"):
                userNameControl = lines[i].split(":")[1].strip()
                if userNameControl== userNames:
                      line_to_update=i+4
                      newContent=f"Bakiye            : {balances}\n"
                      line_to_update2=i+7
                      newContent2=f"Altın Gramı            : {golds}\n"
                      lines[line_to_update] = newContent
                      lines[line_to_update2]=newContent2
                      with open("accounts.txt", 'w',encoding='utf-8') as file:
                        file.writelines(lines)
                        print("İşem başarılı\n---------------------------------------")
                        input()  
             
def userInformation(userNames,FirstNames,LNames,EMail,PNumber,Sifre,balance,goldAmount):
    accounttxt = (f"---------------------------------------\n"
                      f"Kullanıcı adı     : {userNames}\n"
                      f"Şifre             : *********\n"
                      f"isim              : {FirstNames}\n"
                      f"Soyisim           : {LNames}\n"
                      f"Gmail             : {EMail}\n"
                      f"Telefon Numarası  : {PNumber}\n"
                      f"Bakiye :          : {balance}\n"
                      f"Altın Gramı       : {goldAmount}\n"
                      f"---------------------------------------\n")
    print(accounttxt)
    userChoice=int(input("1-Şifre Değiştirmek\n2-İsim Değiştirme\n3-Soyisim Değiştirme\n4-GMail değiştirme\n5-Telefon Numarası değiştirme\n6-Hesap silme\n7-Çıkış\n---------------------------------------"))
    x=0
    if userChoice==1:
     while x<1:
         
          passCheck=getpass("---------------------------------------\nÖncellikle lütfen mevcut şifrenizi giriniz: ")
          if passCheck==Sifre:
             a=0
             while a<1:
              newPassword=getpass("Lütfen yeni şifreyi giriniz: ")
              if newPassword==getpass("Lütfen yeni şifreyi yeniden giriniz"):
                  with open("accounts.txt", "r", encoding="utf-8") as f:
                   lines = f.readlines()
                  for i in range(len(lines)):
                    if lines[i].startswith("Kullanıcı adı"):
                       userNameControl = lines[i].split(":")[1].strip()
                       if userNameControl== userNames:
                         line_to_update=i+1
                         newContent=f"Şifre            : {newPassword}\n"
                         lines[line_to_update] = newContent
                         with open("accounts.txt", 'w',encoding='utf-8') as file:
                           file.writelines(lines)
                           getpass("İşlem başarı ile gerçekleşti\n")
                           
                           a=1
                           x=1
                           return False
                           
              else:
                  getpass("Şifreler birbiri ile uyuşmuyor lütfen yeniden deneyiniz")
          else:
                print("Girdiğiniz şifre hatalı lütfen yeniden deneyiniz")
    elif userChoice==2:
     while x<1:
        
          passCheck=getpass("Öncellikle lütfen mevcut şifrenizi giriniz: ")
          if passCheck==Sifre:
             a=0
             while a<1:
              newName=input("Lütfen yeni isimi giriniz: ")
              print("İsim başarılı bir şekilde değitirirdi")
              with open("accounts.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
              for i in range(len(lines)):
                    if lines[i].startswith("Kullanıcı adı"):
                       userNameControl = lines[i].split(":")[1].strip()
                       if userNameControl== userNames:
                         line_to_update=i+2
                         newContent=f"İlk İsim            : {newName}\n"
                         lines[line_to_update] = newContent
                         with open("accounts.txt", 'w',encoding='utf-8') as file:
                           file.writelines(lines)
                           a=1
                           x=1
                           getpass("İşlem başarı ile gerçekleşti")
                           return False
                           
          else:
                getpass("Şifre hatalı lütfen yeniden deneyiniz")    
    elif userChoice==3:
        while x<1:
        
          passCheck=getpass("Öncellikle lütfen mevcut şifrenizi giriniz: ")
          if passCheck==Sifre:
             a=0
             while a<1:
              newLName=input("Lütfen yeni Soy İsimi giriniz: ")
              print("Soy İsim başarılı bir şekilde değitirirdi")
              with open("accounts.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
              for i in range(len(lines)):
                    if lines[i].startswith("Kullanıcı adı"):
                       userNameControl = lines[i].split(":")[1].strip()
                       if userNameControl== userNames:
                         line_to_update=i+3
                         newContent=f"Soy İsim            : {newLName}\n"
                         lines[line_to_update] = newContent
                         with open("accounts.txt", 'w',encoding='utf-8') as file:
                           file.writelines(lines)
                           a=1
                           x=1
                           getpass("İşlem başarı ile gerçekleşti")
                           return False

          else:
                getpass("Şifre hatalı lütfen yeniden deneyiniz")    
    elif userChoice==4:
        while x<1:
        
          passCheck=getpass("Öncellikle lütfen mevcut şifrenizi giriniz: ")
          if passCheck==Sifre:
             a=0
             while a<1:
              newGMail=input("Lütfen yeni Gmaili giriniz: ")
              print("Soy Gmail bir şekilde değitirirdi")
              with open("accounts.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
              for i in range(len(lines)):
                    if lines[i].startswith("Kullanıcı adı"):
                       userNameControl = lines[i].split(":")[1].strip()
                       if userNameControl== userNames:
                         line_to_update=i+5
                         newContent=f"Gmail            : {newGMail}\n"
                         lines[line_to_update] = newContent
                         with open("accounts.txt", 'w',encoding='utf-8') as file:
                           file.writelines(lines)
                           a=1
                           x=1
                           getpass("İşlem başarı ile gerçekleşti")
                           return False
                           
          else:
                getpass("Şifre hatalı lütfen yeniden deneyiniz")    
    elif userChoice==5:
        while x<1:
        
          passCheck=getpass("Öncellikle lütfen mevcut şifrenizi giriniz: ")
          if passCheck==Sifre:
             a=0
             while a<1:
              newPNumber=input("Lütfen yeni Telefon numaranızı giriniz: ")
              print("Telefon Numarası başarılı bir şekilde değitirirdi")
              with open("accounts.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
              for i in range(len(lines)):
                    if lines[i].startswith("Kullanıcı adı"):
                       userNameControl = lines[i].split(":")[1].strip()
                       if userNameControl== userNames:
                         line_to_update=i+6
                         newContent=f"Telefon Numarası            : {newPNumber}\n"
                         lines[line_to_update] = newContent
                         with open("accounts.txt", 'w',encoding='utf-8') as file:
                           file.writelines(lines)
                           a=1
                           x=1
                           getpass("İşlem başarı ile gerçekleşti")
                           return False
          else:
                getpass("Şifre hatalı lütfen yeniden deneyiniz")
    elif userChoice==6:
     a=1
     while a>0:
         deleteaccpass=getpass("---------------------------------------\nLütfen şifreyi giriniz")
         if deleteaccpass==Sifre:   
          deletaccount= input("Hesabınızı silmek istediğinize emin misiniz?\nEğer Eminseniz lütfen EVET yazın: ")
          if deletaccount=="EVET":
             with open("accounts.txt", "r", encoding="utf-8") as f:
                 lines = f.readlines()
                 for i in range(len(lines)):
                     if lines[i].startswith("Kullanıcı adı"):
                        userNameControl = lines[i].split(":")[1].strip()
                        if userNameControl== userNames:
                          newContent=""
                          line_to_update=i-1
                          lines[line_to_update] = newContent
                          line_to_update=i
                          lines[line_to_update] = newContent
                          line_to_update=i+1
                          lines[line_to_update] = newContent
                          line_to_update=i+2
                          lines[line_to_update] = newContent
                          line_to_update=i+3
                          lines[line_to_update] = newContent
                          line_to_update=i+4
                          lines[line_to_update] = newContent
                          line_to_update=i+5
                          lines[line_to_update] = newContent
                          line_to_update=i+6
                          lines[line_to_update] = newContent
                          line_to_update=i+7
                          lines[line_to_update] = newContent
                          line_to_update=i+8                        
                          lines[line_to_update] = newContent
                          with open("accounts.txt", 'w',encoding='utf-8') as file:
                            file.writelines(lines)
                          input("Hesap başarılı bir şekilde silindi")
                          a=1
                          return True
         else:
            getpass("Şifre hatalı Lütfen yeniden deneyiniz")
            