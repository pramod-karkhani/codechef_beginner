a = list(input().split(' '))

x=int(a[0])
y=float(a[1])
if x<=y-.50 and x%5==0:
    y=y-x-0.5

print("%.2f" %y)
