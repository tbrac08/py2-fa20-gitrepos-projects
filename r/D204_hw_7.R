################################################################################
#  Homwwork assignment 7
###############################################################################

###############################################################################
#   Problem 1a.  Create a trianglular number series producing equilaterial
#   triangles using the formula t = (n**2 + n) / 2 up to 20
###############################################################################

loop_vector <- 1 : 20  # creating vector with the range of numbers

for (index in loop_vector) {
  index = (index**2 + index) / 2
  print(index)
  
}

###############################################################################
#    Problem 1b.  Recreating 1a. with only even numbers
###############################################################################

loop_vector <- 1 : 20

for (index in loop_vector) {
  if (index %% 2 == 0) {            # getting even numbers
    index = (index**2 + index) / 2
    print(index)
    
  }
  
}

################################################################################
#    Problem 1c.  Generate 1a and 1b without using a loop
################################################################################


################################################################################
#   Problem 2a.  Create a vector 1 to 20 and the output is n*3-1 for the 
#   vector
################################################################################

num_vector <- 1:20  #Creating vector for experiment
num_holder <- 1
num_counter <- 1

for (index in num_vector) {
  num_holder = num_counter * 3 - 1 #mult by 3 then - 1
  print(num_holder)                #prints value
  num_counter = num_counter + 1  #increase counter to have process done to next number
  
}

################################################################################
#  2b.  Change all the odd element to even, but leave even alone
################################################################################

num_vector <- 1:20

for (index in num_vector) { #runs through the numbers in the vector
  if(index %% 2 != 0){      #checks to see, if odd
    index = index + 1       #if odd, it adds one
    print(index)
  } else{                   #else not odd, leave alone
    print(index)
  }
  
}

#################################################################################
# Problem 2c.  do without a loop
################################################################################


################################################################################
#  problem 3 import superbowl.csv and have it count the number of super bowl
#  wins each team has and if no super bowl win, display no wins
###############################################################################

#importing super bowl csv
sb_df <- read.csv("c:\\Users\\tpbra\\Desktop\\superbowl.csv", stringsAsFactors = FALSE)

#my_team <- readline(prompt = "Enter in a team name: ") #prompt user for info
#user_value <- readline(prompt = "Enter library name: ")
my_team <- "Green Bay Packers"
print(my_team)
win_total <- 0

sb_winner <-sb_df["Winner"] #gets a list of winners
#print(sb_winner)           #print for debugging purposes


if (win_total <- length(which(sb_winner == my_team))){ #if they have SB wins
  print((win_total))
  cat("Your total Super Bowl win(s) is/are ")
  cat(win_total)
} else{                                                 #no sb wins
  print("Your team has 0 wins")
}
















