
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    l = list(str(x))
    l.reverse()
    n = ''.join(l)
    return str(n) == str(x)


    # 高级做法
    # str(x)[::-1] == str(x)


print(isPalindrome(78987))
        