"""
https://www.hackerrank.com/challenges/find-a-string
language: Python 3

Sample Input

ABCDCDC
CDC

Sample Output

2
"""


str1=input()
str2=input()

num=0

for i in range(len(str1)):
    if str1[i:].startswith(str2):
        num+=1

print(num)
