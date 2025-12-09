import re
text = "This is is a test test"
print(re.findall(r'\b(\w+)\s+\1\b', text))
