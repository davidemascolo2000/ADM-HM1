#!/usr/bin/env python
# coding: utf-8

# # ADM Homework 1
# ## Author: Mascolo Davide
# 
# ### Problem 1 - Introduction 

# In[ ]:


## Ex 1: Say "Hello, World!"
print("Hello, World!")


# In[ ]:


## Ex 2: If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2) != 0 or (n >= 6 and n <= 20):
        print("Weird")
    else:
        print("Not Weird")


# In[ ]:


## Ex 3: Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


# In[ ]:


## Ex 4: Python Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


# In[ ]:


## Ex 5: Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0 , n):
        print(i**2)


# In[ ]:


## Ex 6: Write a Function
def is_leap(year):        
    leap = False
    if (year % 4) == 0:
        if (year % 100) == 0:
                if (year % 400) == 0:
                    leap = True
        else:
            leap = True 
    return leap
year = int(input())
print(is_leap(year))


# In[ ]:


## Ex 7: Print a Function
if __name__ == '__main__':
    n = int(input())
    string = ""
    for i in range(1, n+1):
        string += str(i)
    print(string)


# ### Data Types

# In[ ]:


## Ex 1: List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i = [a for a in range (0, x+1)]
    j = [a for a in range (0, y+1)]
    k = [a for a in range (0, z+1)]  
    newlist = [[x, y, z] for x in i for y in j for z in k if x + y + z != n]
    print(newlist)


# In[ ]:


## Ex 2: Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if n >= 2 and n <= 10:
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input()
    
        for i in student_marks.keys():
            if len(student_marks[i]) < 3 or len(student_marks[i]) > 3:
                raise ValueError("lenght of marks array must be 3")
            else:
                for j in range(0,len(student_marks[i])):
                
                    if student_marks[i][j] < 0 and student_marks[i][j] > 100:
                        raise ValueError("marks[i] must be included between 0 and 100")
                    cnt1 = 0
                    cnt2 = 0
        for i in student_marks.keys():
            if i == query_name:
                for j in student_marks[i]:
                        cnt1 += j
                        cnt2 += 1
        print("{:.2f}".format(cnt1/cnt2))        
    else:
        raise ValueError("marks item must be included between 0 and 100")


# In[ ]:


## Ex 3: Nested Lists
if __name__ == '__main__':
    list_name = list()
    list_score = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_name.append(name)
        list_score.append(score)
    cnt = 0
    while list_score[cnt] == min(list_score):
        cnt += 1
    random = list_score[cnt]
    val = list()
    for i in list_score:
        if i == random:
            val.append(i)
        else:
            if i < random and i > min(list_score):
                random = i
                val2 = list()
                val.append(random)
    val_fin = list()
    for j in range(0, len(list_score)):
        if list_score[j] == random:
            val_fin.append(list_name[j])
    val_fin = sorted(val_fin)
    for i in val_fin:
        print(i)


# In[ ]:


## Ex 4: Find the Runner-Up Score
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lst = list(arr)
    cnt = 0
    if n >=2 and n <= 10:
        while lst[cnt] == max(lst) and cnt <= len(lst) - 1:
            cnt += 1
        second = lst[cnt]
        for i in range(1, len(lst)):
            if lst[i] >= -100 and lst[i] <= 100:
                if lst[i] > second and lst[i] < max(lst):
                    second = lst[i]
            else:
                raise ValueError ("the elements must be included between -100 and 100")
    else:
        raise ValueError ("n must be included between 2 and 10")
    print(second)


# In[ ]:


## Ex 5: Lists
if __name__ == '__main__':
    N = int(input())
    istr = list()
    list1 = list()
    list2 = list()
    for _ in range(N):
        istr.append(input().split())
    for i in range(0, len(istr)):
        if istr[i][0] == "insert":
            list1.insert(int(istr[i][1]), int(istr[i][2]))
        if istr[i][0] == "print":
            print(list1)
        if istr[i][0] == "sort":
            list1.sort()
        if istr[i][0] == "reverse":
            list1.reverse()
        if istr[i][0] == "append":
            list1.append(int(istr[i][1]))
        if istr[i][0] == "remove":
            list1.remove(int(istr[i][1]))
        if istr[i][0] == "pop":
            list1.pop()


