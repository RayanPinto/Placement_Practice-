s="Hello World"
s1=s.split(" ")
print(s1)
x,y=s1

ch,ch1=list(x),list(y)
chh=sorted(ch,key=lambda x:x.lower())
chh1=sorted(ch1,key=lambda y:y.lower())
print(chh,chh1)
str1="".join(chh)
str2="".join(chh1)
str=str1+" "+str2
print(str)