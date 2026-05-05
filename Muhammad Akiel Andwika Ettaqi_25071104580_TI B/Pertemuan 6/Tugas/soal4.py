level_diskon = (
 (500000, 15), # belanja >= 500.000 -> diskon 15%
 (300000, 10), # belanja >= 300.000 -> diskon 10%
 (100000, 5), # belanja >= 100.000 -> diskon 5%
 (0, 0), # default -> tidak ada diskon
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    if total_belanja >= 500000:
        return "Anda mendapatkan diskon 15%"
    elif total_belanja >= 300000:
        return "Anda mendapatkan diskon 10%"
    elif total_belanja >= 100000:
        return "Anda mendapatkan diskon 5%"
    else:
        return "Anda tidak mendapatkan diskon"