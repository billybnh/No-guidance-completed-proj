from art import logo
from art import vs
from game_data import data
from replit import clear
import random

current_score = 0

#Compare followers
def compare_followers(current_score):
  random.shuffle(data)
  for i in range (0, len(data)):
    if current_score == 0:
      first_com = data[-2]
    elif i%2==1:
      first_com = third_data
    else:
      first_com = data[i-2]
    second_com = data[i-1]
    #compare first_com to second_com
    print(f'Compare A: {first_com["name"]}, {first_com["description"]}, from {first_com["country"]}.')
    print(vs)
    print(f'Against B: {second_com["name"]}, {second_com["description"]}, from {second_com["country"]}.')
    answer =input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a" and first_com["follower_count"] > second_com["follower_count"]:
      current_score += 1
    elif answer == "b" and second_com["follower_count"] > first_com["follower_count"]:
      current_score +=1
    elif answer == "a" and first_com["follower_count"] < second_com["follower_count"]:
      return current_score
    elif answer == "b" and second_com["follower_count"] < first_com["follower_count"]:
      return current_score
    else:
      return current_score
    third_data = data[i-1]
    clear()
    print(logo)
    print(f"You're right! Current score: {current_score}.")

#End game
def end_game(current_score):
  clear()
  print(logo)
  if current_score < 48:
    print(f"Sorry that's wrong. Final score: {current_score}")
  else:
    print("Congratulation on scoring 48! You have beaten the game!")
  

print(logo)

current_score = int(compare_followers(current_score))
end_game(current_score)
