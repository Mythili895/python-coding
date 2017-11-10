def addDigits(self, num):
    if num ==0:
        return num
    else:
        return (num-1)%9 +1
