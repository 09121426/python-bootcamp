# int
#float
#string
#boolean
#tuple
#sets
#list
#dictinory
print ("sridevi womens enginerring college")
print ("Deekshitha")
a="Python"
print ("hello",a)
b=input("enter your name\n") 
print ("gud mrng",b)
Name="deekshi"
age="20"
print(f"hello {Name} you are {age} years")
#sub1,sub2,sub3,sub4,sub5=list(map(int(input().split(','))))
sub1=10   #s1=int(input())
sub2=20
sub3=22
sub4=23
sub5=19
sum=sub1+sub2+sub3+sub4+sub5
avg=sum//5
name="deekshi"    #name=input()
print(f"hii {name} your sum is {sum} and your average is {avg}")      #print(f"hii {name} your sum is {(s1+s2+s3)} and your average is {(s1+s2+s3)//3}")
# conditional statements: we will check for conditions
#conditions are : if elif else
c=int(input())
if (c<18):
    print("you are not eligible")
else:
    print("you are eligible")    
name=input()
age=int(input())
if age<18:
    print(f"hello {name} not eligible for voting")
else:
    print(f"hello {name} eligible for voting")  



'''Prime number using half iteration

import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
number = int(input())
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")'''



''' palindrome or not 
n=int(input())
temp=n
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if(temp==s):
    print("palindrome")
else:
    print("not an palindrime")'''


''' armstrong number
n = int(input())
s=n
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")'''


'''sum of num
n=int(input())
sum=0
for i in range(0,n+1):
    sum=sum+i 
print(sum)'''


'''sum=0    
num=int(input("Enter a number:"))   
temp=num    
while(num):  
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("Given number is a strong number")  
else:  
    print("Given number is not a strong number")'''
