#pass by value  :- any change inside function , does not effect the orignal values(make a copy of orignal value )
# def addOne (x):
#     x =x+1
#     print("inside function",x)

# x =5 
# addOne(x)
# print("outside the function ",x)

#pass by reference :- it passed the actual value to the function  (mutable objects).
#change inside function does affect the origanal value .
def modifyList (list):
    list.append(4)
    print("inside function ",list )
list = [4,8,7,5,2]
modifyList(list)
print ("inside function ",list )