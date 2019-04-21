def Fibonacci(sequence,first_term,second_term):
    fibo_list = [first_term,second_term]
    if sequence < 2:
        return '???'
    elif sequence == 2:
        try:
            return float(fibo_list[sequence-1] / fibo_list[sequence-2])
        except ZeroDivisionError:
            return '???'
    else:
        i = 1
        while (i < sequence-1):
            i += 1
            fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
        return float(fibo_list[i] / fibo_list[i-1])

fibo_index = int(input('Enter a positive integer: '))
fibo_first = int(input('How about the first term of a sequence? '))
fibo_second = int(input('And how about the second one? '))
print('Your desired ratio is', Fibonacci(fibo_index,fibo_first,fibo_second))