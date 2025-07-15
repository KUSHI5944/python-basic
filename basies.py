
                                   #letcture-1
# print("hello")
# print("kushi")
# print("heyyy i am kushi.")
# name ="kushi"
# age = 19
# price = 44

# print(age)
# print(price)
# print("my age:",age)
# print("my name:",name)
# print(type(age))
# print(type(name))
# a=2
# b=5
# sum=a+b
# print(sum)
# a = input("name:")
# print(a)
# age=int(input("age:"))
# price=float(input("price:"))

# print("heyyy my name is ",a,"my age is",age)

# light=input("enter the color: ")
# if(light=="red"):
#     print("stop")
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("look")
# else:
#     print("light is broken")

# age=int(input("enter the age:"))
# if(age <= 17):
#     print("you are a kid")
# elif(age >=18 and age < 60):
#     print("you are a adult")
# else:
#     print("you are senior citizon")


# marks=int(input("enter the marks:"))
# if marks >= 90:
#     print("A")
# elif marks >= 80 and marks < 90 :
#     print("B")
# elif marks >= 70 and marks < 80 :
#     print("C")
# else:
#     print("D")


# food = (input("enter the food:"))
# if (food=="pizza"):
#     print("yes")
# else:
#     print("no")


  #arthamatic operation

# a=10
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)

# # relation operation

# print (a==b)
# print (a!=b)


# name=input("enter your name:")
# age = int(input("enter your age :"))
# marks=float(input("enter your marks:"))

# print("welcome",name)
# print("your age is",age)
# print ("you have scored",marks)

# num1=int(input("enter the number1:"))
# num2=int(input("enter the number2:"))
# sum=num1+num2
# print(sum)

# side=float(input("enter the side of the square:"))
# print("area=",side*side)

# val1=float(input("enter the val1:"))
# val2=float(input("enter the val2:"))
# val=val1+val2/2
# print(val)

# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# if(a>=b):
#     print("true")
# else:
#     print("false")

                    #  lecture-2   
                  #  length
                    
# str1="hello"
# str2="world"
# len1=len(str1)
# print(len1)
# len(str2)
# len2=len(str2)
# print(len2)
# # print(str1+str2)

# str="hello im kushi"

# str[2]
# print(str[2])

# str[6]
# print(str[6])

                          #slicling
  
# str="anaconda"
# print(str[2:5])

# str="alakzander"
# # print(str[3:7])
# print(str[:8]) #print feom starting to 8
# print(str[3:])#print till end


#string-funcations

# str="iam a student in the in oxford  in and learning  in python"
# # print(str.endswith("thon")) endswith is used to check wheather the str has ended with same str or not
# print(str.endswith("end"))
# print(str.capitalize()) # first letter will in capes
# print(str.replace("python","javascript"))# replacese
# print(str.find("m"))

# print(str.count("in"))

# pratice-2

# a=input("enter the name:")
# print(len(a))l

# str="this $ and there are $ in ever $ there $ and all $ have $$$"
# print(str.find("$"))


#conditional-statement

# marks=int(input("enter the marks"))
# if(marks>=90):
#     print("A")
# elif(marks>=90 and marks>=80):
#     print("B")
# elif(marks>= 80 and marks>=70):
#     print("C")
# else:
#   print("D")

# num=int(input("enter the num"))
# if (num% 2==0):
#   print("even number")
# else:
#   print("odd number")

# a=num=int(input("enter the value of a"))
# b=num=int(input("enter the value of b"))
# c=num=int(input("enter the value of c"))
# if (a>b and a>c):
#   print(a,"is gretest number")
# elif(b>a and b>c):
#   print(b,"is gretest number")
# else:
#   print(c,"is gretest number")

# a=num=int(input("enter the value of a"))
# if (a%7==0):
#   print(a,"is multiple of 7")
# else:
#   print(a,"is not multiple of 7 ")



               # chapter-3 list and tuple
              #  list
              
# marks=[78,90,44,59,78,67]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks))
# print(marks[1:5])


# list=[23,35,44,59,77,89]
# list.append(9)
# list=["jai","jyothiba","kushi"]
# list.sort()
# list.sort(reverse=True)
# list.reverse
# print(list)


# pratice

# movies=[]
# mov1=(input("enter the value of mov:"))
# mov2=(input("enter the value of mov:"))
# mov3=(input("enter the value of mov:"))

# movies.append(mov1)
# movies.append(mov2) 
# movies.append(mov3)
   
# print(movies)
 
# list1=[1,2,1]
# list2=[1,2,3]
# copy_list1=list1.copy()
# copy_list1.reverse()


# if(copy_list1==list1):
#     print("palindrom")
# else:
#     print("not a palindrom")

# tuple=["c","d","a","a","b","b","a"]
# print(tuple.sort())


# tuple=["c","d","a","a","b","b","a"]
# tuple.sort()
# print(tuple)


# chapter-4 (dictinary)

