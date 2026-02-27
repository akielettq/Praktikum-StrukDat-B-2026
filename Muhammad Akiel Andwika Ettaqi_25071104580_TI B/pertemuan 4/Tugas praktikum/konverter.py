from kurs import kurs

def idr_ke_asing(jumlah, kode):  # Ini dari idr ke mata uang asing
    if kode not in kurs:
        return None
    return jumlah / kurs[kode]

def asing_ke_idr(jumlah, kode):  # Ini dari mata uang asing ke idr
    if kode not in kurs:
        return None
    return jumlah * kurs[kode]

def konversi(jumlah, dari, ke):  # Ini konversi umumnya
    if dari == 'IDR' and ke != 'IDR':
        return idr_ke_asing(jumlah, ke)
    elif dari != 'IDR' and ke == 'IDR':
        return asing_ke_idr(jumlah, dari)
    elif dari == ke:
        return jumlah
    else:
        dalam_idr = asing_ke_idr(jumlah, dari)  # Konversi mata uang asing ke asing lewat idr dlu
        return idr_ke_asing(dalam_idr, ke)
