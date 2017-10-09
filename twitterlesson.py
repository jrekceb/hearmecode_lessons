# Difficulty Level: Beginner
# Exercise: Tweet length calculator

# Part one:
# Create a variable called tweet and put some text in it
#   maybe something like "Hear Me Code class was so much fun today!"

tweet = """Being a teaching assitant at Hear Me code is so fufilling.
 I hope to one day actually teach lesson 1 lalallallalall"""

allowed_characters = 140

# Measure the length of that tweet.

tweet_character_count = len(tweet)

if tweet_character_count > 140:
	print "This tweet has reached the character limit. You need to remove {0} characters".format(tweet_character_count - allowed_characters)
else:
	print "You are so witty and brief because you have {0} characters left to use in your tweet".format(allowed_characters - tweet_character_count)

# Was that tweet more than 140 characters?
#   If so, tell the user it was too long!
# Was that tweet 140 or fewer characters?
#   If so, tell the user how witty they are!


# Part two:
# Adjust the program to say how many characters you have remaining to use, or how many you need to trim by in order to meet the 140 character limit


# Part three:
# Twitter announced they are changing their character limit to 280, but they might change it again.
# Can you make your code flexible enough so that you don't have to replace the character limit in multiple places in your code?