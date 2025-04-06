#1
# def  calc_areaAndPerimeter(r):
#     area= 3.145*r*r
#     print ("The area of circle is ",area)
#     perimeter = 2*3.145*r
#     print("the perimeter of circle is ",perimeter)

# r = int (input("Enter the radius of circle  "))
# calc_areaAndPerimeter(r)

#2
# def addAllNums (*args):
#     sum =0
#     for i in args:
#         sum+=i
#     return sum 

# list = [45,12,52,30,29]
# output = addAllNums(4,5,8,9,7)
# print("the sum of all items in list ",output)

#3
# def convert_celsius_To_F(c):
#     F= (c*9/5)+32
#     return F

# c = float(input("enter the temperature in C "))
# print("the temperature in fahrenheit",convert_celsius_To_F(c))

#4
# def check_season(month):
#     if month=="march" or  month=="april" or month =="may" :
#         print(month, " is Spring season " )
#     elif(month=="june" or  month=="july" or month == "august "):
#         print(month, " is Summer  season ")
#     elif (month=="september " or  month=="october" or month == "november  "):
#         print(month, " is Autumn (Fall)  season ")
#     else:
#         print(month, " is Winter season ")

# month = input("enter the month name ")
# check_season(month)

#5 
def calc_slope (x1,y1,x2,y2):
    if x2-x1==0:
        print("Slope is undefined (vertical line )")
    slope = (y2-y1)/(x2-x1)
    return slope
x1 = float(input("enter the value of x1 "))
y1 = float(input("enter the value of y1 "))
x2 = float(input("enter the value of x2 "))
y2 = float(input("enter the value of y2 "))
slope = calc_slope(x1,y1 ,x2 ,y2)
print("slope : ", slope)