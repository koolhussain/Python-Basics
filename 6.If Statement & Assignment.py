x = 5
y = 8
z = 5
a = 3
#if example
if x < y:
    print('X is lesser than y')

if z < y > x:
    print('Y is greatre than Z & X')

if z < y > x > a:
    print('Y is greatre than Z & X')

if z <= x:
    print('z is less than to equal to x')
    
#if else example
if x > y:
    print('X is greater than y')
else:
    print('Y is Greater than X')

#elif examples
x = 5
y = 10
z = 22
#if conditions is true other conditions below them
#are not checked even if they are true
if x > y:
    print('x > y')
elif x < z:
    print('x < z')
elif 5 > 2:
    print('5 > 2')
else:
    print('if and elif never ran')
    
    
