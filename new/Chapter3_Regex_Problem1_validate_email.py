import re
emails = ["user@example.com", "bad-email", "test@domain.org"]
pattern = re.compile(r'^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.(?:com|org|edu)$')
print([e for e in emails if pattern.match(e)])
