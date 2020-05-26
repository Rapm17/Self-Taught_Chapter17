import re

sentence = "The ghost that says boo haunts the loo"

match = re.findall(".oo", sentence, re.IGNORECASE)

print(match)
