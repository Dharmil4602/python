# a = int(input("Enter An Integer: \n"))
# n1 = int("%i" % a)
# n2 = int("%i%i" % (a,a))
# n3 = int("%i%i%i"% (a,a,a))
# print(n1+n2+n3)

def num(n):
    a = int(n) + int(n+n) + int(n+n+n)
    return a
n = input("Enter the number:- ")
print(num(n))