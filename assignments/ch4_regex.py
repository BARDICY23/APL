import re
def validate_email(email):
    pattern = re.compile(r'^[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.(com|org|edu)$')
    return bool(pattern.match(email))
def extract_hashtags(text):
    return re.findall(r'#\w+', text)
def validate_phone(number):
    pattern = re.compile(r'^(\+\d-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$')
    return bool(pattern.match(number))
def word_frequency(text):
    words = re.findall(r"\w+", text)
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
def duplicate_consecutive(text):
    return re.findall(r'\b(\w+)\s+\1\b', text)
def extract_dates(text):
    return re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
def mask_card(text):
    return re.sub(r'\d(?=\d{4})', '*', text)
def extract_languages(text):
    return re.findall(r'\b[A-Za-z+#\+]+\b', text)
if __name__ == '__main__':
    print(validate_email('user@example.com'))
    print(extract_hashtags('I love #Python and #AI'))
    print(validate_phone('+1-555-1223'))
    print(word_frequency('Python, Python! AI is great; Python AI.'))
    print(duplicate_consecutive('This is is a test test'))
    print(extract_dates('The events are on 2023-05-12 and 2024-01-01.'))
    print(mask_card('Card: 1234-5678-9012-3456'))
    print(extract_languages('I know Python, Java, and C++ but not Ruby.'))
