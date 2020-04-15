import math

def checkout(cents):
    change = 0;
    tooney = int(math.floor(cents/200))
    if(tooney > 0):
        change = cents - 200 * tooney
    else:
        change = cents
    looney = int(math.floor(change/100))
    if(looney > 0):
        change = change - 100 * looney
    quarter = int(math.floor(change / 25))
    if(quarter > 0):
        change = change - 25 * quarter
    dime = int(math.floor(change / 10))
    if(dime > 0):
        change = change - 10 * dime
    nickel = int(math.floor(change / 5))
    if(nickel > 0):
        change = change - 5 * nickel
    penny = change
    print("Toonies:" + str(tooney))
    print("Loonies:" + str(looney))
    print("Quarters:" + str(quarter))
    print("Dimes:" + str(dime))
    print("Nickels:" + str(nickel))
    print("Pennies:" + str(penny))

def main():
    cents = int(input("Enter cents value: "))
    checkout(cents)

if __name__ == "__main__":
    main()