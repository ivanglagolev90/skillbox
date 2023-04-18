for number in range(1000): 
    if number > 1: 
        for i in range(2, number): 
            if(number % i) == 0: 
                break 
        else: 
            print(number, end = ', ') 

print()
print()

print(list(filter(lambda n: n > 1 and not any(n % i == 0 for i in range(2,n)), range(1000))))
