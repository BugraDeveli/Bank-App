class Person1():
    def __init__(self, userName, password, firstName, lastName, balance, email, phone, gold) -> None:
        self.userName = userName
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance
        self.email = email
        self.phone = phone
        self.gold = gold
userNameCheck ="bugra"
def is_username_unique(user_name):
    """Verilen kullanıcı adının benzersiz olup olmadığını kontrol eder."""
    with open("accounts.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines:
        if line.startswith("Kullanıcı adı"):
            current_user_name = line.split(":")[1].strip()
            if current_user_name == user_name:
                return False
    return True

def create_account():
    print("---------------------------------------")
    print("Kullanıcı Bilgileri Girişi")
    print("---------------------------------------")

    # Kullanıcıdan bilgileri al
    while True:
        userN = input("Kullanıcı adı belirleyiniz: ")
        if is_username_unique(userN):
            break
        else:
            print("Bu kullanıcı adı zaten alınmış. Lütfen farklı bir kullanıcı adı seçin.")

    password = input("Şifre belirleyiniz: ")
    firstName = input("İlk isminizi giriniz: ")
    lastName = input("Soyadınızı giriniz: ")
    balance = input("Başlangıç bakiyenizi giriniz: ")
    email = input("Gmail adresinizi giriniz: ")
    phone = input("Telefon numaranızı giriniz: ")
    gold = input("Altın gramınızı giriniz: ")

    # Bilgileri düzgün bir formatta yazdırma
    print("\n---------------------------------------")
    print(f"Kullanıcı Adı      : {userN}")
    print(f"Şifre              : {password}")
    print(f"İlk İsim           : {firstName}")
    print(f"Soyisim            : {lastName}")
    print(f"Başlangıç Bakiyesi : {balance}")
    print(f"Gmail              : {email}")
    print(f"Telefon Numarası   : {phone}")
    print(f"Altın Gramu        : {gold}")
    print("---------------------------------------")
    
    # Kullanıcı bilgilerini dosyaya yazma
    with open("accounts.txt", "a", encoding='utf-8') as f:
        accounttxt = (f"---------------------------------------\n"
                      f"Kullanıcı adı     : {userN}\n"
                      f"Şifre             : {password}\n"
                      f"İlk isim          : {firstName}\n"
                      f"Soyisim           : {lastName}\n"
                      f"Başlangıç Bakiyesi : {balance}\n"
                      f"Gmail              : {email}\n"
                      f"Telefon Numarası   : {phone}\n"
                      f"Altın Gramu        : {gold}\n"
                      f"---------------------------------------\n")
        f.write(accounttxt)

    print("Hesap başarıyla oluşturuldu!")
    
def login_account():
    user_found = False
    with open("accounts.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    userNameCheck = input("Lütfen Kullanıcı adını giriniz: ")

    for i in range(len(lines)):
        if lines[i].startswith("Kullanıcı adı"):
            userNameControl = lines[i].split(":")[1].strip()
            if userNameCheck == userNameControl:
                user_found = True
                passwordcheck = input("Lütfen şifrenizi giriniz: ")
                # Kullanıcı adı doğru ise, bir sonraki satırda şifreyi kontrol et
                if lines[i+1].startswith("Şifre"):
                    passwordControl = lines[i+1].split(":")[1].strip()
                    if passwordcheck == passwordControl:
                        print("Giriş başarılı!")
                        return 0  # Giriş başarılı
                    else:
                        print("Hatalı şifre!")
                        return 1  # Hatalı şifre

    if not user_found:
        print("Kullanıcı adı bulunamadı!")
        return 2  # Kullanıcı adı bulunamadı

from loginModule import logged_in_user  # Import the variable

def account_data_getter():
    global logged_in_user
    userNameCheck = logged_in_user  # Use the stored username
    
    with open("accounts.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    user_data = {}
    for i in range(len(lines)):
        if lines[i].startswith("Kullanıcı adı"):
            userNameControl = lines[i].split(":")[1].strip()
            if userNameCheck == userNameControl:
                # If user is found, get all related information
                user_data['username'] = userNameControl
                user_data['password'] = lines[i+1].split(":")[1].strip()
                user_data['firstName'] = lines[i+2].split(":")[1].strip()
                user_data['lastName'] = lines[i+3].split(":")[1].strip()
                user_data['balance'] = float(lines[i+4].split(":")[1].strip())
                user_data['gmail'] = lines[i+5].split(":")[1].strip()
                user_data['phone'] = lines[i+6].split(":")[1].strip()
                user_data['gold'] = float(lines[i+7].split(":")[1].strip())
                return user_data
    
    # If the loop completes and no user is found
    return None