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
#line
def line(n,char):
    if char=="":
        print("*"*n)
    else:
        print(char[0]*n)
if __name__ == "__main__":
    line(5, "x")
#box_of_hashes
def line(b,a):
    print(a*b)
def box_of_hashes(n):  # You should call function line here with proper parameters
    while n>0:
        line(10, "#")
        n-=1
if __name__ == "__main__":
    box_of_hashes(5)
#square_of_hashes
def line(b,a):
    print(a*b)
def square_of_hashes(n):
    k=n
    while n>0:
        line(k, "#")
        n-=1
if __name__ == "__main__":
    square_of_hashes(5)
#square
def line(b,a):
    print(a*b)
def square(n, m):
    k=n
    while n>0:
        line(k, m)
        n-=1
if __name__ == "__main__":
    square(5, "x")
#triangle
def line(a,b):
    print(b*a)
def triangle(n):
    i=1
    while i<=n:
        line(i, "#")
        i+=1
if __name__ == "__main__":
    triangle(5)
#shape
def line(a,b):
    print(b*a)
def shape(k,x,l,y):
    i=1
    while i<=k:
        line(i,x)
        i+=1
    while l>0:
        line(k,y)
        l-=1
if __name__ == "__main__":
    shape(5, "x", 2, "o")
#spruce
def spruce(n):
    print("a spruce!")
    s="*"
    i=1
    while i<=n:
        print(" "*(n-i)+s*(2*i-1))
        i+=1
    print(" "*(n-1)+s)
if __name__ == "__main__":
    spruce(5)
#greatest_number
def greatest_number(a,b,c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    elif c>=a:
        if c>=b:
            return c
        else:
            return b
    elif b>=c:
        if b>=a:
            return b
        else:
            return a
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
#same_char
def same_chars(ar, i, j):
    if i>=len(ar) or j>=len(ar):
        return False
    if ar[i]==ar[j]:
        return True
    else:
        return False
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
#1st2ndlast
def first_word(s):
    return s.split()[0]
def second_word(s):
    return s.split()[1]
def last_word(s):
    return s.split()[-1]
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
#change_value
a=[1,2,3,4,5]
while True:
    i=int(input("Index: "))
    if i == -1:
        break
    x=int(input("New value: "))
    a[i]=x
    print(a)
#add_items
n=int(input("How many items: "))
a=[]
for i in range(n):
    x=int(input(f"Item {i+1}: "))
    a.append(x)
print(a)
#addition_removal
list=[]
print(f"The list is now {list}")
while True:
    operation=input("a(d)d, (r)emove or e(x)it: ")
    if operation=="x":
        break
    if len(list)==0:
        if operation=="d":
            list.append(1)
            print(f"The list is now {list}")
    else:
        if operation=="d":
             list.append(list[-1]+1)
        elif operation=="r":
             list.pop(-1)
        print(f"The list is now {list}")
print("Bye!")
#same_word_twice
list=[]
while True:
    x=input("Word: ")
    if x in list:
        break
    list.append(x)
print(f"You typed in {len(list)} different words")
#list_twice
list=[]
while True:
    x=int(input("New item: "))
    if x==0:
        break
    list.append(x)
    print("The list now:", list)
    print("The list in order:", sorted(list))
print("Bye!")
#lenoflist
def length(a):
    x=len(a)
    return x
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)
#mean
def mean(a):
    m=(sum(a))/len(a)
    return m
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)
#rangeoflist
def range_of_list(a):
    mx=max(a)
    mn=min(a)
    return mx-mn
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
#star_studded
str=input("Please type in a string: ")
for char in str:
    print(char)
    print("*")
#negative to positive
n=int(input("Please type in a positive integer: "))
for i in range(-n,n+1):
    if i==0:
        continue
    else:
        print(i)
#list_of stars
def list_of_stars(list):
    for i in list:
        print("*"*i)
if __name__=="__main__":
    list=list(input())
