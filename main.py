import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")
    
def dict_calculator(op):
    """
    Chooses a function to execute based on input
    Arguments:
    op: str "1" "2" "3" "4"
    """
    results_dict = {
        "1" : addition,
        "2" : subtraction,
        "3" : multiplication,
        "4" : division
    }
    return results_dict[op]

def dict_operation(op):
    """
    Returns a string naming the kind of operation being executed
    Arguments:
    op: str "1" "2" "3" "4"
    """
    operation_dict = {
        "1" : "Dodaję",
        "2" : "Odejmuję",
        "3" : "Mnożę",
        "4" : "Dzielę"
    }
    return operation_dict[op]

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

def check_num(arg):
    """
    Checks if provided arg is a number
    Arguments:
    arg: str
    """
    if arg.replace(".","").isnumeric():
        return True
    else:
        logging.debug("Jedna z podanych wartości nie jest liczbą.")
        sys.exit()
    
def get_operation():
    """
    Provides instruction to get operation from user
    """
    op = input(
        "Podaj działanie, posługując się odpowiednią liczbą:"
        "\n1. Dodawanie, 2. Odejmowanie, 3. Mnożenie, 4. Dzielenie: "
        )
    if op in "1234":
        return op
    else:
        logging.debug("Podana wartość niezgodna z instrukcją.")
        sys.exit()

def get_base_vars():
    """
    Prompts user to provide 2 necessary variables for operation
    """
    base_vars = []
    for i in range(0,2):
        next_var = input(f"Podaj składnik {i+1}: ")
        if check_num(next_var):
            base_vars.append(float(next_var))
    return base_vars

def get_add_vars():
    """
    Prompts user to provide optional variables for operation
    """
    add_vars = []
    while True:
        next_var = input(f"Podaj następny składnik, lub wciśnij Enter aby zakończyć: ")
        if next_var == "":
            break
        else:
            if check_num(next_var):
                add_vars.append(float(next_var))
    return add_vars

if __name__ == "__main__":
    operation = get_operation()
    vars = get_base_vars()
    if operation in "13":
        vars += get_add_vars()
    
    results = dict_calculator(operation)(vars)
    debug_msg = f"{dict_operation(operation)} " + " i ".join(str(var) for var in vars)
    print(debug_msg)
    logging.debug(debug_msg)
    print(f"Wynik: {results}")