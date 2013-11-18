
# Przyklady funkcji:

def do_kwadratu(x):
	return x*x

# def wbz - alternatywa nazwa. czytelniej? praktyczniej?
def wartosc_bezwgzledna(x):
	if( x > 0 ):
		return x
	else
		return -x

# Nie zdziwi nas mam nadzieje mozliwoc posiadania wiecej nzi jednego argumentu

# funkcja kwadratowa postaci:
# f = a*x^2 + b*x + c
def wypisz_funkcje(a,b,c):
	funkcja=""
	funkcja+=funkcja+"{0}x^2 + ".format(a) if a!=0
	funkcja+=funkcja+"{0}x + ".format(b) if b!=0
	funkcja+=funkcja+str(c) if c!=0
	print funkcja+"\n"


# Nie dziwi nas tez fakt ze jedna funkcja moze wywolac inna:

def formatuj_nazwisko(nazwisko):
    return "Moje nazwisko to " +nazwisko

def formatuj_imie(imie):
    return "Nazywam sie "+imie

def wypisz_dane(imie,nazwisko):
    print formatuj_imie(imie)
    print formatuj_nazwisko(nazwisko)    
wypisz_dane('Jan','Kowalski')

# Dziwić nas natomiast moze, gdy funckaj wywoluje siebie sama:
# Popatrzmy na dwa sposoby obliczenia silni
# jeden jest to sposob tzw. iteracyjny, drugi rekurencyjny/

#Iteracyjnie
def silnia_it(x):
    silnia=1
    for x in xrange(1,x+1):
        silnia*=x
    return silnia
print silnia_it(4)

#Rekurencyjnie
def silnia_rek(x):
    if(x>1):
        return x*silnia_rek(x-1)
    return x
print silnia_rek(4)



# Temat do ktorego podobnie podejdziemy reurencyjnie i iteracyjnie 
# to liczby fibonaciego. Definiuje sie je tak:
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2)

#Wersja rekurencyjna
def fib_rek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rek(n-1) + fib_rek(n-2)


# Wersja iteracyjna
def fib_it(n):
    a = 0
    b = 1
    for i in range(n):
        tmp = b
        b = a + b
        a = tmp
    return a

print "Rekurencyjnie ",fib_rek(5)
print "Iteracyjnie ",fib_it(5)


