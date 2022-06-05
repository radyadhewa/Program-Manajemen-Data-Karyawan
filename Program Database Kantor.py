import os

# membuat class sebagai penyimpan data utama karyawan nantinya


class Employee:
    Nama = ''
    Jabatan = ''
    Gaji = []
    Usia = ''
    Email = ''
    Domisili = ''
    Kelamin = []


# membuat variable penyimpan data yang bersifat global karena digunakan dalam berbagai fungsi
uname = ''
pswrd = ''
total = 0
gaji = 0
dataEmployee = []

# fungsi yang akan digunakan untuk menunjukkan database yang telah dibuat diatas


def show():
    x = 0
    print("\nData Karyawan")
    for data in dataEmployee:
        x += 1
        print(f"\n------------- Profil Karyawan ke-{x} -----------------")
        print("Nama\t\t: "+data.Nama.title())
        print("Jabatan\t\t: "+data.Jabatan.title())
        res = "{:,.2f}".format(data.Gaji)
        print(f"Gaji\t\t: Rp {res}")
        print("Usia\t\t: "+str(data.Usia))
        print("Email\t\t: "+data.Email)
        print("Domisili\t: "+data.Domisili.title())
        print("Kelamin\t\t: "+data.Kelamin.title())
        print("-----------------------------------------------------")

# fungsi untuk menambahkan data baru


def registerEmployee():
    os.system('cls')
    print('== Aktifkan karyawan baru ==')
    enough = True
    global total
    while(enough):
        newEmployee = Employee()
        newEmployee.Nama = input("\nMasukkan Nama Karyawan Baru\t: ")
        newEmployee.Jabatan = input("Masukkan Jabatan Karyawan Baru\t: ")
        while True:
            try:
                newEmployee.Gaji = int(
                    input("Masukkan Gaji Karyawan Baru\t: "))
                if newEmployee.Gaji == '':
                    print('Masukkan Gaji Karyawan Baru\t: ')
            except ValueError:
                print(' Masukan Gaji dengan angka saja')
            else:
                Employee.Gaji.append(newEmployee.Gaji)
                break
        while True:
            try:
                newEmployee.Usia = int(
                    input("Masukkan Usia Karyawan Baru\t: "))
                if newEmployee.Usia == '':
                    print('Masukkan Usia Karyawan Baru\t: ')
            except ValueError:
                print(' Masukkan Usia dengan angka saja')
            else:
                break
        newEmployee.Email = input("Masukkan Email Karyawan Baru\t: ")
        newEmployee.Domisili = input("Masukkan Domisili Karyawan Baru\t: ")
        newEmployee.Kelamin = input("Masukkan Jenis Kelamin\t\t: ")
        Employee.Kelamin.append(newEmployee.Kelamin)
        dataEmployee.append(newEmployee)
        total += 1
        add = input('Apakah ingin menambah karyawan lagi (y/n) ?\t: ')
        if add == 'n':
            enough = False

# fungsi untuk menghapus sebuah data


def unemployed():
    os.system('cls')
    print('== Nonaktifkan Karyawan ==')
    global total
    global gaji
    if dataEmployee != []:
        show()
        index_delete = -1
        id_delete = input(
            "\nMasukkan nama karyawan yang ingin dinonaktifkan: ")
        for a in range(0, len(dataEmployee)):
            if id_delete == dataEmployee[a].Nama:
                index_delete = a
                break
        if(index_delete > -1):
            Employee.Gaji.pop(index_delete)
            Employee.Kelamin.pop(index_delete)
            del dataEmployee[index_delete]
            total -= 1
            print(
                f"\nkaryawan atas nama {(id_delete).title()} telah dinonaktifkan")
            input("tekan 'enter' untuk melanjutkan")
        else:
            print("\nNama tidak ditemukan")
            input("tekan 'enter' untuk melanjutkan")
    else:
        print("\nData anda masih kosong, yuk isi data terlebih dahulu!")
        input("tekan 'enter' untuk melanjutkan")

# fungsi untuk mengedit isi data


def updateData():
    os.system('cls')
    print('== Perbarui Data Karyawan ==')
    index_update = -1
    if dataEmployee != []:
        show()
        id_edit = input(
            "\nMasukkan nama karyawan yang datanya akan diupdate: ")
        for a in range(0, len(dataEmployee)):
            if id_edit == dataEmployee[a].Nama:
                index_update = a
                break
        if(index_update > -1):
            print("Input data terbaru")
            newEmployee = Employee()
            newEmployee.Nama = input("\nMasukkan Nama Karyawan Baru\t: ")
            newEmployee.Jabatan = input("Masukkan Jabatan Karyawan Baru\t: ")
            while True:
                try:
                    newEmployee.Gaji = int(
                        input("Masukkan Gaji Karyawan Baru\t: "))
                    if newEmployee.Gaji == '':
                        print('Masukkan Gaji Karyawan Baru\t: ')
                except ValueError:
                    print(' Masukan Gaji dengan angka saja')
                else:
                    Employee.Gaji[index_update] = newEmployee.Gaji
                    break
            newEmployee.Usia = int(input("Masukkan Usia Karyawan Baru\t: "))
            newEmployee.Email = input("Masukkan Email Karyawan Baru\t: ")
            newEmployee.Domisili = input("Masukkan Domisili Karyawan Baru\t: ")
            newEmployee.Kelamin = input("Masukkan Jenis Kelamin\t\t: ")
            Employee.Kelamin[index_update] = newEmployee.Kelamin
            dataEmployee[index_update] = newEmployee
            print(
                f"\nData karyawan atas nama {(id_edit).title()} berhasil di update!")
            input("tekan 'enter' untuk melanjutkan")
        else:
            print("\nNama tidak ditemukan")
            input("tekan 'enter' untuk melanjutkan")
    else:
        print("\nData anda masih kosong, yuk isi data terlebih dahulu!")
        input("tekan 'enter' untuk melanjutkan")

