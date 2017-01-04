def reverse_integer():
    user_input = int(raw_input("Input number: "))
    while user_input is not 0:
        n = user_input % 10
        print n
        user_input = (user_input - n)/10
        #print user_input

reverse_integer()
