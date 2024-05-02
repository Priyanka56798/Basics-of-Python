str_1 ='hello world'
list_1=[3,6,2,8]
list_2=[5,3,7,4]

print(str_1.capitalize())
print(list_1.reverse())
print(sorted(list_2))


program:8
list_1=[]
str_1=input()
sum=0
for each_char in str_1:
    if(each_char.isdigit()):
        list_1.append(each_char)
        sum=sum + int(each_char)
        
print(list_1)
print(sum)

