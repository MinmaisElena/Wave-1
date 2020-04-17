import sys

def duration():
    day = input("Enter the number of days: ")
    hour = input("Enter the number of hours: ")
    minute = input("Enter the number of minutes: ")
    second = input("Enter the number of seconds: ")
    print(int(day)*60*60*24 + int(hour)*60*60 + int(minute)*60 + int(second))

def main():    
    duration()

if __name__=="__main__":
    main()