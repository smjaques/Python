#Sydney Jaques
#String_101

def str_rot_13(string):
   final = []
   for char in string:
      new = ord(char)

      if 'a' <= char <= 'm':
         new += 13
      elif 'n' <= char <= 'z':
         new -= 13

      if 'A' <= char <= 'M':
         new += 13
      elif 'N' <= char <= 'Z':
         new -= 13

      final.append(chr(new))
   
   result = ''.join(final)
   return result


def str_translate_101(string, o, n):
   translate = []
   for let in range(len(string)):
      if string[let] == o:
         translate.append(n)
      else:
         translate.append(string[let])
   return ''.join(translate)
