from os import system
d_nama = []
d_nim = []
d_prodi = []
d_lulusan = []
d_bekerja = []

def ngopi_dulu():
    system('save')
    print()
    print('==========================================================')
    print('Input Data Karier Mahasiswa'.center(56))
    print('==========================================================')
    print('|           1. Tambah Data Karier Mahasiswa              |')
    print('|           2. Lihat Data Karier Mahasiswa               |')
    print('|           3. Keluar                                    |')
    print('==========================================================')
    pilih2 = (input('Pilih Menu : '))
    if pilih2 == '1':
        tambah()
    elif pilih2 == '2':
        lihat()
    elif pilih2 == '3':
        keluar()
    else:
        tidak = input('Menu Tidak Ada ')
        ngopi_dulu()

def tambah():
    system('save')
    print()
    print('==========================================================')
    print('Tambah Data'.center(56))
    print('==========================================================')
    nama = input('Nama  : ')
    d_nama.append(nama)
    nim = input('NIM  : ')
    d_nim.append(nim)
    prodi = input('Program Studi : ')
    d_prodi.append(prodi)
    lulusan = input('Lulusan Tahun : ')
    d_lulusan.append(lulusan)
    bekerja = input('Bekerja di : ')
    d_bekerja.append(bekerja)
    print ('<Data Tersimpan>'.center(56))
    kembali = input('Kembali [enter]')
    ngopi_dulu()

def lihat():
    system('save')
    print()
    print('==========================================================')
    print('Data Karier Mahasiswa'.center(56))
    print('==========================================================')
    for i in range (len(d_nim)):
        print('%d.  Nama            : %s'%(i+1, d_nama[i]))
        print('    NIM             : %s'%d_nim[i])
        print('    Program Studi   : %s'%d_prodi[i])
        print('    Lulusan Tahun   : %s'%d_lulusan[i])
        print('    Bekerja di      : %s'%d_bekerja[i])
        print('__________________________________________________________')
    kembali = input('Kembali Tekan [enter]')
    ngopi_dulu()
    
def keluar():
    system('save')
    exit()
    
ngopi_dulu()

