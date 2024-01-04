# Defines a function to prompt user for input 
def get_input (word_type: str):
    # Gets user input and stores it in a variable
    user_input: str = input(f"Enter a {word_type}: ")
    # Returns the user input
    return user_input

# Calls get_input() to get a noun from the user 
noun = get_input('noun')
# Calls get_input() to get a verb from the user
verb = get_input('verb')
# Calls get_input() to get a second noun from the user
noun2 = get_input('noun2')
# Calls get_input() to get a second verb from the user
verb2 = get_input('verb2')
# Creates a story string using the user input
story = f"""
 Once upon a time there was a {noun} who loved to {verb} all day .
  one day {noun2} walked into room of {noun} and caught him in an shameless act 

  {noun2}: "What are you doing? "
  {noun}: "i am just {verb}ing what's the big deal?"
  {noun2}: "Well, its not every day that you see a {noun} {verb}ing in the middle of the day. "
  {noun} : "I guess you are right. may be i should take a break."
  {noun2}: "That's probably a good idea why don"t we go {verb2} instead?"
  {noun}: " Sure, that sounds like a fun"
And so , {noun2} and {noun} went off to {verb2} and had a great time . 
"""

print(story)