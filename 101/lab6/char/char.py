#Sydney Jaques
#Char

def is_lower_101(char):
#   lowercase = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#   if char in lowercase:
#      return True
#   else:
#      return False

   if ord('a') <= ord(char) <= ord('z'):
      return True
   else:
      return False

def char_rot_13(char):
   if 'a' <= char <= 'm':
      return chr(ord(char) + 13)
   elif 'n' <= char <= 'z':
      return chr(ord(char) - 13)

   if 'A' <= char <= 'M':
      return chr(ord(char) + 13)
   elif 'N' <= char <= 'Z':
      return chr(ord(char) - 13)

   return char

