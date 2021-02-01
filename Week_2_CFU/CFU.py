#!/usr/bin/env python3
import sys
# This is your assignment in python.
# First, read the experimental design/protocol by looking at the ASCII
# cartoon below. It takes you through steps 1-4, which were performed in-lab.
#
# Step 5 is in python code (scroll down after the cartoon)
# The python code back-calculates the dilutions to estimate the number
# of bacteria in the sample and prints the result of the calculation

# STEPS 1-4, DESCRIPTION OF EXPERIMENT (scroll down to get to python code-STEP 5):
# Goal: Determine infection level of an organ by serial dilution, plating.
# PROTOCOL:
#  Put infected organ (by tuberculosis) into solution
#
#     @~@            (^@
#    @@^^@@  lung     -/   spleen  (not to scale)
#     @  @            ;
#
#   ~ STEP 1: grind up organ, add buffer to .5ML total
#     ..*..**.*.
#      *..*.*.*
#       ..*..*
#         *
#                    ~~ STEP 2: perform serial dilution ~~~
#        <. > 1/2 dilution -->  <  >  1/2 dilution -->  <  >  1/2 dilution -->  <  >
#        /* \                   /  \                    /  \                    /  \
#       /~~o~\                 /~oo~\                  /o~~~\                  /~~~~\
#      /O0   o\               /o    O\                /O   O \                /    o \
#     (_o_oo0__)             (oo___o__)              (_o_____o)              (_o______)
#    dilution 0              dilution 1               dilution 2              dilution 3
#                   ~~~ STEP 3: resuspend (.5ML) and plate on growth medium (100uL total). Incubate. ~~~
#           V                      V                      V                       V
#           V         ##           V                      V         ##            V        #
#           S         ##           S         ##           S         ##            S        #
#   ~~~~~~~~  100uL   ##    ~~~~~~~~  100uL  ##    ~~~~~~~~ 100uL    ##     ~~~~~~~~ 100uL  #
#  |___________|      ##  |___________|      ##  |___________|      ##  |___________|      #
#       \|/           ##       \|/           ##       \|/           ##       \|/           #
#    ~ grow ~         ##    ~ grow ~         ##    ~ grow ~         ##    ~ grow ~         #
#        V            ##        V            ##        V            ##        V            #
#        Y            ##        Y            ##        Y            ##        Y            #
#   |XXXXXXXXX|       ##   |__xX___xx__|     ##   |__x_____x__|     ##   |___________|     #
#                    ~~~~ Step 4: count CFUs after 12 hrs at 37 degrees C   ~~~~           #
#    Too numerous     ##    countable        ##     countable       ##     nothing         #
#    to count         ##       (26)          ##       (10)          ##        (0)          #


# STEP 5:
# The first sample in the assignment (depicted in ASCII above)
cfu_0 = 0  # dilution 0 was too numerous to count (TNTC)
cfu_1 = 26  # after dilution (1/2 of previous)
cfu_2 = 10  # after dilution (1/2 of previous)
cfu_3 = 0  # after dilution (1/2 of previous)

# Now we back-calculate to the original number of bacteria (i.e. colony forming units) in the organ.

# for the undiluted
whole_organ_0 = cfu_0 * .5 / .1  # however, this is zero because it was Too Numerous To Count
print("whole organ undiluted:", whole_organ_0)

# for the first dilution, we'll use cfu_1
whole_organ_1 = cfu_1 * 2 * .5 / .1  # notice we are multiplying by 2 now because the dilution was 1/2
print("whole organ first dilution:", whole_organ_1)

# note: for this assignment, you will have to uncomment the lines the have the "...," and fill in the "..." with
# the requested code. For example, if I ask to set x to a number, and I give you:
# x = ...
# Then you delete the '#' AND the space immediately after it, and then fill in the "..."
x = 5

# ------Start modifying below  ---------------------------------------------------------------
# (1pt total)
# what is the formula to back-calculate from the second dilution?
# hint: We have diluted by 1/2 on top of the previous dilution
# whole_organ_2 = ...
# print("whole organ second dilution", ...)

# (1pt total)
# what is the formula for the third dilution?
# hint: We have diluted by 1/2 AGAIN on top of the previous dilution:
# whole_organ_3 =...
# print("whole organ third dilution", ...)

# (1pt total)
# Question 1: what gave the best result (in this case, the highest)?
print("The highest CFU count was:", ..., "at dilution ...")

# moving on
sys.exit(0)  # delete or comment this line to activate next block

