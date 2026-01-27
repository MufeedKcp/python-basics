with open(r'C:\Users\biten\OneDrive\Desktop\product sales dataset csv\orders.csv', 'r') as f:
    for line in f:                                                                                  # read a file (BEST PRACTICE)
        print(line)

with open(r'C:\Users\biten\OneDrive\Desktop\product sales dataset csv\orders2.csv', 'w') as f:
    f.write('new file')
                                        # 'w' for overwritting the data                                      # write a file                                 
                                          # 'a' for writing new lines while keeping the current data

with open(r'C:\Users\biten\OneDrive\Desktop\product sales dataset csv\orders.csv', 'r') as rf:
    with open(r'C:\Users\biten\OneDrive\Desktop\product sales dataset csv\orders2.csv', 'w') as wf:
        for line in rf:
            wf.write(line)                                                                            # copying the data and paste it into another file



with open('name.txt', 'r') as file:
    if len(file.readlines()) >= 30:
        print("The room is full")                                                                      # to limit the number of value in the value
    else:
        print("Room is not full yet...!")

with open('name.txt', 'r') as file:   
    for lines in file:                                                                                #for searching for someone or some valeus
        if lines.strip() == "mufeed":
            print(f"i found {lines.strip()} nigga")



with open('name.txt', 'r') as file:
    for line in file:
        if line.strip() == "mufeed":
            print(f"I found {line.strip()}")                                                          #to sort the file value 
    for lines in reversed(sorted(file)):
        print(f"hello, {lines.strip()}")


mem = []

with open(r'C:\Users\biten\OneDrive\Documents\python_learning\students.csv', 'r') as f:
    for line in f:
       name, work = line.strip().split(",")
       family = {"name": name, "work": work}
       mem.append(family)

                                                                                
for person in sorted(mem, key=lambda person: person['name']):
    print(f"{person['name']} is in {person['work']}")


import csv                                                                                 #to sort only the name

fam = []
with open(r'C:\Users\biten\OneDrive\Documents\python_learning\students.csv', 'r') as f:
    reader = csv.reader(f)
    for name, work in reader:
        fam.append({"name": name, "work": work})

for person in sorted(fam, key=lambda person: person['name']):
    print(f"{person['name']} is in {person['work']}")


import csv

name = input("whats your name? ")
home = input("where is your home? ")

with open(r'C:\Users\biten\OneDrive\Documents\python_learning\students.csv', 'a') as f:
    writer = csv.writer(f)

    writer.writerow([name, home])
