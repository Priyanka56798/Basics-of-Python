s="united arab emirates"
l=s.split(' ')
print(l)
rev_list=[]
rev_list=l[::-1]
print(rev_list)

program:11
def cal_area(r,pi=3.14):
    ans=pi*r*r
    return ans
r=int(input())
print(cal_area(r))
