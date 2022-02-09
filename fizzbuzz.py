def fizzbuzz(num):
    for i in range(num+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            continue
        elif i % 3 == 0:
            print("fizz")
            continue
        elif i % 5 == 0:
            print('buzz')
            continue
        print(i)


fizzbuzz(50)