#anagrams
def anagrams(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        return True
    else:
        return False
if __name__=="__main__":
    # s1=input()
    # s2=input()
    print(anagrams(s1,s2))
#palindromes
def palindromes(a):
    b=''.join(reversed(a))
    if b==a:
        return True
    else:
        return False
    return x
while True:
    a=input("Please type in a palindrome: ")
    if palindromes(a)==True:
        print(f"{a} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
#sum_of_positives
def sum_of_positives(list):
    sum=0
    for i in list:
        if i>0:
            sum+=i
    return sum
if __name__=="__main__":
    print("The result is", sum_of_positives(list))
#even_numbers
def even_numbers(a):
    even=[]
    for i in a:
        if i%2==0:
            even.append(i)
    return even
if __name__=="__main__":
    even_numbers(list)
#sum_of_lists
def list_sum(l1,l2):
    sum=[]
    for i in range(len(l1)):
        sum.append(l1[i]+l2[i])
    return sum
if __name__=="__main__":
    list_sum(list1,list2)
#distinct_numbers
def distinct_numbers(a):
    b=set(a)
    b=list(b)
    return sorted(b)
if __name__=="__main__":
    distinct_numbers(list)
#length of longest
def length_of_longest(a):
    l=0
    for i in a:
        if len(i)>l:
            l=len(i)
    return l
if __name__=="__main__":
    length_of_longest(list)
#shortest in list
def shortest(a):
    l=100
    for i in a:
        if len(i)<l:
            l=len(i)
            x=i
    return x
if __name__=="__main__":
    shortest(list)
#all_longest in list
def all_the_longest(a):
    list=[]
    l=0
    for i in a:
        if len(i)>l:
            l=len(i)
    for i in a:
        if len(i)==l:
            list.append(i)
    return list
if __name__=="__main__":
    all_the_longest(list)
#everything reversed
def everything_reversed(a):
    l1=[]
    i=len(a)-1
    while i>=0:
        l1.append(''.join(reversed(a[i])))
        i-=1
    return l1
if __name__=="__main__":
    everything_reversed(list)
#most common character
def most_common_character(a):
    n=0
    for i in range(len(a)):
        if a.count(a[i])>n:
            n=a.count(a[i])
            x=a[i]
    return x
if __name__=="__main__":
    most_common_character(str)
#no vowels allowed
def no_vowels(str):
    str=str.replace("a","")
    str=str.replace("e","")
    str=str.replace("i","")
    str=str.replace("o","")
    str=str.replace("u","")
    return str
if __name__=="__main__":
    a=input()
    no_vowels(a)
#no shouting allowed
def no_shouting(a):
    l1=[]
    for i in range(len(a)):
        if a[i].isupper()==False:
            l1.append(a[i])
    return l1
if __name__=="__main__":
    no_shouting(list)
#neighbours in list
def longest_series_of_neighbours(a):
    b=1
    result=1
    for i in range(1,len(a)):
            if abs(a[i]-a[i-1])==1:
                b+=1
            else:
                if b>result:
                    result=b
                b=1
    if b>result:
         result=b
    return result
if __name__=="__main__":
    print(longest_series_of_neighbours(list))
#PART_4_ADDED
#longest_string
def longest(list):
    max=0
    for a in list:
        if len(a)>max:
            max=len(a)
            A=a
    return A
if __name__=="__main__":
    longest(str)
#number of elements
def count_matching_elements(a,x):
    res=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==x:
                res+=1
    return res
if __name__=="__main__":
    count_matching_elements(m,x)
#go
def who_won(l):
    c1=0
    c2=0
    for row in l:
        for item in row:
            if item==1:
                c1+=1
            elif item==2:
                c2+=1
    if c1>c2:
        return 1
    elif c2>c1:
        return 2
    else:
        return 0
if __name__=="__main__":
    who_won(list)
#sudoku row
def row_correct(l,n):
    l1=[]
    for i in l[n]:
        if i==0:
            continue
        elif i in l1:
            return False
        elif i<1 or i>9:
            return False
        else:
            l1.append(i)
    return True
if __name__=="__main__":
    row_correct(li,num)
#sudoku column
def column_correct(l,c):
    l1=[]
    for row in l:
        if row[c]==0:
            continue
        elif row[c] in l1:
            return False
        elif row[c]<1 or row[c]>9:
            return False
        else:
            l1.append(row[c])
    return True
if __name__=="__main__":
    column_correct(sudoku,colm)
#items_multiplied_by_two
def double_items(l):
    new_list=[]
    for i in l:
        new_list.append(2*i)
    return new_list
if __name__=="__main__":
    double_items(list)
#remove smallest
def remove_smallest(l):
    a=l[0]
    for b in l:
        if b<a:
            a=b
    l.remove(a)
    print(l)
if __name__=="__main__":
    remove_smallest(li)
#times ten
def times_ten(a,b):
    dicti={}
    for i in range(a,b+1):
        dicti[i]=i*10
    return dicti
if __name__=="__main__":
    print(times_ten(x,y))
#factorials
def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res
def factorials(a):
    dicti={}
    for i in range(1,a+1):
        dicti[i]=factorial(i)
    return dicti
if __name__=="__main__":
    print(factorials(x))
#histogram
def histogram(str):
    num={}
    for a in str:
        if a in num:
            num[a]+=1
        else:
            num[a]=1
    for key in num:
        print(f"{key} {"*"*num[key]}")
if __name__=="__main__":
    histogram(x)
#phonebook 1
pb={}
while True:
    com=int(input("command (1 search, 2 add, 3 quit): "))
    if com==3:
        break
    elif com==2:
        name=input("name: ")
        num=input("number: ")
        pb[name]=num
        print("ok!")
    else:
        name=input("name: ")
        if name not in pb:
            print("no number")
        else:
            print(pb[name])
print("quitting...")
#invert_dictionary
def invert(d):
    inverted={}
    for key in d:
        inverted[d[key]]=key
    d.clear()
    d.update(inverted)
if __name__=="__main__":
    print(invert(dictionary))
#movie database
def add_movie(l,n,d,y,t):
    dic={}
    dic["name"]=n
    dic["director"]=d
    dic["year"]=y
    dic["runtime"]=t
    l.append(dic)
if __name__=="__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)
#find movies
def find_movies(l,s):
    res=[]
    for dic in l:
        if s.lower() in dic["name"].lower():
            res.append(dic)
    return res
if __name__=="__main__":
    my_movies = find_movies(database, "python")
    print(my_movies)
#create tuple
def create_tuple(x,y,z):
    l=[]
    a=[1,2,3]
    l.append(x)
    l.append(y)
    l.append(z)
    a[0]=min(l)
    a[1]=max(l)
    a[2]=x+y+z
    t=tuple(a)
    return t
if __name__=="__main__":
    print(create_tuple(a,b,c))
#oldest person
def oldest_person(li):
    l=[]
    for tup in li:
        l.append(tup[1])
    m=min(l)
    for tup in li:
        if tup[1]==m:
            return tup[0]
if __name__=="__main__":
    oldest_person(list)
#older people
def older_people(li,ye):
    l1=[]
    for tup in li:
        if tup[1]<ye:
            l1.append(tup[0])
    return l1
if __name__=="__main__":
    older_people(list,year)
# PART 5 ADDED
#PART 6 STARTS
#inscription
name = input("Whom should I sign this to: ")
filename = input("Where shall I save it: ")

    # Inscription content
inscription = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
try:
    with open(filename, "w") as file:
        file.write(inscription)
    print(f"The inscription has been saved to {filename}.")
except Exception as e:
    print(f"An error occurred while saving the file: {e}")
#diary
def add_entry(filename):
    """Add a diary entry to the file."""
    entry = input("Diary entry: ")
    with open(filename, "a") as file:
        file.write(entry + "\n")
    print("Diary saved")

def read_entries(filename):
    """Read and display all diary entries."""
    print("Entries:")
    try:
        with open(filename, "r") as file:
            entries = file.readlines()
            for entry in entries:
                print(entry.strip())
    except FileNotFoundError:
        print("No entries yet.")

"""Main diary program loop."""
filename = "diary.txt"
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")
    if function == "1":
        add_entry(filename)
    elif function == "2":
        read_entries(filename)
    elif function == "0":
        print("Bye now!")
        break
    else:
        print("Invalid option, please try again.")
#word_search
def find_words(search_term: str):
    """Find words matching the search term with wildcard functionality."""
    matching_words = []
    
    with open("words.txt", "r") as file:
        words = [line.strip() for line in file]
    
    if '*' in search_term:
        # Handle asterisk wildcard
        if search_term.startswith('*'):
            suffix = search_term[1:]
            matching_words = [word for word in words if word.endswith(suffix)]
        elif search_term.endswith('*'):
            prefix = search_term[:-1]
            matching_words = [word for word in words if word.startswith(prefix)]
    elif '.' in search_term:
        # Handle dot wildcard
        from re import fullmatch
        regex_pattern = search_term.replace('.', '.')
        matching_words = [word for word in words if fullmatch(regex_pattern, word)]
    else:
        # Exact match
        matching_words = [word for word in words if word == search_term]
    
    return matching_words
if __name__ == "__main__":
    print(find_words("*vokes"))  # Example search term with wildcard
    print(find_words("ca."))    # Example search term with dot wildcard
    print(find_words("python")) # Example exact match
#read_input
def read_input(st,a,b):
    while True:
        try:
            num=input(st)
            num=int(num)
            if a<num and num<b:
                return num
            else:
                print(f"You must type in an integer between {a} and {b}")
        except ValueError:
            print(f"You must type in an integer between {a} and {b}")
if __name__=="__main__":
    read_input(s,x,y)
#parameter validation
def new_person(name: str, age: int):
    # Validate the name
    if not name.strip():
        raise ValueError("Name cannot be an empty string.")
    if len(name.split()) < 2:
        raise ValueError("Name must contain at least two words.")
    if len(name) > 40:
        raise ValueError("Name cannot exceed 40 characters.")

    # Validate the age
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age cannot exceed 150.")
    return (name, age)
if __name__ == "__main__":
    person = new_person(s,i)  
#incorrect_lottery_numbers
def is_valid_line(line):
    week_pattern = r'^week \d+;'
    number_pattern = r'(\d+,){6}\d+$'
    if not re.match(week_pattern, line.split(";")[0] + ";"):
        return False
    try:
        week, numbers = line.strip().split(";")
        week_number = int(week.split()[1])
        if week_number <= 0:  # Week number must be positive
            return False
        numbers = [int(num) for num in numbers.split(",")]
    except (ValueError, IndexError):
        return False
    if len(numbers) != 7:
        return False
    if not all(1 <= num <= 39 for num in numbers) or len(numbers) != len(set(numbers)):
        return False
    return True
def filter_incorrect():
    input_file = "lottery_numbers.csv"
    output_file = "correct_numbers.csv"
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if is_valid_line(line):
                    outfile.write(line)
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    filter_incorrect()
#PART 6 ADDED
#PART 7 STARTS
#hypotenuse
from math import *
def hypotenuse(l1,l2):
    a=sqrt((l1**2)+(l2**2))
    return a
if __name__=="__main__":
    print(hypotenuse(n,m))
#special_characters
import string
def separate_characters(st):
    le=""
    pu=""
    ot=""
    for char in st:
        if char in string.ascii_letters:
            le+=char
        elif char in string.punctuation:
            pu+=char
        else:
            ot+=char
    return le,pu,ot
if __name__=="__main__":
    parts=separate_characters(Str)
    print(parts[0])
    print(parts[1])
    print(parts[2])
#fractions
from fractions import Fraction
def fractionate(n):
    li=[]
    for i in range(n):
        li.append(Fraction(1,n))
    return li
if __name__=="__main__":
    print(fractionate(a))
#lottery_numbers
from random import sample
def lottery_numbers(x,a,b):
    ss=list(range(a+1,b))
    lottery=sample(ss,x)
    lottery.sort()
    return lottery
if __name__=="__main__":
    lottery_numbers(p,q,r)
#how_old
from datetime import datetime, timedelta
d=int(input("Day: "))
m=int(input("Month: "))
y=int(input("Year: "))
dob=datetime(y, m, d)
millenium=datetime(2000, 1, 1)
age=millenium-dob
if age.days<1:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {age.days-1} days old on the eve of the new millennium.")
#string_helper
import re
def change_case(st):
    return st.swapcase()
def split_in_half(st):
    n=len(st)
    return st[:n//2], st[n//2:]
def remove_special_characters(st):
    return re.sub('[^a-zA-Z0-9\s]', '', st)
if __name__=="__main__":
    print(change_case("Well hello there!"),end=" ")
#PART 7 ADDED







