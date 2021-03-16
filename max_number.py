def get_max_number():
    a=int(input('Enter the first number:'))
    b=int(input('Enter the second number:'))
    c=int(input('Enter the third number:'))
    if(a==b or b==c or a==c):
        if(a==b):
            print('Have the same number:%d'%(a))
        elif(b==c):
            print('Have the same number:%d' % (b))
        elif(a==c):
            print('Have the same number:%d' % (a))
    else:
        if(a>b and a>c):
            print('The largest number is %d'%(a))
        elif(b>a and b>c):
            print('The largest number is %d' % (b))
        elif(c>a and c>b):
            print('The largest number is %d' % (c))
    return
