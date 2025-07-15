len=int(input("enter the lenght of the arr"))
arr=[]
i=0
for i in range(len):
   num=int(input("enter the element"))
   arr.append(num)

for i in range(len):
    if arr[i]%2==0:
       print("even")
    else: print("odd")

