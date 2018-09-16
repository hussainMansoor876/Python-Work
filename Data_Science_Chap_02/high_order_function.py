def doubler(f):
    def g(x):
        return 2 * f(x)
    return g
def f1(x1):
   return x1 + 1
name = doubler(f1)
print(name(5))
print(name(8))