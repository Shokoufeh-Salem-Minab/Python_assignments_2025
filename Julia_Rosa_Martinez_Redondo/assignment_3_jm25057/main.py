# ~~~~~~~~A C T I V I T Y 3 PYTHON~~~~~~~~
# Libraries, Modules, Files & Directories
# By Julia Rosa Martinez Redondo jm25057

import random
import my_utils        # my own module in the same carpet also

# ~~~~~~~~INPUT~~~~~~~~
name = input("enter name: ")
message_in_a_bottle = input("write small message: ")

# ~~~~~~~~PROCESS~~~~~~~~
# random number just to use library
rand_num = random.randint(1, 10)

today_date = my_utils.get_today_date()
# disposition & what to be putted
text_to_save = "name: " + name
text_to_save += " | message: " + message_in_a_bottle
text_to_save += " | random num: " + str(rand_num)
text_to_save += " | date: " + today_date

# ~~~~~~~~OUTPUT~~~~~~~~
print("\ndata saved:")
# here i prepare the text to save in file
print(text_to_save)
# ~~~~~~~~SAVE TO FILE~~~~~~~~
my_utils.save_text("my_notes.txt", text_to_save)
