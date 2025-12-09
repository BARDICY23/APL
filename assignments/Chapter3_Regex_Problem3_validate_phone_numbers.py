import re
pattern = re.compile(r'^(?:\+\d-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$')
tests = ['+1-555-1234','123-456-7890','5551234']
print([t for t in tests if pattern.match(t)])
