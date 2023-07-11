#List stop words
from nltk.corpus import stopwords
print(stopwords.words("english"))```

``` python
#Remove stop words
words = [w for w in words if w not in stopwords.words("english")]
print(words)
