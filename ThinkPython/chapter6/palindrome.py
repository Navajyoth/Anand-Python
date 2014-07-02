def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
  
def palindrome(word):
    if len(word) == 1:
        return True
    elif last(word) == first(word):
         return True
    else:
         return False


palindrome('nms')
