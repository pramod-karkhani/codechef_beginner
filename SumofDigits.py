'''You're given an integer N. Write a program to calculate the sum of all the digits of N.
Input

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.
Output

Calculate the sum of digits of N.
Constraints

    1 ≤ T ≤ 1000
    1 ≤ N ≤ 1000000
'''


def sumof(x):
        sum=0
        while(x!=0):
                dig = x%10
                sum += dig
                x=x//10
        return sum        

test = int(input())
list = []
for i in range(test):
        list.append(int(input()))
for i in list:
        print(sumof(i))
