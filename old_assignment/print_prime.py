for number in range(1,100):

    for j in range(2, number):
        if (number % j) == 0:
            break

    else:
        print(number)



