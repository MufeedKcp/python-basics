import os

# print(os.listdir("incoming"))                 #Returns a list of all files & folders in a directory

# print(os.getcwd())                            #Returns the current working directory eg-"incoming"

# print(os.chdir("path"))                       #Changes the current working directory


# for files in os.listdir("incoming"):
#     if files.endswith(".csv"):                #Only process .csv files for ETL.
#         print(files)

# for items in os.listdir("incoming"):
#     full_path = os.path.join("incoming", items)
#     if os.path.isfile(full_path):
#         print(items, "is a file")
#     elif os.path.isdir(full_path):
#         print(items, "is a folder")

# os.path.abspath("incoming")                   # Convert relative to absolute path

# full_path = os.path.abspath("incoming")

# for file in os.listdir(full_path):
#     if file.lower().endswith(".csv"):
#         print(os.path.join("incoming", file))


# os.makedirs("archive", exist_ok=True)           # Creates folder if missing
# os.rmdir("archive")             # Removes empty folder


# for file in os.listdir("archive"):
#     if file.lower().endswith(".csv"):
#         os.rename(os.path.join("archive", file), os.path.join("incoming", file))
#         print(file, "moved")            #Moving all .csv files from incoming/ to archive/.

INCOMING = "incoming"
CSV_FILES = []

for file in os.listdir(INCOMING):
    full_path = os.path.join(INCOMING, file)
    if os.path.isfile(full_path) and file.lower().endswith(".csv"):
        CSV_FILES.append(full_path)

print("CSV files to process:", CSV_FILES)

for file in CSV_FILES:
    print(file)