import math

# luas segitiga
def luasSegitiga(tinggi, alas):
    hasil = (tinggi * alas) * 0.5
    print('luas segitiga dengan tinggi', tinggi,
            'dan alas', alas,
            'adalah', hasil)
# luas persegi
def luasPersegi(sisi):
    hasil = sisi * sisi
    print('luas persegi dengan sisi', sisi,
          'adalah', hasil)
# luas persegi panjang
def luasPersegiPanjang(panjang, lebar):
    hasil = panjang * lebar
    print('luas persegi dengan panjang', panjang,
            'dan lebar', lebar,
            'adalah', hasil)
# luas belah ketupat
def luasBelahKetupat(diagonal1, diagonal2):
    hasil = 0.5 * (diagonal1 * diagonal2)
    print('luas belah ketupat dengan diagonal 1 =', diagonal1,
    'dan diagonal 2 =', diagonal2,
    'adalah', hasil)
# luas jajar genjang
def luasJajarGenjang(alas,tinggi):
    hasil = alas * tinggi
    print('luas jajar genjang dengan alas',alas ,'dan tinggi',
            tinggi,'adalah',hasil)
          