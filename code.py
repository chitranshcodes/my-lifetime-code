# print("chitransh")
# i just want to check if the code is getting updated or not
# i think now i know how to push and commit changes on gitbash
word=input("Please type in a word: ")
length=len(word)
if length>1:
    print(f"There are {length} letters in the word {word}")
print("Thank you!").
num=float(input("Please type in a number: "))
int_part=int(num)
print(f"Integer part: {int_part} \nDecimal part: {num-int_part}".
print("Person 1:")
name1=input("Name: ")
age1=int(input("Age: "))
print("Person 2: ")
name2=input("Name: ")
age2=int(input("Age: "))
if age1>age2:
    print("The elder is", name1)
elif age2>age1:
    print("The elder is", name2)
else:
    print(f"{name1} and {name2} are the same age").
first=int(input("Please type in the first number: "))
second=int(input("Please type in the second number: "))
if first>second:
    print("The greater number was:", first)
elif first<second:
    print(f"The greater number was: {second}")
else:
    print("The numbers are equal!").
word1=input("Please type in the 1st word: ")
word2=input("Please type in the 2nd word: ")
if word1>word2:
    print(f"{word1} comes alphabetically last.")
elif word2>word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.").
age=int(input("What is your age? "))
if 0<=age<5:
    print("I suspect you can't write quite yet...")
elif age>=5:
    print(f"Ok, you're {age} years old")
elif age<0:
    print("That must be a mistake").
name=input("Please type in your name: ")
if name=="Huey" or name=="Dewey" or name=="Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name=="Morty" or name=="Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.").
points=int(input("How many points [0-100]: "))
if points<0 or points>100:
    print("Grade: impossible!")
elif 0<=points<=49:
    print("Grade: fail")
elif 50<=points<=59:
    print("Grade: 1")
elif 60<=points<=69:
    print("Grade: 2")
elif 70<=points<=79:
    print("Grade: 3")
elif 80<=points<=89:
    print("Grade: 4")
elif 90<=points<=100:
    print("Grade: 5")
num=int(input("Number: "))
if num%5==0 and num%3==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
year=int(input("Please type in a year: "))
if year%100==0:
    if year%400==0:
        print("That year is a leap year.")
    else:
        print("That year is not a leap year.")
elif year%4==0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
l1=input("1st letter: ")
l2=input("2nd letter: ")
l3=input("3rd letter: ")
if l1<l2<l3:
    print(f"The letter in the middle is {l2}")
elif l2<l1<l3:
    print(f"The letter in the middle is {l1}")
elif l3<l1<l2:
    print(f"The letter in the middle is {l1}")
elif l3<l2<l1:
    print(f"The letter in the middle is {l2}")
else:
    print(f"The letter in the middle is {l3}")
value=int(input("Value of gift: "))
if value<5000:
    print("No tax!")
elif 25000>value>=5000:
    print(f"Amount of tax: {100+((value-5000)*0.08)}")
elif 25000<=value<55000:
    print(f"Amount of tax: {1700+((value-25000)*0.1)}")
elif 55000<=value<200000:
    print(f"Amount of tax: {4700+((value-55000)*0.12)}")
elif 200000<=value<1000000:
    print(f"Amount of tax: {22100+((value-200000)*0.15)}")  
else:
    print(f"Amount of tax: {142100+((value-1000000)*0.17)}")
while True:
    print("hi")
    a=input("Shall we continue? ")
    if a=="no":
        break
print("okay then")
from math import sqrt
while True:
    num=int(input("Please type in a number: "))
    if num==0:
        break
    if num<0:
        print("Invalid number")
    else:
        print(sqrt(num))
print("Exiting...")
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number== 0:
    break

print("Now!")
pw=input("Password: ")
while True:
    rpw=input("Repeat Password: ")
    if rpw!=pw:
        print("They do not match!")
    else:
        break
print("User account created!")
tpin=4321
attempts=0
while True:
    pin=int(input("PIN: "))
    attempts +=1
    if pin==tpin:
        break
    else:
        print("Wrong")
if attempts==1:
    print("Correct! It only took you one single attempt!")

else:
    print(f"Correct! It took you {attempts} attempts")
year=int(input("Year: "))
nyear=year
while True:
    nyear+=1
    if (nyear%4==0 and nyear%100!=0) or (nyear%400==0):
        break
print(f"The next leap year after {year} is {nyear}")
line=""
word=""
while True:
    last_word=word
    word=input("Please type in a word")
    if word=="end" or word==last_word:
        break
    line+=word+" "
print(line)
count=0
sum=0
pcount=0
ncount=0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num=int(input("Number: "))
    if num==0:
        break
    count+=1
    sum+=num
    if num<0:
        ncount+=1
    elif num>0:
        pcount+=1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {sum/count}")
print(f"Positive numbers {pcount}")
print(f"Negative numbers {ncount}")
n=2
while n<=30:
    if n%2==0:
        print(n)
    n+=1
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
      print(number)
      number-=1
print("Now!")
num=1
ul=int(input("Upper limit: "))
while num<ul:
    print(num)
    num+=1
ul=int(input("Upper limit: "))
num=1
while num<=ul:
    print(num)
    num*=2
ul=int(input("Upper limit: "))
num=1
base=int(input("Base: "))
while num<=ul:
    print(num)
    num*=base
limit=int(input("Limit: "))
sum=0
n=1
while sum<limit:
    sum+=n
    n+=1
print(sum)
str=input("Please type in a string: ")
n=int(input("Please type in an amount: "))
print(str*n)
str1=input("Please type in string 1: ")
str2=input("Please type in string 2: ")
l1=len(str1)
l2=len(str2)
if l1>l2:
    print(f"{str1} is longer")
elif l1==l2:
    print("The strings are equally long")
else:
    print(f"{str2} is longer")
str=input("Please type in a string: ")
n=len(str)-1
while n>=0:
    print(str[n])
    n-=1
str=input("Please type in a string: ")
a=str[1]
b=str[-2]
if a==b:
    print("The second and the second to last characters are", str[1])
else:
    print("The second and the second to last characters are different")
n=int(input("Width: "))
print("#"*n)
l=int(input("Width: "))
m=int(input("Height: "))
n=0
while n<m:
    print("#"*l)
    n+=1
while True:
    str=input("Please type in a string: ")
    if str=="":
        break
    print(str)
    print("-"*len(str))
str=input("Please type in a string: ")
n=len(str)
l=20-n
print("*"*l+ str)
str=input("Word: ")
n=len(str)
if n%2==0:
    l=28-n
    gap=int(l/2)
    print("*"*30)
    print("*"+" "*gap + str + " "*gap + "*")
    print("*"*30)
else:
    l=28-n
    gap=int(l/2)
    print("*"*30)
    print("*"+" "*(gap+1) + str + " "*gap + "*")
    print("*"*30)
str=input("Please type in a string")
n=len(str)-1
m=0
while m<=n:
    print(str[0:m])
    m+=1
print(str[0:m+1])
str=input("Please type in a string")
n=len(str)-1
m=n
while m>=0:
    print(str[m:])
    m-=1
str=input("Please type in a string: ")
if "a" in str:
    print("a found")
else:
    print("a not found")
if "e" in str:
    print("e found")
else:
    print("e not found")
if "o" in str:
    print("o found")
else:
    print("o not found")
str=input("Please type in a word")
l=input("Please type in a character")
n=str.find(l)
if (len(str)-1)-n<2:
    print("")
else:
    print(str[n:n+3])
n=int(input("Please type in a number: "))
i=1
while i<=n:
    j=1
    while j<=n:
        print(f"{i} x {j} = {i*j}")
        j+=1
    i+=1
while True:
    num=int(input("Please type in a number: "))
    if num<=0:
        break
    i=1
    fact=1
    while i<=num:
        fact*=i
        i+=1
    print(f"The factorial of the number {num} is {fact}")
print("Thanks and bye!")
num=int(input("Please type in a number: "))
i=1
while i<=num:
    if i+1 <=num:
        print(i+1)
        print(i)
        i+=2
    else:
        print(i)
        i+=1
n=int(input("Please type in a number: "))
i=1
j=n
while i<=j:
    if i==j:
        print(i)
    else:
        print(i)
        print(j)
        
    i+=1
    j-=1
def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")
if __name__ == "__main__":
     seven_brothers()
def mean(x,y,z):
    print((x+y+z)/3)
if __name__ == "__main__":
    mean(1, 2, 3)
def print_many_times(text, times):
    i=0
    while i<times:
        print(text)
        i+=1
if __name__ == "__main__":
    print_many_times("python", 5)
def hash_square(n):
    i=0
    while i<n:
        print("#"*n)
        i+=1
if __name__ == "__main__":
    hash_square(5)
def chessboard(x):
   n=0
   i=int(x/2)
   while n<x:
       if n%2==0:
           if x%2==0:
               print("10"*i)
           else:
               print("10"*i+"1")
       else:
           if x%2==0:   
               print("01"*i)
           else:
               print("01"*i+"0")
       n+=1
if __name__ == "__main__":
    chessboard(3)
def squared(str,n):
    i=0
    j=0
    str=str*100000
    while i<n:
        print(str[j:j+n])
        j+=n
        i+=1
if __name__=="__main__":
    squared("ab",3)
# PART  3  OVER


