from art import logo
from art import vs
from game_data import data
import random
print(logo)

score=0
game_should_continue=True

account_b=random.choice(data)
#make the game repeatable
while game_should_continue:
    #Generate a random accounut from the game data.
    account_a=account_b
    account_b=random.choice(data)  
    if account_a == account_b:
        account_b=random.choice(data)
      
    def account_format(account):
        
        
        """format the account data into printable format."""
        account_name=account["name"]
        account_description=account["description"]
        account_country=account["country"]
        return f"{account_name}, a {account_description},from {account_country}"

    def check_answer(guess,a_followers,b_followers):
        """check if user is correct.  """
        if a_followers>b_followers:
            return guess=="a"
        elif a_followers<b_followers:
            return guess =="b"


    
    print(f"Compare A:{account_format(account_a)}")
    print("vs")
    print(f"Against B:{account_format(account_b)}")
    #ask user for a guess.
    guess= input("Who has more followers? Type 'A' or 'B': ").lower()

    #get follower count of each account.
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    is_correct= check_answer(guess,a_follower_count,b_follower_count)
    #Give user feedback on their guess.
    if is_correct:
        score+=1
        print(f"you are right. Your Score is {score}")
    else:
        game_should_continue=False
        print(f"Sorry you are wrong. your final score is {score}")



    #score keeping.
    
    #making account at position B become the next account at position A.
    #clear the screen between rounds.

      

