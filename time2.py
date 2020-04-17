import math

def time():
    remainder = 0
    total = int(input("Enter the time in seconds: "))
    day = int(math.floor(total/(60*60*24)))
    if (day > 0):
        remainder = total - day*60*60*24
    else:
        remainder = total
    hour = int(math.floor(remainder/(60*60)))
    if (hour > 0):
        remainder = remainder - hour*60*60
    minute = int(math.floor(remainder/60))
    if (minute > 0):
        remainder = remainder - minute*60
    second = remainder
    print(str(day) + ":" 
        + ("0" + str(hour) if hour < 10 else str(hour)) 
        + ":" + ("0" + str(minute) if minute < 10 else str(minute)) 
        + ":" + ("0" + str(second) if second < 10 else str(second)))

def main():
    time()

if __name__=="__main__":
    main()