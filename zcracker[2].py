import zipfile

def is_passwd_correct(password, zip_path):
    with zipfile.ZipFile(zip_path) as zf:
        try:
            for name in zf.namelist():
                zf.read(name, pwd=str(password).encode())
            return True
        except:
            return False

zip_path = input("Enter zip file path: ")

for password in range(10000):
    if is_passwd_correct(password, zip_path):
        print("Password found:", password)
        break
