import account
logged_in_user = None  
def loginPage():
 x =0
 while 1>x:
  print("---------------------------------------\nCity Banka Hoşgeldiniz\n---------------------------------------") 
  print("Giriş için-1\nKayıt için-2")
  logChoice= int(input())
  if logChoice==1:
    checker=account.login_account()
    if checker==2:
        print("Kullanıcı adı hatalı lütfen yeniden deneyiniz")
        input()
    elif checker==1:
        print("Şifre hatalı lütfen yeniden deneyiniz")
        input()
    elif checker==0:
        print("Başarılı bir şekilde giri yaptınız")
        input()
        x=2
  if logChoice==2:
    account.create_account()



def mainPage():
    user_data = account.account_data_getter()  # This will now correctly reference the logged_in_user
    
    if user_data is None:
        print("Kullanıcı bilgileri bulunamadı.")
        return
    
    userName = user_data['username']
    userBalance = user_data['balance']
    userGold = user_data['gold']
    
    textAccount = f"""
    ---------------------------------------
    Bankamıza Hoşgeldiniz
    ---------------------------------------
    Kullanıcı Adı        : {userName}
    Bakiye               : {userBalance} TL
    Bakiye (USD)         : {userBalance / 33} $
    Altın (gram)         : {userGold} gr
    ---------------------------------------
    1- Para Gönderme
    2- Para Çekme
    3- Altın Alma
    4- Kullanıcı Bilgileri Görüntüleme
    5- Çıkış Yapma
    ---------------------------------------
    """
    input(textAccount)