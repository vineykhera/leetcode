class Counter(object) :
   def __init__(self, fun) :
       self._fun = fun
       self.counter=0
   def __call__(self,*args, **kwargs) :
       self.counter += 1
       return self._fun(*args, **kwargs)

def fibonaci(n):
    global numCalls
    numCalls += 1

    if n <= 1:
        return 1
    else:
        return fibonaci(n-2) + fibonaci(n-1)


def fib_efficient(n, mydict):
    global num_new_calls
    if n <= 1:
        if n in mydict:
            ans = mydict[n]
            return ans
        else:
            mydict[n] = 1
            return 1
    else:
        if n in mydict:
            ans = mydict[n]
        else:
            num_new_calls += 1
            ans = fib_efficient(n-2, mydict) + fib_efficient(n-1, mydict)
        return ans


numCalls = 0
print(fibonaci(2))
print("number of calls", numCalls)
print(fibonaci(3))
print(fibonaci(5))
numCalls = 0
print(fibonaci(15), "Number of calls made", numCalls)

print("Now running fibonaci  with memoization")

mydict = {}
num_new_calls = 0

print(fib_efficient(2, mydict))
print(fib_efficient(3, mydict))
print(fib_efficient(5, mydict))
num_new_calls = 0
fib_efficient = Counter(fib_efficient)

print(fib_efficient(15,mydict), "Number of calls made", num_new_calls)


print('# of times recur has been called =', fib_efficient.counter)