# --------------
#Code starts here
import sys
def palindrome(num):
  numstr = str(num)
  for i in range(num+1,sys.maxsize):
      if str(i) == str(i)[::-1]:
          return i
print(palindrome(1331))          



# --------------
#Code starts here

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) 
    
    return (result)

                  

print(a_scramble("baby shower","shows"))
print(list("Tom Marvolo Riddle"))


# --------------
#Code starts here
import math
def checkPerfectSquare(num):
    sqrt = int(math.sqrt(num))
    if pow(sqrt, 2) == num:
        return True
    else:
        return False

def check_fib(num):
    res1 = 5 * num * num + 4
    res2 = 5 * num * num - 4
    if checkPerfectSquare(res1) or checkPerfectSquare(res2):
        return True
    else:
        return False
print(check_fib(377))   


# --------------
#Code starts here
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

print(compress("ssggtts"))
 


# --------------
#Code starts here
def k_distinct(string,k):
    s_list=(set(string.lower()))
    return len(s_list)>=k

print(k_distinct('Messoptamia',8))


