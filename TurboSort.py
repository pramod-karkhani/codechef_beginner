'''Input

t – the number of numbers in list, then t lines follow [t <= 10^6].
Each line contains one integer: N [0 <= N <= 10^6]
Output

Output given numbers in non decreasing order.
'''
test = int(input())
list = []
for i in range(test):
        list.append(int(input()))
list.sort()
for i in range(len(list)):
        print(list[i])
