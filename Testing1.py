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
'''

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
