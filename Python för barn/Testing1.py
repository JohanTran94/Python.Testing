'''''
print ("Hello, World!")
print("Hello Cuong")
print("abch")



# Definiera variablerna
x = 10
y = 20

# Utför additionen
z = x + y

# Skriv ut resultatet
print(f"{x} + {y} = {z}")



x = 10
y = 20
print (f'summan av {x} + {y} är', (x+y))



x = 10
y = 20
summan = x + y
print (f'summan av {x} + {y} är {summan}')



namn = "Johan"
ålder = 25
print (f"Hej, {namn}! Du är {ålder} år gammal.")



x = 42
y = str (x)
print (y)
print (type (y))


x = "123"
y = 2
z = int (x)
resultat = z * y
print (resultat)
print (type (resultat))


x = 10
y = 3
print (x + y)
print (x - y)
print (x * y)
print (x / y)
print (x // y)
print (x % y)
print (x ** y)

pi = 3.14
int_pi = int (pi)
print (int_pi)
x = 5
flyttal_x = float (x)
print (flyttal_x)

x = 0.1
y = 0.2
print (round(x + y, 1))

x1 = 0.1
y1 = 0.2
x2 = int (x1 * 10)
y2 = int (y1 * 10)
print (x2 + y2)

from decimal import Decimal
x = Decimal("0.1")
y = Decimal("0.2")
resultat = x + y
print (resultat)


x = "2"
y = "5"
summa = int (x) + int (y)
print (f"Summan är: {summa}")

x = 42
text = "Talet är: " + str (x)
print (text)

text = "Data Science"
print (text[0])
print (text[-1])
print (text[4])

text = " Python är roligt! "
print (text.strip())
print (text.replace("roligt", "fantastiskt"))
print (text.upper())

namn = "Johan"
ålder = 30
print (f"Hej, {namn}! Du är {ålder} år gammal.")

x = True
y = False
print(type(x))


x = 10
if x > 5:
    print("x är större än 5")

x = 10
print(x > 5 and x < 15) 

x = 10
print( not(x > 5))

try:
    x = int("hello")  # Code này gây lỗi ValueError
except ValueError as e:
    print(f"Lỗi chuyển đổi giá trị: {e}")
except Exception as e:  # Xử lý mọi lỗi khác
    print(f"Lỗi không xác định: {e}")

try:
    x = 1 / 0  # Lỗi chia cho 0
except ValueError:  # Không đúng loại lỗi
    print("Không xử lý lỗi này.")
finally:
    print("Khối finally được thực thi.")

name = input("Hãy nhập tên của bạn: ")
print(f"Xin chào, {name}!")

try:
    text = int("hej")
except:
    print ("Ett fel uppstod")

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")


reallyLongList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in reallyLongList:
    if number % 2 == 0:
        print(number)

for number in reallyLongList:
    if number % 2 != 0:
        print(number)
'''

