import re
with open("setup.py", "r") as f:
    contents = f.readlines() 

for word in contents:
    if "version" in word:
        result = re.split("'+", word)
        print(result[1])
        break