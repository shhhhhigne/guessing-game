def is_even(num):
    if num % 2 == 0:
        return True
    return False


def show_evens(lst):
    evens = []
    for i, x in enumerate(lst):
        if is_even(x):
            evens.append(i)
    print evens


show_evens([1, 2, 3, 4])
