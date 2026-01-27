weight = float(input("""
    1. Kilogram to Pounds 
             or  
    2. Pounds to Kilogram
choose (1/2): """))

weight1 = float(input("Enter your Weight:  "))

if weight == 1:
    result = weight1 * 2.20462
    print(f"{round(result)}Ibs")
elif weight == 2:
    result2 = weight1 * 0.453592
    print(f"{round(result2)}kg")
else:
    print(f"oohps...{weight1} is not valid...!")