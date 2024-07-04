import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
var1 = input("Podaj składnik 1:")
var2 = input("Podaj składnik 2:")

logging.debug(f"{operation} {var1} i {var2}")
print("Wynik:")