# Movie Ratings

## Tasks

# complete following the pseudo code:

# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.


#Hint: Draw out what's communicating with what.

## Acceptance Criteria

# Program follow all business logic
# Program runs continuously, and exits on the word exit
# program does not break with integer or strings

while True:
    rating = str(input("What film rating would you like information for?  "))
    if rating == "universal":
        print("Everyone can watch.")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "pg":
        print("General viewing, but some scenes may be unsuitable for young children")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "12":
        print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
        rating = str(input("What other film rating would you like information for?  "))
    elif rating == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
        rating = str(input("What other film rating would you like information for?  "))
    else:
        print("We could not give you information for this rating, please try again.")
        rating = str(input("What film rating would you like information for?  "))
    if rating == "exit":
        exit()