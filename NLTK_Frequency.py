import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

f= open("que.txt","r")

fileData=f.readlines()
print(fileData)

text=" ".join(fileData)
print(text)

tokenized_text=sent_tokenize(text)
print(tokenized_text)

tokenized_word=word_tokenize(text)
print(tokenized_word)
fdist = FreqDist(tokenized_word)
print(fdist)
fdist.most_common(30)
fdist.plot(30,cumulative=False)
plt.show()