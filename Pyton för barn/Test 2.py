
'''''
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
print (beräkna_lön_efter_skatt(18000,15))
'''
age = int(input("Ange din ålder: "))
if age < 18:
 print("Du är inte gammal nog för att titta på filmen!")

if age >=18:
 print ("Enjoy your single time!!!")
