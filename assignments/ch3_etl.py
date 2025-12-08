import re
def etl_pipeline(strings, stopwords=None):
    if stopwords is None:
        stopwords = {'the','a','is'}
    freq = {}
    for s in strings:
        words = re.findall(r"\w+", s)
        for w in words:
            if w.lower() in stopwords:
                continue
            freq[w] = freq.get(w, 0) + 1
    return freq
if __name__ == '__main__':
    texts = ['the quick brown fox', 'a quick dog', 'quick is quick']
    print(etl_pipeline(texts))
