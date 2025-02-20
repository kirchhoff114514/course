def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    fallingresult = 1
    while k > 0:
        fallingresult = fallingresult * n
        n = n - 1
        k = k - 1
    return fallingresult



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    digitsum=0
    while y!=0:
        digitsum+=y%10
        y=y//10
    return digitsum



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    eights_count=0
    digit=0
    while n!=0:
        #统计相邻8的个数
        digit=n%10
        if digit==8:
            eights_count+=1
        else:
            #判断是否是两个
            if  eights_count==2:
                return True
            eights_count=0
        n=n//10
    if eights_count==2:
        return True
    else:
        return False



