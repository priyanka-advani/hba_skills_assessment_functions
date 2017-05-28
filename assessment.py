"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def is_hometown(town):
    """Takes a town and returns True only if town is my hometown (San Francisco)"""

    return town == "San Francisco"


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def full_name(first_name, last_name):
    """Takes a first and last name and returns it as one full name"""

    return "{} {}".format(first_name, last_name)


#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.


def greeting(town, first_name, last_name):
    """Takes a town, a first name, and a last name and returns a greeting
    based on whether or not the person is from my hometown (San Francisco)"""

    name = full_name(first_name, last_name)

    if is_hometown(town):
        print "Hi, {}, we're from the same place!".format(name)

    else:
        print "Hi {}, I'd like to visit {}!".format(name, town)
        

###############################################################################

# PART TWO
#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    return fruit.lower() in ["strawberry", "raspberry", "blackberry"]


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit):
        return 0
    else:
        return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    return lst + [num]


def calculate_price(item_price, state, tax_rate=0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    # calculate item total
    item_tax = item_price * tax_rate
    item_total = item_price + item_tax

    # for CA, add 3% recycling fee to item total
    if state == "CA":
        item_total += (item_total * 0.03)

    # for PA, add $2 highway safety fee to item total
    elif state == "PA":
        item_total += 2

    # for MA, add Commonwealth Fund fee to item total
    # $1 for items under $100
    # $3 for items $100 or more
    elif state == "MA":
        if item_price < 100:
            item_total += 1
        else:
            item_total += 3

    return item_total


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.


def append_multiple_args(lst, *args):
    """Takes a list and any number of additional arguments and returns the list
    with all additional arguments appended"""

    # iterate through arguments and append each to the list
    for arg in args:
        lst.append(arg)

    return lst


#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


def outer(word):
    """Takes a word and returns a tuple of the original word and the original
    word multiplied by 3"""

    def inner(word):
        """Takes a word and returns that word multiplied by 3"""

        return word * 3

    return (word, inner(word))


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