# In[ ]:


## Ex 6: Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tupla = tuple(integer_list)
    print(hash(tupla))


# ### Strings

# In[ ]:


## Ex 1: Swap Case
def swap_case(s):
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for i in s:
        if i in s1:
            res += i.upper()
        if i in s2:
            res += i.lower()
        if i not in s1 and i not in s2:
            res += i
    return res  
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[ ]:


## Ex 2: String Split and Join
def split_and_join(line):
    line = line.split()
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# In[ ]:


## Ex 3: What's your Name?
def print_full_name(first, last):
    prt1 = "Hello"
    prt2 = "! You just delved into python."
    print(prt1 + " " + first + " " +  last + prt2)
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[ ]:


## Ex 4: Mutations
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[ ]:


## Ex 5: Find a string
def count_substring(string, sub_string):
    res = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            res += 1 
    return res
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:


## Ex 6: String Validators
if __name__ == '__main__':
    s = input()
    alphanum = alpha = digit = lower = upper = 0
    for i in s:
        if i.isalnum():
            alphanum += 1
        if i.isalpha():
            alpha += 1
        if i.isdigit():
            digit += 1
        if i.islower():
            lower += 1
        if i.isupper():
            upper += 1
    print(alphanum > 0)
    print(alpha > 0)
    print(digit > 0)
    print(lower > 0)
    print(upper > 0)


# In[ ]:


## Ex 7: Text Alignement
thickness = int(input()) #This must be an odd number
c = 'H'
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[ ]:


## Ex 8: Text Wrap
def wrap(string, max_width):
    if len(string) > 0 and len(string) < 1000:
        if max_width > 0 and max_width < len(string):
            res = ""
            for i in range(0, len(string), max_width):
                res += string[i : i + max_width]
                res += "\n"
        else:
            raise ValueError("max_width must be included between 0 and len(string)")
    else:
        raise ValueError("len(string) mjst be incluced between 0 and 1000")        
    return res
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[ ]:


# Ex 9: Designer Door Mat
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


# In[ ]:


## Ex 10: String Formatting
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        for j in ('d', 'o', 'X', 'b'):
            print("{0:{width}{j}}".format(i, j = j, width = width), end=' ')
        print()
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[ ]:


## Ex 11: Alphabet Rangoli
def print_rangoli(size):
    s = "abcdefghijklmnopqrstuvwxyz"
    lc = [s[i] for i in range(n)]   
    items = list(range(n))
    items = items[:-1]+items[::-1]
    for j in items:
        t = lc[-(j+1):]
        row = t[::-1]+t[1:]
        print("-".join(row).center(n*4-3, "-")) 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[ ]:


## Ex 12: Capitalize
import os

def solve(s):
    s = s.split(" ")
    res = ""
    for i in s:
        for j in range(0, len(i)):
            if j == 0:
                res += i[0].upper()                    
            else:
                res += i[j]  
            res += " "
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


# In[ ]:


## Ex 13: The Minion Game
def minion_game(string):
    vow = "AEIOUaeiou"
    A = 0
    B = 0
    for i in range(0, len(string)):
        if string[i] in vow:
            A += len(string) - i
        else:
            B += len(string) - i
    if B > A:
        print("Stuart", B)
    elif B < A:
        print("Kevin", A)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[ ]:


## Ex 14: Merge the Tools!
def merge_the_tools(string, k):
    if len(string) > 0 and len(string) <= 10**4:
        if k >= 1 and k <= len(string):
            d = (len(string) // k)
            c = 0
            inc = k
            while c < len(string):
                res = ""
                res += string[c : k]
                c = k
                k += inc
                res1 = res[0]
                for i in res:
                    if i not in res1:
                        res1 += i
                print(res1)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)            


