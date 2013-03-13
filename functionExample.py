# Okay, here's a function. Let's save this for another time.
def feet_to_inches(feet):
    return (feet * 12)

# Time to print! Immediately print this stuff to the screen.
print("I'm a program that converts feet to inches.")
print("How many feet would you like to convert?")

# Oh! An equals sign! We always evaluate the right side first during
# assignment, so let's start there.
# (talking about the right side now:)
# Oh! Parentheses! We always evaluate inside out when we see
# parentheses, so let's start at the innermost expression (input()).
# input()! We know what that means, because when the interpreter
# started, it loaded a bunch of code for us (the code that's built
# into Python, not code _you_ wrote). One of those functions that was
# saved for later was input(). So we know that it waits for user
# input, and returns the string that the user entered. Now since it's
# a String, and we're trying to do math with it, and you can't really
# do math with Strings, we convert it to an Integer. So we call int(),
# which Python also already knows about. That int() function is called
# with one parameter: the string that the user entered. It attempts to
# convert it to a number, and if so, returns an Integer. Now that the
# right side is completely evaluated, we store the result in the
# 'feet' variable, which Python saves for later (just. like.
# functions!)
feet = int(input())

# Alrighty! I spy more parentheses! Time to go inside out again...
# So we have the function 'feet_to_inches' called with one parameter:
# feet. Since feet is inside the parentheses, we evaluate that first.
# We look up that variable, and sure enough! We know what it is. We
# assigned a string to it on the previous line of code. So we replace
# 'feet' with the Integer it represents. Then we call 'feet_to_inches'
# with that Integer. Oh look! We know what 'feet_to_inches' is all
# about too, because we stored that away at the very beginning of the
# program. So know we look up its implementation, and do what it says.
# It says to multiply the given variable by 12, and return it. So if
# it's given 3, it returns 36. So the entire 'feet_to_inches(feet)'
# call is replaced by 36. Then we're asked to add 6 to that number, so
# that evaluates to 42. Then, and only then, do we replace the %r in
# the string with the number 42, and then we print the whole string to
# the screen.
print("Here's the equivalent inches, plus another 6: %r" % (feet_to_inches(feet) + 6))

# And that's allllll folks.
