# This script is Lab 1 for Python Programming
#We will calculate the volume of runoff for a agricultural plot

#Prompt user for plot dimensions
print "Hello, let's calculate how much runoff is escaping your plot?"

#These lines set user-provided inputs as the variables for calculations. Each line creates a string variable. It then uses the raw_input function to print a questions for the user and stores they're inputs as the variables. I also used \n to print the questions with more spacing to make it easier to read.

#Prompt for plot length
length = raw_input("\nWhat is the length of your plot in feet? Enter a number. >>\n")

#Convert input (feet) to inches. And change it to an intger so we can do math. 
plot_length = int(length)*12

#Prompt for plot width 
width = raw_input("\nWhat is the width of your plot in feet? Enter a number. >>\n")

#Convert input to inches. Convert it to integer.
plot_width = int(width)*12

#Prompt for rainfall in inches
rainfall_inches = raw_input("\nHow many inches of rain fell in the past storm? Enter a number. >>\n")

#Print statement for fun
print "\nOkay, let me do some calculations... hmm.. \n"

#Calculate the plot's area. To do math, we must first convert the stored variables to integers (from string)
area_plot = plot_length*plot_width

#Calculate rainfall volume. Convert rainfall to an integer value.
rainfall_volume = area_plot*int(rainfall_inches)

#Print rainfall volume. We must reconvert the variables to string so that they can contcatenate them.
print "\nLooks like the rainfall volume was " + str(rainfall_volume) + " cubic inches. But what is that in gallons? Gah. I haven't done this conversion since elementary school. Let me Google the conversion factor real quick.\n"

#Convert cubic volume to gallons
runoff_gallons = int(rainfall_volume)/231

#Print the total area
print "\nLooks like " + str(runoff_gallons) + " gallons fell on your plot. Woah, that's a lot.\n"

#Print all the variables 
print "So, just to summarize -- \nyour plot length was " + str(length) + " feet. \nThe width was " + str(width) + " feet. \nThe rainfall in inches was " + str(rainfall_inches) + " inches. \nFinally,this made " + str(runoff_gallons) + " gallons of runoff."