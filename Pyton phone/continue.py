while True:
    line = input('> ')
    if line[0] == '#':
        continue #to go to the top of the loop
    if line == 'done':
        exit() # terminate the program
    print(line)
print('Done')