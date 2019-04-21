def Fibonacci(sequence):
    fibo_list = [0,1]
    if sequence < 1:
        return '???'
    elif sequence < 3:
        return fibo_list[sequence-1]
    else:
        i = 1
        while (i < sequence-1):
            i += 1
            fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
        return fibo_list[i]

fibo_index = int(input('Enter a positive integer: '))
print('Your desired Fibonacci number is', Fibonacci(fibo_index))