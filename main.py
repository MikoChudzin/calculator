import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")


if __name__ == "__main__":
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: \n1. Dodawanie, \n2. Odejmowanie, \n3. Mnożenie, \n4. Dzielenie: ")
    var1 = float(input("Podaj składnik 1:"))
    var2 = float(input("Podaj składnik 2:"))
    
    if operation == "1":
        operate = "Dodaję"
        result = var1 + var2
    elif operation == "2":
        operate = "Odejmuję"
        result = var1 - var2
    elif operation == "3":
        operate = "Mnożę"
        result = var1 * var2
    elif operation == "4":
        operate = "Dzielę"
        result = var1 / var2
        
    logging.debug("%s %s i %s" % (operate, var1, var2))
    print(f"Wynik: {result}")