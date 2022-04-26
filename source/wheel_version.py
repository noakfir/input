import re
with open("input/setup.py", "r") as f:
    contents = f.readlines() 

for word in contents:
    if word.startswith("    version="):
        word = word.strip()
        result = re.split("'+", word)
        print(result[1])