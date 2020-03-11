#! python3

def meth1(n):
    t =(1,2,3,3,4,2,2,9,8)

    print('Original tuple is ')
    print(t)

    for i in sorted(t):
        print('Only sorted below:')
        print(i)
	

    for j in sorted(set(t)):
        print('Sorted and setted..i.e removed duplicates.')
        print(j)

meth1(22)
