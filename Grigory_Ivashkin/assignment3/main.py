from utils.notes_utils import add_note, read_notes
# a function that creates an interface in console
def show_menu():
    print("\nNotes Saver")
    print("1) Add note")
    print("2) Show notes")
    print("3) Exit")

# shows the interface until we exit the program.
while True:
    show_menu() # shows the interface
    choice = input("Choose: ").strip() # takes our input as like we clicked the buttons

# first button - add new note
# user writes something. if it is not the emty string
# we call for the add_note function frome notes_utils.py
    if choice == "1":
        text = input("Write your note: ").strip()
        if text == "":
            print("Empty note not saved.")
        else:
            add_note(text)
            print("Saved.")
# second button. we call for read_notes function.
# if notes.txt is empty. will print "no notes yet"
# if notes.txt contain anything, will print the returning of the function (var notes)
    elif choice == "2":
        notes = read_notes()
        if notes.strip() == "":
            print("No notes yet.")
        else:
            print("\nYour Notes")
            print(notes)
# button to exit from the "app". to end the program. to exit from console. otherwise, it will work forever. ( or until we shut down the system or close the console 
# by just exiting the program)
    elif choice == "3":
        break
# if user did not chosed 1/2/3: 
    else:
        print("Wrong choice. Try again.")
