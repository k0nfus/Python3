for num in range(1, 21):
    if num == 4 or num == 13:
        print(str(num) + " is unlucky")
    else:
        if num % 2:
            print(str(num) + " is odd")
        else:
            print(str(num) + " is even")