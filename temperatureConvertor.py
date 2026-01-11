temperature = input("Is your temperature Celsius or Fehrenheit (C/F): ")
 
temp1 = int(input("enter the temperature: "))

if temperature == "C":
    result = temp1 * 9//5 + 32
    print(f"Temperature {temp1}°C = {result}°F")

elif temperature == "F":
    result2 = (temp1 - 32) * 5//9
    print(f"temperature in {temp1}°F = {result2}°C")

else:
    print(f"invalid temperature sign")

