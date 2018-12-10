def cipher_word(word):
   if len(word) > 1:
      first = word[0]
      last = word[-1]
      word = list(word)
      word[0] = last
      word[-1] = first
      word = ''.join(word)
   return word

def cipher_words(words):
   words = words.split()
   stuff = []
   for each in words:
      n = cipher_word(each)
      stuff.append(n)
   print(stuff)
   s = ' '.join(stuff)
   return s




