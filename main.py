import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
    
def dict_calculator(op,args):
    """
    Chooses a function to execute based on input
    Arguments:
    str op: "1" "2" "3" "4"
    list of floats args
    """
    results_dict = {
        "1" : ["Dodaję", addition(args)],
        "2" : ["Odejmuję", subtraction(args)],
        "3" : ["Mnożę", multiplication(args)],
        "4" : ["Dzielę", division(args)]
    }
    return results_dict[op]

def addition(args):
    result = 0
    for arg in args:
        result += arg
    return result

def subtraction(args):
    return args[0] - args[1]

def multiplication(args):
    result = 1
    for arg in args:
        result *= arg
    return result

def division(args):
    return args[0] / args[1]
    
def get_vars(a):
    """
    Prompts the user to input variables
    based on the operation chosen
    Arguments:
    str a: "1" "2" "3" "4"
    """
    vars = []
    if a == "1" or a == "3":
        i = 1
        while True:
            next_var = input(f"Podaj składnik {i} (zatwierdź puste, jeśli nie masz więcej składników): ")
            if next_var == "":
                break
            else:
                if next_var.replace(".","").isnumeric():
                    vars.append(float(next_var))
                else:
                    logging.debug("Jedna z podanych wartości nie jest liczbą.")
                    sys.exit()
            i += 1
        return vars
    elif a == "2" or a == "4":
        for i in range(0,2):
            next_var = input(f"Podaj składnik {i+1}: ")
            if next_var.replace(".","").isnumeric():
                vars.append(float(next_var))
            else:
                logging.debug("Jedna z podanych wartości nie jest liczbą.")
                sys.exit()
        return vars

if __name__ == "__main__":
    operation = input(
        "Podaj działanie, posługując się odpowiednią liczbą:"
        "\n1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie: "
        )

    vars = get_vars(operation)
    results = dict_calculator(operation, vars)
    debug_msg = f"{results[0]} " + " i ".join(str(var) for var in vars)
    print(debug_msg)
    logging.debug(debug_msg)
    print(f"Wynik: {results[1]}")