# ### Sets

# In[ ]:


## Ex 1: Introduction to Sets
def average(array):
    s = set(array)
    return(sum(s) / len(s))
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# In[ ]:


## Ex 2: Symmetric Difference
m = int(input())
set1 = input()
n = int(input())
set2 = input()
set1 = set1.split()
set1 = set(list(map(int, set1)))
set2 = set2.split()
set2 = set(list(map(int, set2)))
res1 = set1.difference(set2)
res2 = set2.difference(set1)
res = sorted(set.union(res1, res2))
for i in res:
    print(i, "\t")


# In[ ]:


## Ex 3: Set Add
a = set()
[a.add(input()) for _ in range(int(input()))]
print(len(a))


# In[ ]:


## Ex 4: Set discard, remove e pop
n = int(input())
s = set(map(int, input().split()))
N = int(input())
istr = list()

for _ in range(N):
    istr.append(input().split())
for i in range(0, len(istr)):
    if istr[i][0] == "discard":
        s.discard(int(istr[i][1]))
    if istr[i][0] == "remove":
        s.remove(int(istr[i][1]))
    if istr[i][0] == "pop":
        s.pop()
print(sum(s))


# In[ ]:


## Ex 5: Set Union
m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))
res = set1.union(set2)
print(len(res))


# In[ ]:


## Ex 6: Set Intersection
m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))
res = set1.intersection(set2)
print(len(res))


# In[ ]:


## Ex 7: Set Difference
m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))
res = set1.difference(set2)
print(len(res))


# In[ ]:


## Ex 8: Set Symmetric Difference
m = int(input())
set1 = set(map(int, input().split()))
n = int(input())
set2 = set(map(int, input().split()))
res = set1.symmetric_difference(set2)
print(len(res))


# In[ ]:


## Ex 9: Set Mutations
_ = int(input())
s1 = set(map(int, input().split()))
N = int(input())
if len(s1) > 0 and len(s1) < 1000:
    if N > 0 and N < 100:
        for _ in range(N):
            istr, _ = input().split()
            s2 = set(map(int, input().split()))
            if len(s2) > 0 and len(s2) < 100:
                if(istr == "intersection_update"):
                    s1.intersection_update(s2)
                if (istr == "update"):
                    s1.update(s2)
                if(istr == "symmetric_difference_update"):
                    s1.symmetric_difference_update(s2)
                if(istr == "difference_update"):
                    s1.difference_update(s2)
print(sum(s1))


# In[ ]:


## Ex 10: The Captain's Room
k = int(input())
s = list(map(int, input().split()))
s.sort()
a = set([s[i] for i in range(0,len(s),2)])
b = set([s[i] for i in range(1,len(s),2)])
print (list(a.symmetric_difference(b))[0])


# In[ ]:


## Ex 11: Check Subset
n = int(input())
for _ in range(n):
    N = int(input())
    sub = set(map(int, input().split()))
    M = int(input())
    s = set(map(int, input().split()))
    print (sub.issubset(s))


# In[ ]:


## Ex 12: Check Strict Superset
sup = set(map(int, input().split()))
n = int(input())
cnt = 0
for _ in range(n):
    s = set(map(int, input().split()))
    if sup.issuperset(s):
        cnt += 1
if cnt == n:
    print(True)
else:
    print(False)


# In[ ]:


## Ex 13: No Idea
n = input().split(' ')
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
cnt = 0
for i in arr:
    if i in a:
        cnt += 1
    if i in b:
        cnt -= 1
print(cnt)


# ### Collections

# In[ ]:


## Ex 1: Collections.Counter
from collections import Counter

n = int(input())
s = list(map(int, input().split()))
m = int(input())
l = list()
res = 0
for _ in range(m):
    ele = list(map(int, input().split()))
    l.append(ele)
for i in range(0, m):
    if l[i][0] in s:
        res += l[i][1]
        s.remove(l[i][0])
print(res)


