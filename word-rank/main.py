sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

number_of_words = {}

for s in sentences:
    words = s.split(' ')
    for w in words:
        w = w.lower()
        if w not in number_of_words:
            number_of_words[w] = 1
        else:
            number_of_words[w] += 1

number_of_words = sorted(number_of_words.items(),key=lambda x:x[1],reverse=True)
for i in range(3):
    print(f'{i+1}. "{number_of_words[i][0]}" - {number_of_words[i][1]}')