#seçilen jpeg dosyası bozar ve tekrar düzeltir.


import binascii
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
import random



def browse_file(entry_var):
    file_path = filedialog.askopenfilename()
    entry_var.set(file_path)

def hex_viewer(filePath):
    
    try:
        
        
        with open(filePath, 'rb') as file:
            # Dosyanın tamamını oku
            file_content = file.read()

            # Dosyanın hex temsilini al ve ekrana yazdır
            hex_representation = binascii.hexlify(file_content).decode('utf-8')
            return hex_representation
            

    except FileNotFoundError:
        messagebox.showerror("Hata", f"Dosya bulunamadı: {file_path}")
    except Exception as e:
        messagebox.showerror("Hata", f"Hata oluştu: {e}")




def diziyi_donusttur_dosyaya(broken_hex,file_path):

    

    # Hexadecimal veriyi ikili (binary) veriye çevir
    binary_veri = binascii.unhexlify(broken_hex)

        # JPEG dosyasını oluştur ve ikili veriyi yaz
    with open(file_path, "wb") as dosya:
        dosya.write(binary_veri)


def jpeg_crypt():
    #Bu imza, dosyanın ilk iki byte'ında bulunur.
    #Eğer bir dosyanın ilk iki byte'ı "FF D8" ise, bu dosyanın JPEG formatında olduğunu söyleyebiliriz.
    #Bu fonksiyon dosyanın ilk iki bytını sil
    #dosyanın en başına gel 5 byte ekle (10tane karakter yani)
    #bu 10 bytı rastgele hex karakterleri ile doldur 


    # Hex viewer fonksiyonunu kullanarak dosyanın hex temsilini al
    file_path = file_var.get()
    hex_representation = hex_viewer(file_path)
    
    
    # İlk iki byte'ı sil
    hex_representation = hex_representation[4:]

    # Dosyanın en başına gel ve 5 byte   rastgele hex karakteri  ekle
    hex_liste=["a", "b", "c", "d", "e" , "f","0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
      
    rastgele_karakterler = random.sample(hex_liste, 10)

    # Seçilen karakterleri birleştirerek 10 basamaklı bir karakter oluştur
    rastgele_karakterler_str = ''.join(rastgele_karakterler)

    # Dosyanın en başına  5 byte   rastgele hex karakteri  ekle 
    hex_representation = rastgele_karakterler_str  + hex_representation


    diziyi_donusttur_dosyaya(hex_representation,file_path)

    


def jpeg_encrypt():
    #hex kodunun ilk 10 karakteri sil
    #hexin başına "FF D8" yaz
    
    # Hex viewer fonksiyonunu kullanarak dosyanın hex temsilini al
    file_path = file_var.get()
    
    hex_representation = hex_viewer(file_path)


    # Hex kodunun ilk 10 karakterini sil
    hex_representation = hex_representation[10:]
    
    # Hex'in başına "FFD8" ekle
    hex_representation = "ffd8" + hex_representation
    
    # Yeni dosyayı oluştur
    diziyi_donusttur_dosyaya(hex_representation,file_path)

# Hex görüntüleme fonksiyonunu çağır
#hex_viewer(dosya_yolu)



#Arayüz
# Ana pencereyi oluştur
root = tk.Tk()
root.title("jpeg broken")

# Pencere boyutlarını ayarla (genişlik x yükseklik)
root.geometry("900x600")
# Pencerenin boyutlarını sabit yap
root.resizable(width=False, height=False)


# Arka plan rengini ayarla
root.configure(bg="#f0f0f0")

# Değişkenler
file_var = tk.StringVar()
NewFileName = tk.StringVar()


# Kullanıcıdan dosya yolunu al
file_label = tk.Label(root, text="Dosya Seçin:", font=("Helvetica", 12), bg="#f0f0f0")
file_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_file = tk.Entry(root, textvariable=file_var, state="disabled", width=40)
entry_file.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

browse_button = tk.Button(root, text="Gözat", command=lambda: browse_file(file_var))
browse_button.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)


#jpeg şifreleme işlem butonu

run_button = tk.Button(root, text="encrypt", command=jpeg_crypt, bg="#4CAF50", fg="white")
run_button.grid(row=1, column=3, columnspan=4, pady=10 ,padx=30)


#jpeg deşifreleme işlem butonu 

encrypt_button = tk.Button(root, text="decrypt", command=jpeg_encrypt, bg="#ff0000", fg="white")
encrypt_button.grid(row=1, column=10, columnspan=4, pady=10 ,padx=30)




#Penceereyi göster
root.mainloop()
