from random import randint
print("guessing Heads or Tails game started")
score = 0
n = int(input("No. of round you want to play"))
b = n
def flipcoin():
    a = ["Heads" , "Tails"]
    computer = a[randint(0,1)]
    return computer

while n>0:
    user_guess = input("Heads or Tails").lower()
    if user_guess == "heads" or user_guess == "tails":
        coin = flipcoin()
        if coin.lower() == user_guess:
            print("Good guess!")
            score = score + 1
        else:
            print("Better luck next time")
    else:
        print("wrong choice! Either write Heads or Tails")
        n = n+1
    n = n-1
print("Your score:" ,score, "out of" ,b)
