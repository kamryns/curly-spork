class Trial:
  def _init_(self, phrase):
    print(phrase)
    s = phrase[::-1]
    rev_str = reversed(phrase)
    print (rev_str)
    if (phrase==phrase[::-1]):
        print('This is a palindrome')
    else:
        print('This is not a palindrome')
def tester():
  phrase = input("Type a Word: ")
  obj = Trial()
  phrase = obj._init_([phrase])
if __name__ == "__main__":
    tester()
