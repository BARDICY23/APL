import re
text = "I know Python, Java, and C++ but not Ruby."
langs = re.findall(r'\bC\+\+\b|\b[A-Za-z]+\b', text)
print([l for l in langs if l.lower() in {'python','java','c++','ruby'}])
