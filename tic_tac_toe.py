#

current_position = {"top left": " ", "top center": " ", "top right": " ",
            "center left": " ", "center": " ", "center right": " ",
            "bottom left": " ", "bottom center": " ", "bottom right": " "}


current_player = "X"


some_string = "Hello {a_value}, {some_value}".format(a_value = "x", some_value = "y")
print some_string



print "\nANOTHER WAY: Using a Dictionary\n"

some_dictionary = {"a_value" : "x", "some_value" : "y"}
some_string = "Hello {a_value}, {some_value}".format(**some_dictionary)
print some_string
