def outerFunction ():
    x =2

    def innerFunction ():
        y=4
        result = x+y
        return result
    return innerFunction()

output = outerFunction()
print(output )