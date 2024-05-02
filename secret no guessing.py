secret_num=33
condition=True
while(condition):
    n=int(input())
    if(n == secret_num):
        print("congratualations!you guessed it right")
        condition=False
    elif(n>secret_num):
        print("Number too large")
    elif(n<secret_num):
        print("Number too small")
    elif(n <= 0):
        condition=False
        print("Am qutting the game")