# Generalizing code
# Now, we notice that some values are the same for each calculation. They are:
RESUSPEND_VOLUME_ML = .5

# we can substitute variables into the formulas:
whole_organ_0 = cfu_0 * RESUSPEND_VOLUME_ML / .1
whole_organ_1 = cfu_1 * 2 * RESUSPEND_VOLUME_ML / .1
# (1pt total)
# substitute these values into the formulas for the other dilutions:
# whole_organ_2 = ...
# whole_organ_3 = ...
print("whole organ undiluted:", whole_organ_0)
print("whole organ first dilution:", whole_organ_1)
print("whole organ second dilution:", whole_organ_2)
print("whole organ third dilution:", whole_organ_3)

# (1pt total)
# now do the same by defining a new variable, VOLUME_PLATED_ML, to substitute for .1:
# VOLUME_PLATED_ML = ...
# whole_organ_0 = ...
# whole_organ_1 = ...
# whole_organ_2 = ...
# whole_organ_3 = ...
print("whole organ undiluted:", whole_organ_0)
print("whole organ first dilution:", whole_organ_1)
print("whole organ second dilution:", whole_organ_2)
print("whole organ third dilution:", whole_organ_3)

# code challenge: in the code above, change the value of VOLUME_PLATED_ML to .2 and rerun the output.
# Leave the value at .2 to turn in. *****(you must do this for the 1 pt).*****

# (1pt total)
# Question 2: What benefit is there in using variables instead of just the values themselves?
print("the value of using variables is ...")

# Generalize further
sys.exit(0)  # delete or comment this line to activate next block

# The next statements to the for-loops Are instructional, no points.
CFUs = [0, 26, 10, 0]

print("This is the first loop construct to handle all dilutions:")
dilution = 1
for cfu in CFUs:
    whole_organ = cfu * dilution * .5 / .1
    print("whole organ CFUs with dilution factor: ", dilution, "is", whole_organ)
    dilution = dilution * 2

# (1pt total)
# Question 3: Why must 'dilution' be set to 1 outside of the loop?
# Hint: What happens if you set it inside the loop?
print("The variable 'dilution' is set outside of the loop because ...")

# (1pt total)
# Code challenge: REPLACE THE VALUES .5 and .1 with as you did above with RESUSPEND_VOLUME_ML and VOLUME_PLATED_ML,
# but now add a new variable DILUTION_FACTOR, set to 2, and replace the '2' in the code.
print("This is the second loop construct that uses more variables (should give same output):")
dilution = 1
for cfu in CFUs:
    whole_organ = cfu * dilution * .5 / .1
    print("whole organ CFUs with dilution factor: ", dilution, "is", whole_organ)
    dilution = dilution * 2  # modify this line


# Moving on: Better loops
sys.exit(0)  # delete this line to activate the next block of code

# The zip() function allows us to loop over two lists at the same time, item for item.
# Example (no points here):
numbers = [1, 2, 3]
ABCs = ['a', 'b', 'c']
for number, letter in zip(numbers, ABCs):
    print(number, letter)

# output:
# 1 a
# 2 b
# 3 c

# We can "zip" together the dilution factor with its corresponding CFUs (0, 26, 10, 0)
# (1pt total)
DILUTIONS = [1, 2, 4, 8]
for dilution, cfu in zip(DILUTIONS, CFUs):
    print("Dilution factor", dilution, "had", cfu, "colony forming units.")
    # replace the two following lines with code from above: (1pnt total)
    # set whole_organ as above (same exact expression)
    # copy print statement from above (same exact expression)


# Another formulation. This is an example, don't change anything
DILUTIONS = [0, 1, 2, 3]  # just a series from 0 to 3, not the actual factor
for dilution_number, cfu in zip(DILUTIONS, CFUs):
    dilution = 2 ** dilution_number
    whole_organ = cfu * dilution * .5 / .1
    print("whole organ CFUs with dilution factor: ", dilution, "is", whole_organ)

# (1pt total)
# Question 4. What does '2 ** dilution_number' do? Hint: what is the '**' operator?
print("2 ** dilution_number calculates: ...")

# Extra Credit Coding Challenge.

# enumerate()
# There is a way to write the above function with only the important list, using:
# enumerate(CFUs) in place of zip(DILUTIONS, CFUs)

# (1pt total) EXTRA CREDIT
# Look up the function enumerate() and rewrite the loop (you must uncomment each line).
# (Extra 1pnt total)
# fill in the ...'s below
# for ... in enumerate(CFUs):
#     ...
#     print("whole organ CFUs with dilution factor: ", dilution, "is", whole_organ)
