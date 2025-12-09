import re
text = "I love #Python and #AI"
print(re.findall(r'#\w+', text))
