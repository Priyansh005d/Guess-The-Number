import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a!=n):
    guesses +=1
    a = int(input("Guess The Number : "))
    if(a>n):
        print("Lower Number Please")
    elif(a<n):
        print("Higher Number Please")  
print(f"You Guessed the Correct Number {n} in {guesses} attempts")