# In[ ]:


## Ex 2: DefaultDict Tutorial
from collections import defaultdict

s = defaultdict(list)
res = []
n, m = map(int,input().split())
for i in range(1, n+1):
    s[input()].append(str(i))
for i in range(m):
    b = input()
    if b in s:
        print(' '.join(s[b]))
    else:
        print(-1)


# In[ ]:


## Ex 3: Collections.namedtuple
from collections import namedtuple

n = int(input())
col = ",".join(input().split())
Student = namedtuple("Student", col)
num = 0
if n > 0 and n <= 100:        
    for i in range(n):
        row = input().split()
        student = Student(*row)
        num += int(student.MARKS)
    print(num/n)
else:
    raise ValueError("n must be includeed between 0 and 100")


# In[ ]:


## Ex 4: Collections.OrderDict
from collections import OrderedDict

n = int(input())
s = OrderedDict()
if n > 0 and n <= 100:
    for i in range(n):
        item = input().split()
        price = int(item[-1])
        item_name = " ".join(item[:-1])
        if s.get(item_name):
            s[item_name] += price
        else:
            s[item_name] = price
    for i, j in s.items():
        print(i, j)
else:
    raise ValueError("n must be includeed between 0 and 100")


# In[ ]:


## Ex 5: Collections.deque
from collections import deque

n = int(input())
s = deque()
for i in range(n):
    m = list(input().split())
    if m[0] == "append":
        s.append(m[1])
    if m[0] == "pop":
        s.pop()
    if m[0] == "popleft":
        s.popleft() 
    if m[0] == "appendleft":
        s.appendleft(m[1])    
print(*s, sep = " ")


# In[ ]:


## Ex 6: Word Order
n = int(input())
dupl = {}
for i in range(n):
    s = input()
    if s in dupl:
        dupl[s] += 1
    else:
        dupl[s] = 1
print(len(dupl))
for j in dupl:
    print(dupl[j], end = " ")


# In[ ]:


## Ex 7: Company Logo
import math
import os
import random
import re
import sys
from collections import Counter
    
if __name__ == '__main__':
    s = input()
    s = sorted(s)
    res =  Counter(s).most_common()
    res = sorted(res, key = lambda x: (x[1] * -1, x[0]))
    for i in range(0, 3):
        print(res[i][0], res[i][1])


# In[ ]:


