num = input('Enter a number: ')
try:
    i_num = int(num)
except:
    i_num = 'a'

if i_num != 'a':
    print('You enter: ', num)
else:
    print('Not a number')


