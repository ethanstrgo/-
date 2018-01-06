def isPalindrome(s):
    if len(s) <= 1:
        return 1
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

'''循环实现'''
def isPalindrome1(s):
    for i in range(len(s))/2:
        if not s[i] == s[[len(s)] - i -1]:
            return 0
    return 1

def isPalindrome2(s):
    return s == s[::-1]
