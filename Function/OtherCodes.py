#/////Lambsa function/////

# data=[12,3,34,5,47,78,4,4,2,4,2,3,7,7]

# def even_num_filter(n):
#     result= n%2 ==0
#     return result





# even_num=tuple(filter(even_num_filter,data))
# print(even_num)

# def f1():
#     def f2():
#         return "Hello, I am inner function"
#     return f2()

# print(f1())



#//////////////Nested Function////////////////
# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def operation(a,b,c):
#     return c(a,b)  # add(90,10)
# """highy ordered function"""
# print(operation(90,10,add))
# print(operation(90,10,sub))



#//////////////Map Function////////////////
# def square(n):
#     return n**2

# data=[1,2,3,4,5,6,7,8,9]
# square_num= list(map(square,data))
# print(square_num)