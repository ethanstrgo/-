# def fib(n):
# #递归实现斐波那契数列
#     if n == 1:
#         return 1
#     else:
#         return n + fib(n-1)
#
# print(fib(8))



# def fib(a, b):
#     if a == 0:
#         return 0
#     c  = a + b
#     fib(b, c)
#     print(a, b)

def func(arg1,arg2):
    if arg1 == 0:
        print(arg1, arg2)
    arg3 = arg1 + arg2
    print(arg3)
    func(arg2, arg3)

func(0,1)
