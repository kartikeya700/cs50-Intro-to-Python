def main():
    Time = input("What time is it? ")
    time = convert(Time)
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
def convert(time):
    Hours, Minutes = time.split(":")
    hours = int(Hours)
    minutes = int(Minutes)
    TIME = float(hours + minutes/60)
    return TIME
if __name__ == "__main__":
    main()
