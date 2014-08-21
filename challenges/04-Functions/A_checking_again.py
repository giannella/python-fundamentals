# We applied the same logic many times in the previous challenge!
# Let's use functions to make our lives easier...

sally_age = 12
john_age = 21

def can_drink(age):
    if age > 20:
        return True
    elif age < 21:
        return False # Again - make this depend on the age!

print "Sally can drink?", can_drink(sally_age)
print "John can drink?", can_drink(john_age)

# Now define a more complex function that takes whether someone is drinking and
# only checks ages if they are

def enforce(name, age, is_drinking):
    # Replace "pass" with some logic to test things out
    print "Checking " + name + "!"
    if age < 21:
        if is_drinking == True:
            print "This isn't right!"
        else:
            print "OK!"
    else:
        print "OK!"

    # When you check,
    # print "Checking Name!"
    # (you'll need to set the name)
    # Then print "OK!" or "This isn't right!" as appropriate.

# Note that we can define our data before or after a function

alice_name = "Alice"
alice_age = 20
alice_is_drinking = True
bob_name = "Bob"
bob_age = 12
bob_is_drinking = False
charles_name = "Charles"
charles_age = 22
charles_is_drinking = True

#enforce(alice_name, alice_age, alice_is_drinking)
#enforce(bob_name, bob_age, bob_is_drinking)
#enforce(charles_name, charles_age, charles_is_drinking)
# And so on - do this for Bob and Charles!

# That should've been a LOT less typing!

# When you're done, have a look at the tests, and see how they correspond to the
# functions above
