def prime(num1,num2):
    prime_lst =[]
    for num in range(num1,num2):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                prime_lst.append(num)

    return prime_lst
    

print(prime(10,30))