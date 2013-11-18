
# Na poprzednich zajechac poznalismy 3 typy elementow
# jezyka Python umozliwiajace wybor ktore elementy naszego
# programu zostana wykonane/ile razy zostana wykonane.

# Byly nimi instrukcja if:
# b=dzielną
# a=dzielnik
# if( a!=0 ) 
#	print b/a
# else
#	print "nie dzielimy przez 0"
#
# Instrukcja if pozwala nam tworzyc wykonywac blok kodu
# gdy dany warunek jest spelniony, a inny gdy spelniony jest 
# inny warunek.
#
#
# Kolejnymi były instrukcje: while oraz for:
# 
n=4
silnia=1
while(n>0):
   silnia=silnia*n
   n-=1
 print silnia
#
 n=4
 silnia=1
 for i in xrange(1,n+1):
     silnia*=i
 print silnia
#
#
# Sluza do powtarzania tego samego bloku kodu
# podczas gdy zmienne na ktorych tenze kod pracuje
# ulegaja zmianie.
#
#
# Gdybysmy nie posiadali instrukcji if
# musielibysmy np. pisac 2 rozne programy
# jeden na wypadek gdy dostajemy dzielnik=0
# drugi gdy mozemy ladnie podzielic.
# 
# Gdybysmy nie posiadali petli, musielibysmy przekopiowac
# ten blok wykonujacy sie obecnie w petli, tyle razy
# ile chcielibysmy by petla sie wykonala.
# 
# Generalnie, zle niewygodnie i cieszymy sie z if-ow i petli.
# 
# Programista nie mniej, bestia leniwa i poszedl dalej.
# Zalozmy ze w naszym programie musimy czesto liczyc silnie.
# Jak widac z przykladow wyzej za kazdym razem musielibysmy 
# przekopiowc 5-6 linijek kodu za kazdym miec 2 zmienne słuzace
# tylko do do policzenia silni itp.
#
# Miło by było miec kawałek kodu ktoremu powiemy:
# sluchaj wylicz mi silnie 5ciu (5!).
# Na ratunek przychodza funkcje:
# 
def silnia(liczby):
    silnia=1
    for i in xrange(1,liczby+1):
        silnia*=i
    print silnia

# włożyliśmy (ekapsulowalismy - madre slowo) nasz kod liczacy silnie
# do swoistego czarnego pudelka ktore by sie wykonac potrzebuje jeden argument
# wywolajmy ta funkcje pare razy

silnia(1)
silnia(2)
silnia(3)
silnia(4)

# Wlasnie w tych 4rech linijkach zaoszczedzilismy jakies 10 lini kodu,
# dzieki funkcja. Radosc, fanfary itp :)

# Obecnie nasza funkcja cos liczy a potem wypisuje na ekran.
# Nie jest to zle, nie mniej nie mamy teraz jak sie dostac do wartosc silni
# gdybysmy chcieli ja wykorzystac dalej w programie.
# Zmodyfikujemy funkcje silnia tak by zwracala wartosc zamist ja wypisywac.

def silnia(liczby):
    silnia=1
    for i in xrange(1,liczby+1):
        silnia*=i
    return silnia

print silnia(1)
print silnia(2)
print silnia(3)
wartosc_silni = silnia(4)
print wartosc_silni

# Zaczyna byc uzytecznie :) 
# Idac dalej mozemy nawet wywolac ja w petli:

for i in xrange(1,5):
    print silnia(i)




