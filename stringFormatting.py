#converts the age variable to a string, cannot concatonate strings and integers
age = 24
print('My age is ' + str(age) + ' years')
#handy way to type if you have a lot of data or code
print('My age is {0} year'.format(age))
#example when we need to use multiple replacement fields
print('There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}'.format(31, 'January', 'March', 'May', 'July', 'August', 'October', 'December'))

#2d allocates 2 spaces, 4d allocates 4 spaces, ** 2 = to the 2nd power and 3 is cubed
for i in range(1,12):
    print('No, %2d squared is %4d and cubed is %4d' % (i, i ** 2, i ** 3))

#formatting numbers...this is using python 2 formatting
print('Pi is approximately %12f' % (22 / 7))
print('Pi is approximately %12.50f' % (22 / 7))

#formatting with python 3
for i in range(1,12):
    print('No, {0:2} squared is {1:4} and cubed is {2:4}'.format(i, i ** 2, i ** 3))