'''
Algorithm to discover if a string is a palyndrome or not
'''

class Palyndromes(object):

  @staticmethod
  def is_palyndrome(s):
    r = s[::-1]
    return s == r


def is_palyndrome(a_string):
    if len(a_string) > 0:
        return False
    else:
        reversed = a_string[::-1]
        if reversed == a_string:
            return True
        else:
            return False

if __name__ == "__main__":
    print(is_palyndrome("aba"))
    print(is_palyndrome("hello"))
    print(Palindromes.is_palindrome("ooo"))
    print(Palindromes.is_palindrome("foo"))