'''''
skapa och manipulera en lista:
1. skapa en lista med 5 städer.
2. lägg till en ny stad  islutet av listan.
3. ta bort den andra staden i listan.
4. skriv ut alla städer med en for-loop.
lagra och summera heltal:
1. skapa en lista med 5 heltal.
2. summera alla tal i listan.
utmaning:
skapa en lista med namn och sök efter ett namn med en for-loop.
uppdatera alla städer till stor begynnelsebokstav


# 1. Skapa en lista med 5 städer
städer = ["Stockholm", "Göteborg", "Malmö", "Uppsala", "Västerås"]

# 2. Lägg till en ny stad i slutet av listan
städer.append("Örebro")

# 3. Ta bort den andra staden i listan
städer.pop(1)

# 4. Skriv ut alla städer med en for-loop
for stad in städer:
    print(stad)

# Lagra och summera heltal
heltal = [3, 7, 12, 5, 8]
summa = sum(heltal)
print(f"Summan av talen är {summa}")

# Utmaning: sök efter ett namn
namn = ["Anna", "Björn", "Cecilia", "David", "Erik"]
sök_namn = "Cecilia"

for n in namn:
    if n == sök_namn:
        print(f"{sök_namn} finns i listan!")
        break
else:
    print(f"{sök_namn} finns inte i listan.")

# Uppdatera alla städer till stor begynnelsebokstav
städer = [stad.capitalize() for stad in städer]
print(städer)

reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

print("Length: ")
print(len(reallyLongList))

x = 1
for i, fruit in enumerate(reallyLongList):
    if i == (i+1):
        continue
    if (i+1) % 3 == 0:
        print(fruit)
    # x += 1
    x = x + 1
    # Funkar inte
    # x++

print(type(x))
print("x är:")
print(x)

def beräkna_lön_efter_skatt(bruttolön, skattesats):
    """
    Beräknar nettolön (lön efter skatt).

    Parametrar:
    - bruttolön (float): Lön före skatt.
    - skattesats (float): Skattesatsen i procent (t.ex. 30 för 30%).

    Returnerar:
    - float: Nettolön (lön efter skatt).
    """
    if skattesats < 0 or skattesats > 100:
        raise ValueError("Skattesatsen måste vara mellan 0 och 100.")
    if bruttolön < 0:
        raise ValueError("Bruttolön kan inte vara negativ.")
    
    skatt = bruttolön * (skattesats / 100)
    nettolön = bruttolön - skatt
    return nettolön

print(beräkna_lön_efter_skatt(35000,30))


age = int(input("Ange din ålder: "))
if age < 18:
 print("Du är inte gammal nog för att titta på filmen!")

if age >=18:
 print ("Enjoy your single time!")

 
def beräkna_lön_efter_skatt(bruttolön, skattesats):
    """
    Beräknar nettolön.

    Parametrar:
    - bruttolön (float): Lön före skatt.
    - skattesats (float): Skattesatsen i procent

    Returnerar:
    - float: Nettolön.
    """
    if skattesats < 0 or skattesats > 100:
        raise ValueError("Skattesatsen måste vara mellan 0 och 100.")
    if bruttolön < 0:
        raise ValueError("Bruttolön kan inte vara negativ.")
    
    skatt = bruttolön * (skattesats / 100)
    nettolön = bruttolön - skatt
    return nettolön

print (beräkna_lön_efter_skatt(35000,-1))

produkt = {"namn": "Laptop", "pris": 10000, "lager": 50}

# 1. Skriv ut produktens pris.
print ("Produktens pris är: ", produkt ["pris"])
# 2. Lägg till en nyckel för "kategori".
produkt ["kategori"] = "Datorer"
# 3. Ändra värdet på "lager" till 40.
produkt ["lager"] = 40

print (produkt)

# Skapa en dictionary med tre nyckel-värde-par (e.g.,"namn", "ålder", "stad").
Person1 ={"namn": "Johan", "age": 30, "stad": "Stockholm"}
# Iterera genom dictionary och
# skriv ut varje nyckel och värde.
for nyckel, värde in Person1.items():
    print(f'Personens {nyckel}: {värde}')
# Ex:person = {"name": "Anna", "age": 25, "city": "Stockholm"}
# ... fortsätt här

x = int(input("Skriv ett tal: "))
if x > 0:
 print ("Taler är positivt")
elif x < 0:
 print ("Talet är negativt")
else:
 print ("Talet är noll")
 
password = ""
while password == "abc":
    password = input("Ange password: ")
    if password == "abc":
        print("Fel password! Försök igen!")
print("Inloggad")

password = ""
while password != "abc":
    password = input("Ange password: ")
    if password != "abc":
        print("Fel password! Försök igen!")
print("Inloggad")

Fråga = ""
while Fråga != "framtiden":
    print("Vad är något som alltid är framför dig, men som du aldrig kan nå?")
    Fråga = input("Ange svar: ")
    if Fråga != "framtiden":
        print("Fel svar pucko, försök igen!")
print("Rätt svar! Bra jobbat!")

myfamily = {
   "child1" : {
     "name" : "Emil",
#     "year" : 2004,
#     "hobbies": ["Programming", "Football", "Gaming"]
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print( len(myfamily) )
'''
my_list = ["äpple", "banan", "körsbär"]
for fruit in my_list:
   print(fruit)
   print (type(fruit))