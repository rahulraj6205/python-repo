# def sum (n1,n2):
#     sum = n1+n2
#     return sum 

#keyword argument 
# n1 = int (input("enter the first number "))
# n2 = int (input ("enter the second number "))
# print("the sum of two number is ", sum (n1,n2))

# # positional argument 
# print ("the sum of two number is ",sum (n2=5,n1 =7))

#default argument 
# def add (n1=0,n2=6):
#     print ("n1: ", n1) 
#     print ("n2: ",n2)
#     sum = n1 + n2
#     return sum 
# print ("the sum of two number is ",add(3))

# Arbitary argument 
# def addAllNumber (*args):
#     sum =0
#     for i in args:
#         sum=sum+i
#     return sum 
# output = addAllNumber(1,2,5,8,7,6)
# print (" the sum of all number is ",output)
    
def students (**kwargs):
    for x,y in kwargs.items():
        print(x , "is ",y)
students (name = "rahul sharma", age= 24, city = "Gaya ", )
students (name ="shivam raj  ",age = 20, city ="Gaya ")
students (name ="mohit " ,age = 16, city ="delhi " )