from colorama import init, Fore
init()
print("Leap year calculator")

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(Fore.GREEN + "Leap year.")
        else:
            print(Fore.RED + "Not leap year.")
    else:
        print(Fore.GREEN + "Leap year.")
else:
    print(Fore.RED + "Not leap year.")
