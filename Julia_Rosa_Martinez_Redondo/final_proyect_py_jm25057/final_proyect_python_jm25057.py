# ~~~~~~~~P R O J E C T  PYTHON - CinemaSA seats~~~~~~~~
# By Julia Rosa Martinez Redondo jm25057
# meaning of numbers:
# 0 = empty seat
# 1 = paid seat
# 2 = reserved seat (not paid yet)

# idea of project:
# manage seats of a cinema
# allow user to see seats, reserve, cancel, pay
# and save everything in a txt file

SEATS_FILE = "seats_state.txt"   # file where i save the seats state


# ~~~~~~~~LOAD / SAVE PART~~~~~~~~
def save_seats(seats):
    # this function saves the seats list into a txt file
    # so when program closes, data is not lost
    file = open(SEATS_FILE, "w")
    file.write(",".join(str(x) for x in seats))
    file.close()


def load_seats():
    # this function tries to load the seats from txt
    # if file does not exist, it uses the initial seats
    try:
        file = open(SEATS_FILE, "r")
        data = file.read().strip()
        file.close()

        # convert text to list of numbers
        parts = data.split(",")
        seats = []
        for p in parts:
            if p != "":
                seats.append(int(p))

        # small check just in case file is wrong
        if len(seats) != 16:
            return initial_seats()

        return seats

    except FileNotFoundError:
        # if something fails, start from initial state
        return initial_seats()


def initial_seats():
    # initial seats given in the statement
    # index 0 is seat 1, index 15 is seat 16
    return [0, 0, 0, 1,
            0, 1, 1, 2,
            2, 2, 2, 0,
            0, 1, 1, 1]


# ~~~~~~~~SHOWING SEATS~~~~~~~~
def show_seats_by_type(seats, wanted):
    # show only seats of one type
    # wanted can be 0, 1 or 2

    print("\nseats that are type:", wanted)
    print("(0 empty / 1 paid / 2 reserved)")

    found_any = False
    i = 0
    while i < len(seats):
        if seats[i] == wanted:
            # +1 because seats start at 1 for users
            print("seat", i + 1, "is", seats[i])
            found_any = True
        i += 1

    if found_any is False:
        print("none of this type")


def show_all_seats_simple(seats):
    # quick view of all seats with their status
    print("\nall seats (seat : status)")
    i = 0
    while i < len(seats):
        print((i + 1), ":", seats[i])
        i += 1


def show_empty_seats(seats):
    # show only empty seats (0)
    # this is used before reserving
    print("\nEMPTY seats you can reserve:")
    i = 0
    any_empty = False
    while i < len(seats):
        if seats[i] == 0:
            print("seat", i + 1)
            any_empty = True
        i += 1

    if any_empty is False:
        print("no empty seats left :(")


def show_reserved_seats(seats):
    # show only reserved seats (2)
    # used for cancelling or paying
    print("\nRESERVED seats:")
    i = 0
    any_res = False
    while i < len(seats):
        if seats[i] == 2:
            print("seat", i + 1)
            any_res = True
        i += 1

    if any_res is False:
        print("no reserved seats :(")


# ~~~~~~~~RESERVE / CANCEL / PAY~~~~~~~~
def reserve_one_seat(seats, seat_num):
    # reserve seat only if it is empty
    idx = seat_num - 1
    if seats[idx] == 0:
        seats[idx] = 2
        print("ok reserved seat", seat_num)
    else:
        print("cant reserve that seat, its not empty (prohibited)")


def cancel_one_seat(seats, seat_num):
    # cancel only if seat was reserved
    idx = seat_num - 1
    if seats[idx] == 2:
        seats[idx] = 0
        print("ok cancelled seat", seat_num)
    else:
        print("cant cancel, seat is not reserved")


def pay_one_seat(seats, seat_num):
    # pay seat only if it was reserved (2)
    idx = seat_num - 1
    if seats[idx] == 2:
        seats[idx] = 1
        print("ok seat paid", seat_num)
    else:
        print("cant pay, seat is not reserved")


# ~~~~~~~~MAIN PROGRAM~~~~~~~~
# first load seats from file or initial
seats = load_seats()

opt = ""
while opt != "5":

    print("\n--- CinemaSA MENU ---")
    print("1) see seats (choose type)")
    print("2) reserve seat(s)")
    print("3) cancel reserved seat(s)")
    print("4) pay reserved seat(s)")
    print("5) exit (and save)")

    opt = input("choose option: ")

    if opt == "1":
        # user chooses what type of seats to see
        print("\nwhat do you want to see?")
        print("0 = empty")
        print("1 = paid")
        print("2 = reserved")

        t = int(input("choose 0/1/2: "))

        if t == 0 or t == 1 or t == 2:
            show_seats_by_type(seats, t)
        else:
            print("not valid type")

    elif opt == "2":
        # reserve seats
        show_empty_seats(seats)

        more = "y"
        while more == "y":
            seat_num = int(input("choose seat number to reserve (1-16): "))

            if seat_num >= 1 and seat_num <= 16:
                reserve_one_seat(seats, seat_num)
            else:
                print("wrong seat number")

            more = input("reserve another? (y/n): ")

        show_all_seats_simple(seats)

    elif opt == "3":
        # cancel reservations
        show_reserved_seats(seats)

        more = "y"
        while more == "y":
            seat_num = int(input("choose seat number to cancel (1-16): "))

            if seat_num >= 1 and seat_num <= 16:
                cancel_one_seat(seats, seat_num)
            else:
                print("wrong seat number")

            more = input("cancel another? (y/n): ")

        show_all_seats_simple(seats)

    elif opt == "4":
        # pay reserved seats
        show_reserved_seats(seats)

        more = "y"
        while more == "y":
            seat_num = int(input("choose seat number to pay (1-16): "))

            if seat_num >= 1 and seat_num <= 16:
                pay_one_seat(seats, seat_num)
            else:
                print("wrong seat number")

            more = input("pay another? (y/n): ")

        show_all_seats_simple(seats)

    elif opt == "5":
        # exit and save seats
        save_seats(seats)
        print("saved in", SEATS_FILE)
        print("bye")

    else:
        print("not valid option")
