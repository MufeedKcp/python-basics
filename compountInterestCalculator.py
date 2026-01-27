# repeat = "Y"

# while repeat =="Y":
#     principle = int(input("Enter the principle: "))
#     rate = float(input("Enter the rate: "))
#     time = int(input("Enter number of years: "))
#     counter = 1


#     while counter <= time:
#         principle+=(principle*rate / 100)
#         print(f"year {counter}: {round(principle, 2)}")
#         counter+=1
#     repeat = input("Do you want to calculate again? (Y/N): ").upper()

################################################################################################

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = int(input("Enter the principle: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero...!")

while rate <= 0:
    rate = int(input("Enter the interest rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero...!")

while time <= 0:
    time = int(input("Enter the time in year: "))
    if time <= 0:
        print("Time can't be less than or equal to zero...!")

total = principle * pow((1 + rate / 100), time)
print(f"{total:.2f}")