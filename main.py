import logModule as log
import moneyIslem as mon
from getpass import getpass
with open("accounts.txt","a", encoding='utf-8') as f:
    pass
x=0
while x<1:
    textAccount = f"""
             ---------------------------------------
                    Garanti Banka Hoşgeldiniz
             ---------------------------------------
             1-Giriş Yap
             2-Kayıt ol
             ---------------------------------------
             """
    choice=int(input(textAccount))
    if choice== 1:
     global userName
     userName=input("Lütfen Kullanıcı adını giriniz:")
     checkLog=log.login(userName)
     if checkLog==0:
         input()
         deletedAccount=False
         i=0
         while i<1:
             if deletedAccount ==False:
              userData=log.account_data_getter(userName)        
              userName = userData['username']
              userBalance = userData['balance']
              userGold = userData['gold']
              userFName=userData['firstName']
              userLName=userData['lastName']
              userGmail=userData['gmail']
              userPNumber=userData['phone']
              userPassword=userData['password']
              
              
              textAccount = f"""
              ---------------------------------------
                           {userFName} {userLName}
              ---------------------------------------
              Kullanıcı Adı        : {userName}
              Bakiye               : {userBalance} TL
              Bakiye (USD)         : {userBalance / 33:.2f} $
              Altın (gram)         : {userGold} gr
              ---------------------------------------
              1- Para Yatırma
              2- Para Gönderme
              3- Para Çekme
              4- Altın Alma
              5- Kullanıcı Bilgileri Görüntüleme
              6- Çıkış Yapma
              ---------------------------------------
              """
              moneyChoice=int(input(textAccount))
              if moneyChoice==1:
                  mon.paraYatirma(userName,userBalance)
              elif moneyChoice==2:
                  mon.paraGonderme(userName,userBalance)
              elif moneyChoice==3:
                 mon.paraCekme(userName,userBalance)
              elif moneyChoice==4:
                  mon.altinIslemleri(userName,userGold,userBalance)
              elif moneyChoice==5:
                  deletedAccount=mon.userInformation(userName,userFName,userLName,userGmail,userPNumber,userPassword,userBalance,userGold)
              elif moneyChoice==6:
                  print("Çıkış Yapılıyor iyi günler")
                  input()
                  i=1
             elif deletedAccount==True:
                 getpass("Bu hesap silinmiştir lütfen başka bir hesap ile giriş yapınız")
                 i=1
     elif checkLog==1:
         print("Şifre Hatalı")
         input()
     else:
         print("Kullanıcı adı hatalı")
         input()
    if choice==2:
        log.createAccount()
        input()

        
    