## Ex 8: Pilling Up!
for i in range(int(input())):
    input()
    s = [int(i) for i in input().split()]
    minore = s.index(min(s))
    left = s[:minore]
    right = s[minore + 1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")


# ### Date and Time

# In[ ]:


## Ex 1: Calendar Module
import datetime 

y = str(input())
week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']
day = datetime.datetime.strptime(y, '%m %d %Y').weekday()
print(week[day]) 


# In[ ]:


## Ex 2: Time Delta
import math
import os
import random
import re
import sys
import datetime

def time_delta(t1, t2):
    first = datetime.datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z')
    second = datetime.datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    return str(abs(int((first-second).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()


# ### Exceptions

# In[ ]:


## Ex 1: Exceptions
t = int(input())
for i in range(t):
    try:
        a,b= map(int,input().split())
        print(a//b)
    except BaseException as s:
        print("Error Code:", s)


# ### Built-ins

# In[ ]:


## Ex 1: Zipped
n, x = map(int, input().split()) 
res = []
for i in range(x):
    res.append( map(float, input().split())) 
for i in zip(*res): 
    print(sum(i) / x)


# In[ ]:


## Ex 2: Athlete Sort
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    res = sorted(arr, key = lambda x: x[k])
    for i in res:
        print(*i) 


# In[ ]:


## Ex 3: ginortS
s = input()
res = []
even = []
odd = []
for i in s:
    if i.islower() or i.isupper():
        res.append(i)
        res = res[::-1]
        res.sort(key = lambda i:(not i.islower(), i))
    if i.isdigit():
        if int(i) % 2 != 0:
            odd.append(i)
        if int(i) % 2 == 0:
            even.append(i)
for i in res:
    print(i, end = "")
for i in sorted(odd):
    print(i, end = "")
for i in sorted(even):
    print(i, end = "")


# ### Python Functionals

# In[ ]:


## Ex 1: Map and Lambda Functions
cube = lambda x: pow(x, 3)

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    seq = [0,1]
    for i in range(2, n):
        num = seq[-1] + seq[-2]
        seq.append(num)
    return seq
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# ### Regex and Parsing

# In[ ]:


## Ex 1: Detect Floating Point Number
def is_float(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

m = int(input())
l = [input().strip() for _ in range(m)]
for i in l:
    if(i == '0'): print(False)
    else:
        print(is_float(i))


# In[ ]:


## Ex 2: Re.split
regex_pattern = r"[.,]"
import re
print("\n".join(re.split(regex_pattern, input())))


# In[ ]:


## Ex 3: Group, Groups & Groupdict
import re

m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)


# In[ ]:


## Ex 4: Re.findall & Re.finditer
import re

v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))


# In[ ]:


## Ex 5: Re.start & Re.end
S = input()
k = input()
import re

pattern = re.compile(k)
r = pattern.search(S)
if not r: 
    print ("(-1, -1)")
while r:
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)


# In[ ]:


## Ex 6: Validating Roman Numerals
import re
regex_pattern = r"^M{,3}(C(D|M)|D?C{,3})(X(L|C)|L?X{,3})(I(X|V)|(X|V)?I{,3})$"
print(str(bool(re.match(regex_pattern, input()))))


# In[ ]:


## Ex 7: Validating Phone Numbers
import re

[print('YES' if re.match(r'[789]\d{9}$',input()) else 'NO') for _ in range(int(input()))]


# In[ ]:


## Ex 8: Validating and Parsing Email Addresses
import re

n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)


# In[ ]:


## Ex 9: Hex Color Code
import re

pattern = r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for x in re.findall(pattern,input()):
        print(x)


# In[ ]:


## Ex 10: HTML Parser - Part 1
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
MyParser = MyHTMLParser()
MyParser.feed(''.join([input().strip() for _ in range(int(input()))]))


# In[ ]:


## Ex 11: HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment  ", data, sep="\n")
        else:
            print(">>> Single-line Comment  ", data, sep="\n")
    def handle_data(self, data):
            if data != "\n":
                print(">>> Data", data, sep="\n")
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[ ]:


## Ex 12: Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[ ]:


## Ex 13: Validating UID
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')


# In[ ]:


## Ex 14: Regex Substitution
for _ in range(int(input())):
    line = input() 
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    print(line)


# In[ ]:


## Ex 15: Validating Credit Card Numbers
import re

for _ in range(int(input())):
    s = input()
    if re.match(r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$", s) and not re.search(r"([\d])\1\1\1", s.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")


# In[ ]:


## Ex 16: Validating Postal Codes
import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# In[ ]:


## Ex 17: Matrix Script
import math
import os
import random
import re
import sys

n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))


# ### XML

# In[ ]:


## Ex 1: XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return len(node.attrib) + sum([get_attr_number(i) for i in node])
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


# In[ ]:


## Ex 2: XML 2 - Find the Maximum Depth
import xml.etree.ElementTree as etree
global maxdepth

maxdepth = -1
def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1
    for i in elem:
        depth(i, level + 1)
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


# ### Closures and Decorators

# In[ ]:


## Ex 1: Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(c[-10:-5], c[-5:]) for c in l)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


# In[ ]:


## Ex 2: Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


# ### Numpy 

# In[ ]:


## Ex 1: Arrays
import numpy

def arrays(arr):
    arr = arr[::-1]
    arr = numpy.asarray(arr, dtype = numpy.float64)
    return arr  
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# In[ ]:


## Ex 2: Shape and Reshape
import numpy

s = numpy.array(list(map(int,input().split())))
s.shape = (3, 3)
print(s)


