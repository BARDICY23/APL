import re
text = "The events are on 2023-05-12 and 2024-01-01."
print(re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))
