''' You are asked to calculate factorials of some small positive integers.
Input

An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.
#Output

For each integer n given at input, display a line with the value of n!'''

def fact(x):
        ans = 1
        while(x>1):
                ans = ans*x
                x-=1
        return ans               
                
                


tests = int(input())
list = []
for i in range(tests):
       list.append(fact(int(input())))
       
#print(list)
for j in range(len(list)):
        print(list[j])
