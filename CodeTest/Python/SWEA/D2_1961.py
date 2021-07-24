def te(*args):
    count = 0
    for arg in args:
        print(type(arg), arg)
        count += 1
    print(count)

te(*list([1,2,3,4]))