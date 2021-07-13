def bubble(a):
    l = len(a) - 1
    for i in range(0, l):
        for j in range(0, l-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] 
    #print(a)
    return a

assert(bubble([3,2,1])==[1,2,3])
assert(bubble([5,4,3,2,1])==[1,2,3,4,5])

def startri(r):
    for i in range(r):
        print(' '*(r-i-1) + '*'*(2*i+1)) 

#startri(9)

def fibonacci(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        print(n1)
        next = n1 + n2
        #update number
        n1 = n2
        n2 = next

#fibonacci(10)

def fib(n):
    p, q = 0, 1
    while p<n:
        yield p
        p , q = q, p+q

#for i in fib(10):
#    print(i)

def reverse_interger(n):
    a = 0                   
    while n > 0:       
        a = a * 10 + n % 10       
        n = n // 10       
    return a

#print(reverse_interger(123))

def average_words_length(s):       
    return sum(len(word) for word in s.split()) / len(s.split())

