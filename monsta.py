import main
from services import db_tamagoci

def alur_bertarung(nama, nama2):
    resultMonsta = db_tamagoci.bertarung_monsta(nama)
    resultMusuh = db_tamagoci.bertarung_musuh(nama2)
    if resultMonsta > resultMusuh:
        print("yeeeaayyy kamu menang")
    elif resultMonsta == resultMusuh:
        print("masih imbang nih")
    else:
        print("kamu kalah nih..")

def start():
    nama = input("nama monstamu: ")
    db_tamagoci.profil_monster(nama)
    nama = input("nama musuhmu: ")
    db_tamagoci.musuh(nama)
    while True: 
        menu = input("\nmenu : \n1. Status Monster \n2. Makan \n3. Latihan \n4. Extra \n5. Status Musuh \n6. Bertarung \n7. Kembali \n\nSilahkan : ")

        if menu == "1":
            nama = input("nama monstamu: ")
            db_tamagoci.status_monster(nama)
        elif menu == "2":
            nama = input("nama monstamu: ")
            db_tamagoci.makan(nama)
        elif menu == "3":
            nama = input("nama monstamu: ")
            db_tamagoci.latihan(nama)
        elif menu == "4":
            nama = input("nama monstamu: ")
            db_tamagoci.extra(nama)
        elif menu == "5":
            nama = input("nama musuh: ")
            db_tamagoci.status_musuh(nama)
        elif menu == "6":
            nama = input("nama monstamu: ")
            nama2 = input("nama musuh: ")
            alur_bertarung(nama, nama2)
        elif menu == "7":
            main.menu()
        else:
            break

if __name__ == "__main__":
    start()