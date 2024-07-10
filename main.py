import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")



def calculator(op,*args):
    """
    Performs a mathematic operation based on first arg
    on the rest of the arguments.
    Supports multiple args for next_varition and multiplication
    Supports two args for subtraction and division
    Arguments:
    str op: "1","2","3","4"
    list of floats *args
    """
    if op == "1":       # dodawanie
        result = 0
        for i in range(0,len(args[0])):
            result += args[0][i]
        return result
    elif op == "2":     # odejmowanie
        return args[0][0]-args[0][1]
    elif op == "3":     # mnożenie
        result = 1
        for i in range(0,len(args[0])):
            result *= args[0][i]
        return result
    elif op == "4":     # dzielenie
        return args[0][0] / args[0][1]
    else:
        return None
    
def dict_calculator(op,*args):
    """
    op_dict = {
        "1" : [result ]
    }
    
    """
    
    pass

def addition(*args):
    result = 0
    for i in range(0,len(args)):
        result += args[i]
    return result

def subtraction(arg1, arg2):
    return arg1 - arg2

def multiplication(*args):
    result = 1
    for i in range(0,len(args)):
        result *= args[i]
    return result

def division(arg1, arg2):
    return arg1 / arg2
    
def get_vars(a):
    """
    Prompts the user to input variables
    based on the operation chosen
    Arguments:
    str a: "many","two"
    """
    vars = []
    if a == "many":
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
    elif a == "two":
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

    # if operation == "1":
    #     operate = "Dodaję"
    #     vars = get_vars("many")
    # elif operation == "2":
    #     operate = "Odejmuję"
    #     vars = get_vars("two")
    # elif operation == "3":
    #     operate = "Mnożę"
    #     vars = get_vars("many")
    # elif operation == "4":
    #     operate = "Dzielę"
    #     vars = get_vars("two")
    # debug_msg = f"{operate} " + " i ".join(str(var) for var in vars)
    # logging.debug(debug_msg) #', '.join(str(x) for x in list)
    # print(f"Wynik: {calculator(operation,vars)}")

    # op_dict = {
    #     "1" : ["Dodaję",   get_vars("many")],
    #     "2" : ["Odejmuję", get_vars("two")],
    #     "3" : ["Mnożę",    get_vars("many")],
    #     "4" : ["Dzielę",   get_vars("two")]
    # }
    # vars = op_dict[operation][1]
    # debug_msg = f"{op_dict[operation][0]} " + " i ".join(str(var) for var in vars)
    # logging.debug(debug_msg) #', '.join(str(x) for x in list)
    # print(f"Wynik: {calculator(operation,vars)}")
    print(addition(2,3,5), multiplication(5,5,5))
    print(subtraction(20,10), division(10,2))