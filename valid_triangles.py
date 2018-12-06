*** Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
Input

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains three angles A, B and C of triangle separated by space.
Output

Display 'YES' or 'NO' if the triangle is Valid or not respectively.
***

t = int(input())
for i in range(t):
	ans = sum(list(map(int , input().split())))
	if ans==180:
		print("YES")
	else:
		print("NO")

