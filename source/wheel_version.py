import re
with open("input/setup.py", "r") as f:
    contents = f.readlines() 

for word in contents:
    if word.startswith("    version="):
        result = re.split("'+", word)
        print(result[1])
        break