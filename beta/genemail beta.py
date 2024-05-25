import random
import string

def generate_email():
    # Daftar domain email yang mungkin digunakan
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]

    # Menghasilkan nama acak dengan panjang 8 karakter
    name = ''.join(random.choices(string.ascii_lowercase, k=8))

    # Memilih domain email secara acak dari daftar yang ada
    domain = random.choice(domains)

    # Menggabungkan nama dan domain untuk membentuk alamat email
    email = f"{name}@{domain}"

    return email

def generate_password(length=12):
    # Karakter yang mungkin digunakan dalam kata sandi
    characters = string.ascii_letters + string.digits + string.punctuation

    # Menghasilkan kata sandi acak dengan panjang yang ditentukan
    password = ''.join(random.choices(characters, k=length))

    return password

# Contoh penggunaan fungsi generate_email() dan generate_password()
email = generate_email()
password = generate_password()

print(f"Email: {email}")
print(f"Password: {password}")

input("Press Enter to exit...")
