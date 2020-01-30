print("--------LARGEST NUMBER USING IF-ELIF-ELSE STATEMENT--------")
a=input("Enter value: ")
b=input("Enter value: ")
c=input("Enter value: ")
if a>b and a>c:
		print(a," is largest")
elif b>c:
		print(b," is largest")
else:
		print(c," is largest")	

print("--------FACTORIAL USING WHILE LOOP--------")
x=int(input("Enter value: "))
i=1
fact=1
while i<=x:
	fact*=i
	i+=1
print(x,"!=",fact)

print("--------FIBONACCI USING IF STATEMENT AND WHILE LOOP--------")
x=int(input("Enter value: "))
f1=0
f2=1 
c=2
if x==1:
	print(f1)
elif x==2:
	print(f1,f2)
else:
	print(f1,f2,end=" ")
	while c<x:
		f=f1+f2
		print(f,end=" ")
		f1=f2
		f2=f
		c+=1
print("")

print("--------MULTIPLICATION TABLE--------")	
n=int(input("Enter value: "))
for i in range(1,11):
	print(n,"x",i,"= ",n*i)

print("--------PASCAL TRIANGLE--------")	

n=int(input("Enter value: "))
for line in range(1,n+1):
	D=1
	print(" "*(n-line),end=" ")
	for i in range(1,line+1):
		print(D,end=" ")
		D=int(D*(line-i)/i)
	print("")
