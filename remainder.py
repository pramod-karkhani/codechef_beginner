 '''Write a program to find the remainder when two given numbers are divided.
Input

The first line contains an integer T, total number of test cases. Then follow T lines, each line contains two Integers A and B.
Output

Find remainder when A is divided by B.
Constraints

    1 ≤ T ≤ 1000
    1 ≤ A,B ≤ 10000

'''
def rem(a,b):
        return a%b
        
                
        

test = int(input())
list = []
for i in range(test):
        x,y = map(int, input().split())
        list.append(rem(x,y))

for i in range(len(list)):
        print(list[i])
