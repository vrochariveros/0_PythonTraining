"""
Learning Python
Area Calculator
"""

print ("Calculator is waking up...")

#variable will determine if program should be running or not 
isRunning = True

while isRunning == True:
    option = input("Please enter C for Circle or T for Triangle: ").lower()
    
    if option == 'c': 
      radius = float(input("Enter radius: "))
      area = 3.14159 * radius**2
      print("Area:" + str(area))
      #print "Area: %f" % area
    elif option == "t":
      base = float(input("Please enter the base of the triangle: "))
      height = float(input("Please enter the height of the triangle: "))
      area = 0.5 * base * height
      print("Area:" + str(area))
      #print "Area: %f" % area
    else:
      print ("Invalid input")
    
    # closing option A
    userContinue = input("Just so you know, I'm still existing. Do you wish to continue? Type Y for yes N for no: ").lower()

    if userContinue == 'n':
      isRunning = False

    # closing option B 
    # note: userContinue() should be defined outside of while loop because otherwise it gets called constantly within the loop
    # def userContinue(): #define the function
    #    response = input("Just so you know, I'm still existing. Do you wish to continue? Type Y for yes N for no: ").lower() #define response variable and assign value from calling input
    #    return response #returning response (variable) value

    # if userContinue() == 'n': #if the value this function returns is n
    #     isRunning = False #then we assign this variable

print("Okay, I'll go back to sleep now...")