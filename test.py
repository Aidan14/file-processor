import re
import os

words = ['agagiosdji', '1518069aga', ')(*&^agagAGAG%$#@!ñ']

validWords = []

for word in words:
    if re.match('^[a-zA-Zñ\[\]{}*.`!@#$%^&*()\-=_+;/?><|\\áéíóúÁÉÍÓÚ ]+$', word):
        validWords.append(word)

print(validWords)

print(os.environ['FILE_PATH'])