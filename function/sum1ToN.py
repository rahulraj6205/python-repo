# def studentInfo (**kwargs):
#     for x,y  in kwargs.items():
#         print (x ,"is ",y )

# studentInfo (name = "rahul sharma",age = 20, city = "Gaya ")
# studentInfo (name = "monul sharma",age = 25, city = "Gaya ")
# studentInfo (name = "shivam  sharma",age = 24, city = "Gaya ")

def add1ToN(n):
    sum =0
    for i in range (1,n+1):
        sum+=i
    return sum

n = int (input("Enter the number ")) 
print ("the of 1 to" ,n, "is ",add1ToN(n))