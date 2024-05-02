password=input()
alpha_count=0
special_count=0
numeric_count=0
for each_chr in password:
    if(('A'<=each_chr and each_chr<='Z') or ('a'<=each_chr and each_chr<='z')):
        alpha_count=alpha_count+1
    elif('0' <= each_chr and each_chr <= '9'):
        numeric_count=numeric_count +1
    else:
        special_count=special_count+1
if(alpha_count==5 and numeric_count==3 and special_count==1):
    print("valid password")
else:
    print("Invalid password") 

