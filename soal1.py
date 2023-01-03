while True:
    print('****** Kredit Keaktifan Mahasiswa ******')
    print('(Student Activities Credit)')
    print('1. Menambahkan Kegiatan')
    print('2. Menampilkan Jumlah Poin')
    print('3. Keluar')
    print('---------------------------------') 
    pil = int(input('Silahkan masukkan pilihan yang Anda:'))
    if pil==1:
        NK = input('Nama Kegiatan:')
        TG = int(input('Tanggal Kegiatan:'))
        print('Pilihan Kategori Kegiatan:')
        print('- Prestasi')
        print('- Organisasi')
        print('- Kepanitiaan')
        print('- Rekognisi')
        PKK = input('Masukkan Kategori Kegiatan:')
        print('Kegiatan berhasil ditambahkan')
        def a():
            print(NK,'  ',   TG,'   ',     PKK,'    ',    )
    elif pil==2:
        print('Nama Kegiatan    Tanggal     Kategori    Poin')
        a()
    elif pil==3:
        print('Sistem Berhenti...')
    else:
        print('Input yang Anda berikan salah')