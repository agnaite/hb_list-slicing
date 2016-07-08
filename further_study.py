from list_operations import *

# Further Study / Extra Credit
# ----------------------------
#
# In this section you will implement your own versions of the standard list methods.
# You should use only the primitive operations from Part 1 and 2 in your implementations.
# For loops are also allowed, such as the following:
#     for element in some_list:
#         # Do something with element
#
# Each custom method imitates a built-in list method, as described by the docstring
# for each function. Play with the built-in methods in the Python REPL to get a feel
# for how they work before trying to write your custom version.


def custom_len(input_list):
    """
    like len(input_list), should return the number of items in the list

    For example:

    >>> custom_len(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
    8

    """

    return 0


# For the next four exercises, you'll need to be clever and think about ways
# to use "list slice assignment" to solve these problems.
#
# NOTE: these are especially contrived--for example, you wouldn't really want
# to typically append things to a list like this (you'd want to to use the
# list.append() method), but we want you to practice list slicing assignment
# in different ways so it sticks in your brain.


def custom_append(input_list, value):
    """
    like input_list.append(value), should add the value to the end of the list
    and return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> custom_append(notes, 'Re')
    >>> notes == ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do', 'Re']
    True

    """

    pass


def custom_extend(input_list, second_list):
    """
    like input_list.extend(second_list), should append every item in the second
    list to the end of the first list and return nothing

    For example:

    >>> months = ['Jan', 'Feb', 'Mar']
    >>> custom_extend(months, ['Apr', 'May'])
    >>> months == ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    True

    """

    pass


def custom_insert(input_list, index, value):
    """
    like input_list.insert(index, value), should insert (not replace) the value
    at the specified index of the input list and return nothing

    For example:

    >>> months = ['Jan', 'Mar']
    >>> custom_insert(months, 1, 'Feb')
    >>> months == ['Jan', 'Feb', 'Mar']
    True

    """

    pass


def custom_remove(input_list, value):
    """
    like input_list.remove(value), should remove the first item of the
    value specified and return nothing

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> custom_remove(notes, 'Do')
    >>> notes == ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    True

    """

    pass


def custom_pop(input_list):
    """
    like input_list.pop(), should remove the last item in the list and
    return it

    For example:

    >>> custom_pop(['Jan', 'Feb', 'March'])
    'March'

    """

    return None


def custom_index(input_list, value):
    """
    like input_list.index(value), should return the index of the first item
    which matches the specified value

    For example:

    >>> custom_index(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Re')
    1

    """

    return 0


def custom_count(input_list, value):
    """
    like input_list.count(value), should return the number of times the specified
    value appears in the list.

    For example:

    >>> custom_count(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Do')
    2

    """

    return 0


def custom_reverse(input_list):
    """
    like input_list.reverse(), should reverse the elements of the original list
    and return nothing (we call this reversing "in place")

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> custom_reverse(multiples)
    >>> multiples == [27, 24, 21, 18, 15, 12, 9, 6, 3, 0]
    True

    """

    pass


def custom_contains(input_list, value):
    """
    like (value in input_list), should return True if the list contains the
    specified value and False if it does not. Remember, do not use the `if X in Y`
    statement -- find another way to solve it!

    For example:

    >>> custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 23)
    False

    >>> custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 24)
    True

    """

    return None


def custom_equality(some_list, another_list):
    """
    like (some_list == another_list), should return True if both lists contain
    the same values in the same indexes

    For example:

    >>> custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Feb', 'Mar'])
    True

    >>> custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Mar', 'Feb'])
    False

    """

    return None


##############################################################################
# END OF EXTRA CREDIT
#
# Please ask for a code review. Also, give your partner a high-five!

##############################################################################
# This is the part were we actually run the doctests.

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