# info={
#   "key":"values",
#   "name":"kushi",
#   "class":"bca'4th sem'",
#   "sec":"a",
#   "roll no":"44"
# }
# # print(info)
# print(info["key"])
# print(info["name"])
# print(info["sec"])

# nested object

# students={
#   "name":"kush",
#   "marks":{
#     "eng":"98",
#     "hin":"87",
#     "acc":"90"
#   }
# }
# # print(students)
# print(students["marks"])
# print(students.keys())
# print(list(students.values()))
# print(students.items())


# set:set is a collection of unique number and its immutable its cant be changed and unorderd list

# set={2,59,44,8,9,"haha","kush","kushi"}
# print(set)
# # print(type(set))
# # print(len(set))
# set2={3,44,59,6,7,8}
# print(set2.intersection(set2))


                          # loop in python
#  question-1           
              
# i=1
# while i<=100:
#   print(i)
#   i+=1
 
#  question-2
 
# i=100
# while i>=1:
#   print(i)
#   i-=1
   
#  question-3

# i=1
# n=(input("entwr the value of n:\="))
# while i<=10:
#   print(n*i)
#   i+=1

# question-4

# count=1
# while count <=10:
#   print("hello",count)
#   count+=1
#   # print(count)

# question-5

# n=int(input("enter the value of n:"))
# i=0
# while i<=10:
#   i+=1
#   print(n*i)

# question-6

# num=[1,4,7,6,3,9,4,3,5]
# # print(num[0])
# # print(num[1])
# # print(num[2])
# idx=0
# while idx < len(num):
#   print(num[idx])
#   idx+=1   
    
# question-7
    
# hero=["pet","tom","jerry","max","joe"]
# i=0
# while i < len(hero):
#   print(hero[i])
#   i+=1
  
# question-8

# num=[5,25,44,59,38,89,90,120]  
# i=0
# x=59
# while i<len(num):
#   if (num [i] == x):
#     print("found at idx",i)
#     i+=1
# -----------------------------------------------------------------------------------------
#  for loops
# ~list

# num=[1,2,3,4,5]  
# for val in num:
#   print(val)

# tuple
# tup=[10,20,30,40,50]
# for num in tup:
#   print(num)
  
  # str
# str="apna college"
# for char in str:
#   print(char)
  
  
  # pratice-1
# num=[10,20,30,40,50,60,70,80]
# for ele in num:
#   print(ele)
  
  # pratice-2
  
# num=(10,20,30,40,44,50,59,44,60,60,80,44,59)
# idx=0
# x=44
# for ele in num:
#   if (ele==x):
#     print("found",idx)
#     idx+=1
  
# range
# in rage it starts from 0 and end at -1 foe ex 1-5 it will print 0-4
# print (range(10))

# seq=range(5)
# for i in seq:
#   print(i)
  
# range(start,stop,step)

# for i in range(10):    range(stop)
# print(i)

# for i in range(2,10):   range(start,stop)
#   print(i)

# for i in range(2,10,2):   range(start,stop,size(it will increse by 2))
#   print(i)

# for i in range(2,100,2):
#   print (i)
  
  # pratice-1
# for i in range (1,101):
#   print(i)
  
    
  # pratice-2
# for i in range (100,0,-1):
#   print(i)
  
  # pratice-3
# n = int (input("enter the number:"))
# for i in range (1,11):
#   print(n*i)
  
#   pratice-4
  
# n=7
# sum=0
# for i in range(1,n):
#   sum+=i
#   print("total sum",sum)
  
    # pratice-5
  
# n=7
# fact=0
# for i in range(1,n):
#   fact+=i
#   print("total fact",fact)
  
# --------------------------------------------------------------------------------------------

# funcations in python
# funcations are the block of code that perform specfic task

# def cal_sum(a,b):
#   sum=a+b
#   print(sum)
#   return(sum)

# cal_sum(2,3)
# cal_sum(4,5)
# cal_sum(6,3)

# def print_hello():
#   print("hello")
    
# print_hello()

# def cal_avg(a,b,c):
#   sum=a+b+c
#   avg=sum/3
#   print(avg)
#   return avg

# cal_avg(2,3,4)
# cal_avg(44,59,2)
# cal_avg(5,6,7)

# cities=["banglore","mubai","pune","delhi","noida"]
# heros=["iromman","capital america","thor","halk"]

# def print_len (list):
#   print(len(list))
  
# print(len(cities))
# print(len(heros))



# def cal_fact(n):
#   fact=1
#   for i in range(1, n+1):
#     fact*=i
#   print(fact)

# cal_fact(5)

# a=int(input("enter the valu of a:"))
# b=int(input("enter the valu of b:"))
# def add(a,b):
#   sum=a+b
#   print(sum)
#   return(sum)

# add(a,b)
  
  
  # recursion

def show(n):
  if(n==0):
    return
  print(n)
  show(n-1)
show(5)










































































































































































































