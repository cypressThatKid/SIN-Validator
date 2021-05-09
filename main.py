from colorama import Fore, Style
import sys

def validate(sin):
    bigNumber = []
    sin = str(sin)

    first = int(sin[0])
    third = int(sin[2])
    fifth = int(sin[4])
    seventh = int(sin[6])
    ninth = int(sin[8])
    second = int(sin[1]) * 2
    fourth = int(sin[3]) * 2
    sixth = int(sin[5]) * 2
    eighth = int(sin[7]) * 2
    
    bigString = "{}{}{}{}{}{}{}{}{}".format(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth)

    for number in bigString:
        bigNumber.append(int(number))

    bigAnswer = sum(bigNumber)

    if bigAnswer % 10 == 0:
        return True
    else:
        return False


sin = input("Enter Social Insurance Number: ")

if sin == "":
    sys.exit(Fore.RED + "[ERROR] Enter A SIN!" + Fore.RESET)

if validate(sin):
    print(Fore.GREEN + "{} is VALID!".format(sin))
else:
    print(Fore.RED + "{} is NOT valid!".format(sin))

print(Fore.RESET)
