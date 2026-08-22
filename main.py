# cheracter check
def char_check(pas):
    l = len(pas)
    if(l>=8):
        return True
    else:
        return False

# Check upper case
def upper_check(pas):
    for char in pas:
        if char.isupper():
            return True

    return False

# Check lower case
def lower_check(pas):
    for char in pas:
        if char.islower():
            return True
    
    return False

# Number check
def num_check(pas):
    for char in pas:
        if char.isdigit():
            return True

    return False

# Special Character
s_char = "@#$&!%"
def special_check(pas):
    for char in pas:
        if char in s_char:
            return True
        
    return False




password = input("Enter your password: ")


tn = char_check(password)
upper = upper_check(password)
lower = lower_check(password)
num = num_check(password)
special = special_check(password)


if(tn and upper and lower and num and special):
    print("Your password is strong.")
else:
    print("Your password is weak.")
