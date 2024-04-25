from dotenv import dotenv_values
from mysql.connector import connect

params = {
    "db" : dotenv_values(".env")
}

db_user = params["db"]["MYSQL_USERNAME"]
db_password = params["db"]["MYSQL_PASSWORD"]
db_host = params["db"]["MYSQL_HOST"]
db_port = params["db"]["MYSQL_PORT"]
db_name = params["db"]["MYSQL_DB"]

db = connect(
    host = db_host,
    user = db_user,
    password = db_password,
    database = db_name
)

if db:
    print("loading to connect ...")
    print("connecting to database .....\n")


def profil_monster(nama):
    cursor = db.cursor()
    cursor.execute("INSERT INTO table_monsta (nama, power, strengh, stamina) VALUES (%s, %s, %s, %s)", (nama, 0, 0, 0))
    db.commit()
    print(f"\n'{nama}' telah lahir\n")

def makan(nama):
    cursor = db.cursor()
    cursor.execute("UPDATE table_monsta SET power = power + 10, strengh = strengh + 50, stamina = stamina + 50 WHERE nama = %s", (nama,))
    db.commit()
    print(f"\n{nama} kekuatanmu bertambah...!")

def status_monster(nama):
    cursor = db.cursor()
    cursor.execute("SELECT power, strengh, stamina FROM table_monsta WHERE nama = %s", (nama,))
    status = cursor.fetchone()
    print(f"""
    1. nama monsta : {nama} 
    2. power: {status[0]}, 
    3. strength: {status[1]}, 
    4. stamina: {status[2]}
""")
    
def musuh(nama):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tabel_enemy(nama, power, strengh, stamina) VALUES (%s, %s, %s, %s)", (nama, 1000, 1000, 2000))
    db.commit()

def status_musuh(nama:str):
    cursor = db.cursor()
    cursor.execute("SELECT power, strengh, stamina FROM tabel_enemy WHERE nama = %s", (nama,))
    status = cursor.fetchone()
    print(f"""
    1. nama musuh : {nama} 
    2. power: {status[0]}, 
    3. strength: {status[1]}, 
    4. stamina: {status[2]}
""")

def latihan(nama):
    cursor = db.cursor()
    cursor.execute("UPDATE table_monsta SET power = power * 2, strengh = strengh * 2, stamina = stamina - 20 WHERE nama = %s", (nama,))
    db.commit()
    print(f"\n{nama} kekuatanmu bertambah lagi...!")

def extra(nama):
    cursor = db.cursor()
    cursor.execute("UPDATE table_monsta SET power = power * 3, strengh = strengh * 3, stamina = stamina + 200 WHERE nama = %s", (nama,))
    db.commit()
    print(f"\n{nama} kekuatanmu bertambah lagi lagi...!")

def bertarung_monsta(nama):
    cursor = db.cursor()
    cursor.execute("SELECT power, strengh, stamina FROM table_monsta WHERE nama = %s", (nama,))
    monsta_stats = cursor.fetchone()
    return monsta_stats[0]

def bertarung_musuh(nama2):
    cursor = db.cursor()
    cursor.execute("SELECT power, strengh, stamina FROM tabel_enemy WHERE nama = %s", (nama2,))
    enemy_stats = cursor.fetchone()
    return enemy_stats[0]