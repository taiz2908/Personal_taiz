# Python Data Types:
# - Integer - 22/1/43
# - Flot - 1.1/3.4,11.3
# - boolean - True/False
# - strings - hello/ibraur

#concatenation example:
print("hello " + str(20) + " world")
print(f"hello {20} world") #works only latest python version, f stands for format
print(f"hello {20 * 24 * 60 } world")
print(f"hello {30 * 24 * 60 } world")

#how to write with variable
mins_sec = 24 * 60
string = "world"
print(f"hello {20 * mins_sec } {string}")
print(f"hello {30 * mins_sec } {string}")

#functions in python
mins_sec = 24 * 60
string = "world"
def test():
    print(f"hello {20 * mins_sec } {string}")
    print("All Good!")
test()

#functions parameters(input) in python
mins_sec = 24 * 60
string = "world"

def test(numbers):
    print(f" {numbers} hello {numbers * mins_sec } {string}")

test(20)
test(30)

#Variables scope in python global + local
#local scope can be used inside that function.
global_variable="test3 "

def local_variable(local_variable1, local_variable2):
    internal_variable = "test4"
    print(local_variable1 + local_variable2 + global_variable)
    print(internal_variable)

local_variable("test1 ", "test2 ")

####### user inputs ####