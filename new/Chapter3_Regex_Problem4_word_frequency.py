import re
from collections import Counter
text = "Python, Python! AI is great; Python AI."
words = re.findall(r"\b[A-Za-z+#+\+]+\b", text)
print(dict(Counter(words)))
