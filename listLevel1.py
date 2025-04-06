list=[1,"apple",True,4.5,5]

print(len(list))
print(list[0])   
print(list[2])
print(list[4])

my_info=["rahul",19,5.3,"unmarried","india"]

mix_fruit=["Gauva","Mango","Apple","pear","fig","orange","banana"]
print(mix_fruit)
print(len(mix_fruit))
print(mix_fruit[0])
print(mix_fruit[4])
print(mix_fruit[-1])

mix_fruit[2] = "grapes"
# mix_fruit.replace("pear",",cherry")
print(mix_fruit)

#10
mix_fruit.append("Grapes")
print(mix_fruit)
#11
mix_fruit.insert(4,"carrot")
print(mix_fruit)
#12
print("14")
# fruit= mix_fruit.Upper()
# print(fruit)
#13
print("13")
# str =("apple","Mango")
# fruit= mix_fruit+str
# print(fruit)
print(mix_fruit + ["apple","mango"])
#14
print( "Gauva" in mix_fruit)
#15
mix_fruit.sort()
print(mix_fruit)
#16
mix_fruit.sort(reverse=True)
print(mix_fruit)
#17
fruit= mix_fruit[:3]
print(fruit)
#18
print(mix_fruit[-3:])
#19
print(mix_fruit[4])
#20
mix_fruit.remove("pear")
print(mix_fruit)
#21
mix_fruit.pop(5)
print(mix_fruit)
#22
mix_fruit.pop()
print(mix_fruit)
#23
mix_fruit.clear()
print(mix_fruit)
#24
# del mix_fruit
# print(mix_fruit)


#level-2
print("LEVEL-2")
age= [19,23,19,25,21,20,25,26,25,24]
print(age)
age.sort()
print(age)
print("MInimum age :-",min(age))
print("Maximum age ",max(age))
age.append(19)
print(age)
age.append(26)
print(age)

median_age= (20+25)/2
print(median_age)

avg_age = 272/12
print(avg_age)

print("the range of age is :- ",min(age), max(age))