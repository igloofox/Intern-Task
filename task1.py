from textwrap import wrap
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']

def mapFirst(string):
   return ''.join(bin(a.index(c))[2:].zfill(6) for c in string)

def binaryToLetter(binNew):
   return ''.join(chr(int(binNew[max(0, i - 8):i], 2)) for i in range(len(binNew), 0, -8))

def reverseString(string):
   return string[::-1]
def main():
   k = 'Y3Jvc3MgYW5kIHBvaW50ZXIgYW5hbHlzaXMgZ3JhcGggYWxnb3JpdGhtcyBpaXQgbWFkcmFzIGdhamVuZHJhIGNpcmNsZSBlaW5zdGVpbjAxMjM0'
   print("the first binary value is: ",mapFirst(k))
   print("the final decoded value is: ", reverseString(binaryToLetter(mapFirst(k))))

if __name__ == "__main__":
  main()