# fungsi untuk menampilkan data beserta rekapitulasinya


def tampilData():
    os.system('cls')
    print('== Rekap Data Karyawan ==')
    employ = Employee()
    print('\nTotal karyawan dalam perusahaan\t\t\t\t: ', total)
    uang = sum(employ.Gaji)
    res = "{:,.2f}".format(uang)
    print(f'Total gaji yang harus dibayar oleh perusahaan adalah\t: Rp {res}')
    print('Total karyawan pria ada\t\t\t\t\t: ', employ.Kelamin.count('pria'))
    print('Total karyawan wanita ada\t\t\t\t: ',
          employ.Kelamin.count('wanita'))
    if dataEmployee != []:
        show()
        input("tekan 'enter' untuk melanjutkan")
    else:
        print("\nData anda masih kosong, yuk isi data terlebih dahulu!")
        input("tekan 'enter' untuk melanjutkan")

# fungsi untuk mengeluarkan tampilan menu


def menu():
    os.system('cls')
    print(f"==== DATABASE KARYAWAN {uname.upper()} ====\n")
    print("Pilihan Menu Program: ")
    print("1. Aktifkan karyawan baru")
    print("2. Nonaktifkan karyawan")
    print("3. Edit data karyawan")
    print("4. Tampilkan rekapitulasi data secara keseluruhan")
    print("0. Exit\n")

# fungsi untuk looping program


def startProgram():
    while True:
        menu()
        choice = int(input('Masukkan pilihan menu yang diinginkan: '))
        if choice == 0:
            frontpage()
        elif choice == 1:
            registerEmployee()
        elif choice == 2:
            unemployed()
        elif choice == 3:
            updateData()
        elif choice == 4:
            tampilData()
        else:
            print('Maaf menu tidak tersedia')

# fungsi animasi loading screen


def loading():
    os.system('cls')
    import time
    import sys
    print("Loading:")

    animation = ["[●○○○○○○○○○]", "[●●○○○○○○○○]", "[●●●○○○○○○○]", "[●●●●○○○○○○]", "[●●●●●○○○○○]",
                 "[●●●●●●○○○○]", "[●●●●●●●○○○]", "[●●●●●●●●○○]", "[●●●●●●●●●○]", "[●●●●●●●●●●]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")
    os.system('cls')

# fungsi untuk menginisasi halaman awal login atau sign up page


def frontpage():
    os.system('cls')
    global uname
    global pswrd
    print('=== Selamat datang di sistem database karyawan ===\n')
    print(('Silahkan ketik "login" atau "sign up" jika baru pertama kali menggunakan'))
    first = input('Pilihan anda: ')
    while True:
        if first.lower() == 'sign up':
            os.system('cls')
            print('Silahkan mendaftarkan username dan password')
            username = input(
                '\nMasukkan username yang akan digunakan perusahaan\t: ')
            password = input(
                'Masukkan password yang akan digunakan oleh perusahaan\t: ')
            uname = username
            pswrd = password
            print('username dan password telah tersimpan')
            input('pencet "enter" untuk melanjutkan')
            os.system('cls')
            print('Silahkan langsung ketik "login"')
            first = input('\nPilihan anda: ')
        elif first.lower() == 'login':
            os.system('cls')
            print('Silahkan login')
            user = input('\nUsername\t: ')
            pw = input('Password\t: ')
            if user == uname and pw == pswrd:
                loading()
                startProgram()
            else:
                loading()
                print('\nMaaf username dan password tidak cocok')
                print(
                    '\nsilahkan klik "login" untuk mencoba ulang atau "reset" jika lupa username dan password namun data akan hilang')
                first = input('Pilihan anda: ')
        elif first.lower() == 'reset':
            os.system('cls')
            uname = ''
            pswrd = ''
            print(
                '\nData username dan password telah dihapus, sekarang silahkan mulai dari sign up!')
            first = input('Pilihan anda: ')
        else:
            print('maaf command salah')
            first = input('Pilihan anda: ')


# memanggil fungsi untuk menjalankan program
frontpage()
