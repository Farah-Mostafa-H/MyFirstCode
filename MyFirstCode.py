t=[]
new_list=[]
num=int(input("Enter a positive integer(or a non-positive integer to stop):"))
while num>0 :
    t.append(num)
    num=int(input("Enter a positive integer(or a non-positive integer to stop):"))
for i in range(len(t)):
    if i % 2!=0:
        new_list.append(i*2)
    else:
        new_list.append(i*2)
the_original_list=tuple(t)
print(f"the original tuple:{the_original_list}")
print(f"New list:{new_list}")