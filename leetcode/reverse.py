def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        n = 0
        if x < 0:
            s = ''
            l = list(str(x)[1:])
            l.reverse()
            n = int('-'+s.join(l))
        else:
            s = ''
            l = list(str(x))
            l.reverse()
            n = int(s.join(l))

        if n < -2**31 or n > 2**31 - 1:
            n = 0
        return n
print(reverse(1534236469))