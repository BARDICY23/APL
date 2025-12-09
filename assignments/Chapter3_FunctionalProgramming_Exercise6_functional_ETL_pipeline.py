from collections import Counter
import re

def functional_etl(texts):
    stopwords = {"the", "a", "is", "and", "or", "in", "on", "at", "to", "for"}
    
    words = []
    for text in texts:
        words.extend(re.findall(r'\b\w+\b', text.lower()))
    
    filtered = [w for w in words if w not in stopwords]
    return dict(Counter(filtered))

texts = ["the quick brown fox", "the lazy dog", "a quick fox"]
result = functional_etl(texts)
print(result)
