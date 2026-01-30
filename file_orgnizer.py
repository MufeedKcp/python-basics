import os

os.makedirs('organized', exist_ok=True)
os.makedirs('organized/CSV', exist_ok=True)
os.makedirs('organized/PNG', exist_ok=True)
os.makedirs('organized/text document', exist_ok=True)            # this Create subfolders inside organized for each file type.
os.makedirs('organized/others', exist_ok=True)
os.makedirs('organized/PDF', exist_ok=True)


for file in os.listdir("messy_file"):
    full_path = os.path.join("messy_file", file)    
    if os.path.isfile(full_path):        # Process only files (skip folders)
        if file.lower().endswith(".csv"):
            os.rename(os.path.join("messy_file", file), os.path.join("organized/CSV", file))

        elif file.lower().endswith(".txt"):
            os.rename(os.path.join("messy_file", file), os.path.join("organized/text document", file))
    
        elif file.lower().endswith(".pdf"):
            os.rename(os.path.join("messy_file", file), os.path.join("organized/PDF", file))
    
        elif file.lower().endswith(".png"):
            os.rename(os.path.join("messy_file", file), os.path.join("organized/PNG", file))

        else:
            os.rename(os.path.join("messy_file", file), os.path.join("organized/others", file))
    else:
        pass

