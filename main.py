import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")



def calculator(op,*args):
    if op == "1":
        result = 0
        for i in range(0,len(args[0])):
            result += args[0][i]
        return result
    elif op == "2":
        return args[0][0]-args[0][1]
    elif op == "3":
        result = 1
        for i in range(0,len(args[0])):
            result *= args[0][i]
        return result
    elif op == "4":
        return args[0][0] / args[0][1]
    else:
        return None
    
def get_vars(a):
    vars = []
    if a == "many":
        i = 1
        while True:
            add = input(f"Podaj składnik {i} (zatwierdź puste, jeśli nie masz więcej składników): ")
            if add == "":
                break
            else:
                if add.replace(".","").isnumeric():
                    vars.append(float(add))
                else:
                    logging.debug("Jedna z podanych wartości nie jest liczbą.")
                    sys.exit()
            i += 1
        return vars
    elif a == "two":
        for i in range(0,2):
            add = input(f"Podaj składnik {i+1}: ")
            if add.replace(".","").isnumeric():
                vars.append(float(add))
            else:
                logging.debug("Jedna z podanych wartości nie jest liczbą.")
                sys.exit()
        return vars

if __name__ == "__main__":
    operation = input(
        "Podaj działanie, posługując się odpowiednią liczbą:"
        "\n1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie: "
        )
    if operation == "1":
        operate = "Dodaję"
        vars = get_vars("many")
    elif operation == "2":
        operate = "Odejmuję"
        vars = get_vars("two")
    elif operation == "3":
        operate = "Mnożę"
        vars = get_vars("many")
    elif operation == "4":
        operate = "Dzielę"
        vars = get_vars("two")
    debug_msg = f"{operate} " + " i ".join(str(var) for var in vars)
    logging.debug(debug_msg) #', '.join(str(x) for x in list)
    print(f"Wynik: {calculator(operation,vars)}")