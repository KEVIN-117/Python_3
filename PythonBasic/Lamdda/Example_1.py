adition = lambda a: a+10
print(adition(10))



def function(n):
    return lambda a:a+n

s = function(10)
print(s(10))