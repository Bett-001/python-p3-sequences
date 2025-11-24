
def print_fibonacci(n):
    if n <= 0:
        print([])  # print empty list for 0 or negative
        return
    elif n == 1:
        print([0])
        return
    
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    print(fib_list)
