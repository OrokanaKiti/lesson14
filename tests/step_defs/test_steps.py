#Author - Sammie - Date 11/21/2019
#Description- This is a happie~ program designed to test the Retire.py program located in a higher folder than this program~ please enjoy
#
# Version-----------------------------------
# 0.07
#
# TODO--------------------------------------
# [X] Imported pytest_bdd correctly
# [X] comment setup correctly
# [X] Auto fill correctly
# [X] Layout and ensure auto fill correctly setup everything correctly
# [X] properly name all methods
# [] Figure out how to properly paramaterize the main function
# [] Get Scenario Setup Correctly
# [] Get Scenario Functioning with pytest
# [] Get Scenario Outlines Functioning with examples
# [] Get normal outlines working with pytest
# [X] Create Git hub Repository = "https://github.com/OrokanaKiti/lesson14"
# [X] Attach Travis CI
# [] Ensure Program mostly accceptable [Finished polished product]
# -------------------------------------------

from pytest_bdd import scenarios, parsers, given, when, then
from Retire import *

# ----------------------------------------------------------------------
#  Setup Code ~ ♫
# ----------------------------------------------------------------------

#Setup Scenario thingy #(commented for use later)#
#@scenario('..tests/Features/display.feature', 'Setup')
#def scenario_main():
#    pass

#The Given Tag for setup (Might be utilized later)
@given("calculator starts up normaly with no input yet and intro screen displays")
def test_setup():

    print("Nothing Given")


# ----------------------------------------------------------------------
# Scenario Outline Code ~ ♫
# Scenario Outline Code ~ ♫
# ----------------------------------------------------------------------

@when("user enters <num1> & <num2>")
def test_outline_input():
    raise NotImplementedError(u'STEP: When	user enters <num1> & <num2>')


@then("returns year <result> + month <result2> for obtaining full benefits")
def test_outline_assert():
    raise NotImplementedError(u'STEP: Then	returns year <result> + month <result2> for obtaining full benefits')
    assert true

# ----------------------------------------------------------------------
# regular test statements Code ~ ♫
# ----------------------------------------------------------------------

@when('user enters "13" into the month option and a year')
def test_rounder_input():

    sample13 = calculate_retirement_date(1957,12,62,13)
    #raise NotImplementedError(u'STEP: When	user enters "13" into the month option and a year')
    return sample13

@then("the program should at +1 to the year, then restart the month at 1")
def test_rounder_assert():
    raise NotImplementedError(u'STEP: Then	the program should at +1 to the year, then restart the month at 1')
    assert (test_rounder_input() == (2020,1))     #based on original setup of ver .07 of this program this  should return false

# ----------------------------------------------------------------------

@when("user enters something that is not a number")
def test_not_num_input():
    raise NotImplementedError(u'STEP: When	user enters something that is not a number')


@then('program should throw "Input not accepted" and offer to restart execution')
def test_not_num_assert():
    raise NotImplementedError(u'STEP: Then	program should throw "Input not accepted" and offer to restart execution')
    assert true

# ----------------------------------------------------------------------

@when("user enters something that is more characters than expected")
def test_too_much_input():
    raise NotImplementedError(u'STEP: When	user enters something that is more characters than expected')

@then('then program should throw "incorrect input" and offer to restart execution')
def test_too_much_assert():
    raise NotImplementedError(u'STEP: Then	then program should throw "incorrect input" and offer to restart execution')
    assert true

#@then program should throw "incorrect input" and offer to restart execution

# ----------------------------------------------------------------------

@when("user enters something that is less characters than expected")
def test_too_little_input():
    raise NotImplementedError(u'STEP: When	user enters something that is less characters than expected')

@then('program should throw "incorrect input" and offer to restart execution')
def test_too_much_assert():
    raise NotImplementedError(u'STEP: Then	program should throw "incorrect input" and offer to restart execution')
    assert true

#@then program should throw "incorrect input" and offer to restart execution

# ----------------------------------------------------------------------

@when("user hits enter without inputing anything")
def test_nothing_input():
    raise NotImplementedError(u'STEP: When	user hits enter without inputing anything')

@then('program should throw "no input detected" and offer to restart execution')
def test_nothing_assert():
    raise NotImplementedError(u'STEP: Then	program should throw "no input detected" and offer to restart execution')
    assert true

#@then program should throw "no input detected" and offer to restart execution

# ----------------------------------------------------------------------

@when('user enters something that is before "1900" for the date born')
def test_not_yet_input():
    raise NotImplementedError(u'STEP: When	user enters something that is before "1900" for the date born')

@then('program should throw "sorry too old" and offer to restart execution')
def test_not_yet_assert():
    raise NotImplementedError(u'STEP: Then	program should throw "sorry too old" and offer to restart execution')
    assert true

#@then program should throw "sorry too old" and offer to restart execution

# ----------------------------------------------------------------------

@when('user enters something that is after "2019" for the date born')
def test_too_far_input():
    raise NotImplementedError(u'STEP: When	user enters something that is after "2019" for the date born')

@then('program should throw "Impossible for them to exsist" and offer to restart execution')
def test_too_far_assert():
    raise NotImplementedError(u'STEP: Then	program should throw "Impossible for them to exsist" and offer to restart execution')
    assert true

#@then program should throw "Impossible for them to exsist" and offer to restart execution

# ----------------------------------------------------------------------
# Junk Code ~ ♫
# ----------------------------------------------------------------------
#
#
#
#
#
#
#
#

#Validation Code
test_rounder_input()

print("Tester All Green")