# In[ ]:


## Ex 3: Transpose and Flatten
import numpy

n, m = map(int, input().split())
i = numpy.array([input().strip().split() for _ in range(n)], int)
print(i.transpose())
print(i.flatten())


# In[ ]:


## Ex 4: Concatenate
import numpy

n, m, p = map(int, input().split())
res1 = numpy.array([input().split() for _ in range(n)], int)
res2 = numpy.array([input().split() for _ in range(m)], int)
print(numpy.concatenate((res1, res2), axis = 0))


# In[ ]:


## Ex 5: Zeros and Ones
import numpy

n = list(map(int, input().split()))
print(numpy.zeros(n, dtype = numpy.int))
print(numpy.ones(n, dtype = numpy.int))


# In[ ]:


## Ex 6: Eye and Identity
import numpy

numpy.set_printoptions(legacy = "1.13")
n, m = map(int, input().split())
print(numpy.eye(n, m))


# In[ ]:


## Ex 7: Array Mathematics
import numpy

n, m  = list(map(int, input().split()))
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(*[eval("a"+ i + "b") for i in ["+", "-", "*", "//", "%", "**"]], sep='\n')


# In[ ]:


## Ex 8: Floor, Ceil and Rint
import numpy

numpy.set_printoptions(legacy = "1.13")
a = numpy.array(input().split(), float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


# In[ ]:


## Ex 9: Sum and Prod
import numpy

n, m = map(int, input().split())
a = numpy.array([input().split()for _ in range(n)], int)
print(numpy.prod(a.sum(axis = 0)))


# In[ ]:


## Ex 10: Min and Max
import numpy

n, m = map(int, input().split())
a = numpy.array([input().split()for _ in range(n)], int)
print(max(a.min(axis = 1)))


# In[ ]:


## Ex 11: Mean, Var and Std
import numpy

n, m = map(int, input().strip().split())
arr = numpy.array([input().strip().split() for _ in range(n) ], int)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr, axis = None), 11))


# In[ ]:


## Ex 12: Dot and Cross
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n) ], int)
b = numpy.array([input().split() for _ in range(n) ], int)
print(a @ b)


# In[ ]:


## Ex 13: Inner and Outer
import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print(numpy.inner(a, b))
print(numpy.outer(a, b))


# In[ ]:


## Ex 14: Polynomials
import numpy

c = list(map(float,input().split()))
x = input()
print(numpy.polyval(c, int(x)))


# In[ ]:


## Ex 15: Linear Algebra
import numpy

numpy.set_printoptions(legacy='1.13')
n = int(input())
a = numpy.array([input().strip().split() for _ in range(n)], float)
print(numpy.linalg.det(a))


# ### Problem 2 - Challenges 

# In[ ]:


## Ex 1: Birthday Cake Candles
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    s = candles
    res = s.count(max(s))
    return res
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()


# In[ ]:


## Ex 2: Number Line Jumps
import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        if (x1 - x2) % (v2 - v1) == 0:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()


# In[ ]:


## Ex 3: Viral Advertising
import math
import os
import random
import re
import sys

def viralAdvertising(n):
    c = 5
    cnt = 0
    for _ in range(0,n):
        liked = c//2
        c = liked * 3
        cnt = cnt + liked
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()


# In[ ]:


## Ex 4: Recursive Digit Sum
import math
import os
import random
import re
import sys

def superDigit(n, k):
    x = (int(n) * int(k)) % 9
    return x or 9    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()


# In[ ]:


## Ex 5: Insertions Sort - Part 1
import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = i
        while pos > 0 and val < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
            print(*arr, sep = " ")
        arr[pos] = val
    print(*arr, sep = " ")
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)


# In[ ]:


## Ex 6: Insertion Sort - Part 2
import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        pos = i
        while pos > 0 and val < arr[pos - 1]:
            arr[pos] = arr[pos - 1]
            pos -= 1
        arr[pos] = val
        print(*arr, sep= ' ')

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

