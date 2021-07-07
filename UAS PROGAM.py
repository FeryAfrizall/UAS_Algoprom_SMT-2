# -*- coding: utf-8 -*-
"""
UAS ALGORITMA PEMROGAMAN
@author: hp
"""
#set tanggal sama dengan tanggal sekarang
import datetime
tanggal = datetime.date.today()

#Perulangan untuk mengulang program
jwb = 'y'
while jwb == 'y':
    
    #List
    List_kode_golongan = [1,2,3]
    List_golongan = ['Golongan 1','Golongan 2','Golongan 3']
    List_gajipokok = [2500000,4500000,6500000]

    #Tampilan Interfaces
    print("===========================================")
    print("\t SLIP GAJI KARYAWAN CV.LOGOS")
    print("\t Tanggal : ",tanggal)
    print("===========================================")
    
    #tampilkan list menggunakan perulangan
    idx = 0
    print("Kode ","\t Golongan ", "\t \t Gaji Pokok ")
    while idx < len(List_kode_golongan) :
        print(str(List_kode_golongan[idx]) + "\t" + "\t" + List_golongan[idx] + " \t \t Rp." + str(format(List_gajipokok[idx],',.2f'))) 
        idx = idx + 1
        
    #Inputan Nama dan golongan
    print("===========================================")
    input_Nama = input("\n> Masukkan Nama Pegawai : ")
    input_Golongan = int(input("> Masukkan Golongan Pegawai (1-3): "))

    #validasi inputan golongan tidak boleh lebih dari 3
    while input_Golongan > 3 or input_Golongan < 1 :
        sts = "\n !WARNING  Inputan Golongan Pegawai hanya boleh 1 sampai 3 "
        print(sts)
        input_Golongan = int(input("> Masukkan Golongan Pegawai (1-3) : "))  

    #Inputan Jenis Kelamin 
    input_jenisKelamin = input("> Masukkan Jenis Kelamin Pegawai (Laki Laki / Perempuan) : ")
    input_jenisKelamin = input_jenisKelamin.lower()

    #validasi inputan jenis kelamin hanya boleh laki-laki dan perempuan
    while input_jenisKelamin != "laki laki" and input_jenisKelamin != "perempuan" :
        sts = "\n !WARNING  Inputan jenis kelamin hanya boleh laki-laki dan perempuan "
        print(sts)
        input_jenisKelamin = input("> Masukkan Jenis Kelamin Pegawai (Laki Laki / Perempuan): ")
        input_jenisKelamin = input_jenisKelamin.lower()

    #inputan status kawin
    input_statusKawin = input("> Masukkan Status Kawin Pegawai (Kawin / Belum Kawin) : ") 
    input_statusKawin = input_statusKawin.lower()

    #validasi inputan status kawin hanya boleh kawin dan belum kawin
    while input_statusKawin != "kawin" and input_statusKawin != "belum kawin":
        sts = "\n !WARNING  Inputan status kawin hanya boleh kawin dan belum kawin "
        print(sts)
        input_statusKawin = input("> Masukkan Status Kawin Pegawai (Kawin / Belum Kawin) : ") 
        input_statusKawin = input_statusKawin.lower()
            
    # jika status kawin = kawin maka tampilkan inputan punya anak
    if input_statusKawin == "kawin":
                
        #inputan punya anak
        input_PunyaAnak = input("> Masukkan Punya Anak atau Belum Punya Anak (Punya Anak / Belum Punya Anak): ")
        input_PunyaAnak = input_PunyaAnak.lower() 
                
        #validasi inputan punya anak hanya boleh punya anak dan belum punya anak
        while input_PunyaAnak != "punya anak" and input_PunyaAnak != "belum punya anak":
            sts = "\n !WARNING  Inputan punya anak hanya boleh punya anak dan belum punya anak "
            print(sts)
            input_PunyaAnak = input("> Masukkan Punya Anak atau Belum Punya Anak : ")
            input_PunyaAnak = input_PunyaAnak.lower() 
    else :
        pass

    #baca berulang idx didalam list golongan
    #jika value idx list golongan sama dengan value pilihan
    #ambil indexnya
    idx = 0
    while idx < len(List_golongan):
        if List_kode_golongan[idx] == input_Golongan :
            gajipokok = List_gajipokok[idx]
            gol = List_golongan[idx]
        idx = idx + 1

    #Tampilkan Data Pegawai
    print("================================================")
    print("\t \t \t DATA PEGAWAI")
    print("================================================")
    print("Nama          = " + input_Nama)
    print("Status        = " + input_statusKawin)
    print("Golongan      = " + gol)
    print("Jenis kelamin = " + input_jenisKelamin)
    print("Gaji Pokok    = Rp." + str(format(gajipokok,',.2f')))

    #jika jenis kelamin laki-laki dan sudah kawin akan dapat tunjangan istri
    if input_statusKawin == "kawin":
        #Tunjangan Istri
        if input_jenisKelamin == "laki laki" and input_statusKawin == "kawin":
            if input_Golongan == 1 :
                tunjanganIstri = 0.01 * gajipokok
            elif input_Golongan == 2 :
                tunjanganIstri = 0.03 * gajipokok
            elif input_Golongan == 3 :
                tunjanganIstri = 0.05 * gajipokok
        else :
            tunjanganIstri = 0
            
        #Tunjangan Anak
        if input_PunyaAnak == "punya anak" and input_statusKawin == "kawin":
            tunjanganAnak = 0.02 * gajipokok
        elif input_PunyaAnak == "belum punya anak" and input_statusKawin == "kawin":
            tunjanganAnak = 0
    #jika belum kawin mana tidak dapat tunjangan istri dan tunjangan anak   
    elif input_statusKawin == "belum kawin" :
        tunjanganAnak = 0
        tunjanganIstri = 0

    #Tampilkan tunjagan istri dan tunjangan anak    
    print("\nTunjangan Istri = Rp." + str(format(tunjanganIstri,',.2f')))
    print("Tunjangan Anak    = Rp." + str(format(tunjanganAnak,',.2f')))

    #Gaji Bruto
    if input_statusKawin == "kawin" and input_PunyaAnak == "punya anak": 
        gajibruto = gajipokok + tunjanganAnak + tunjanganIstri
        
    elif input_statusKawin == "kawin" and input_PunyaAnak == "belum punya anak":
        gajibruto = gajipokok + tunjanganIstri

    else :
        gajibruto = gajipokok
        
    #Biaya jabatan
    biayajabatan = 0.005 * gajibruto

    #iuran pensiun
    iuranpensiun =  15500

    #iuran organisasi
    iuranorganisasi = 3500

    #gaji Netto
    gajinetto = gajibruto - biayajabatan - iuranpensiun - iuranorganisasi

    #tampilkan Rincian Gaji
    print("=========================================")
    print("\t \t Rincian Slip Gaji")
    print("=========================================")
    print("> Gaji Bruto        = Rp." + format(gajibruto,',.2f'))
    print("> Biaya Jabatan     = Rp." + format(biayajabatan,',.2f'))
    print("> Iuran Organisasi  = Rp." + format(iuranorganisasi,',.2f'))
    print("> Iuran Pensiun     = Rp." + format(iuranpensiun,',.2f'))
    print("> Gaji Netto        = Rp." + format(gajinetto,',.2f'))
    
    #pertanyaan apakah ingin mengulang program
    jwb = input("\nHitung lagi ? (y/t) : ")
    jwb = jwb.lower()
    
        #validasi inputan jawab hanya boleh y/t
    while jwb != 'y' and jwb != 't':
        sts = "\n !WARNING  Inputan jawab hanya boleh y dan t "
        print(sts)
        jwb = input("\nHitung lagi ? (y/t) : ")
        
        #jika jawab = t maka program akan berakhir    
    if jwb == "t":
        break
print("\n==== PROGRAM TELAH BERAKHIR ====\n")