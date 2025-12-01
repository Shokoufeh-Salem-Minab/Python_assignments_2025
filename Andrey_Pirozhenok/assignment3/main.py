"""
App that checks if there are any people that were born on the same day.
"""

import re
from docdb import Connection, is_valid_ident

con = Connection("./gitignoremeplease")
con.table_create_if_not_exists("days")
con.table_create_if_not_exists("users")
dob_regex = re.compile("^\\s*([0-9]+)\\s*-\\s*([0-9]+)\\s*$")


def main() -> None:
    name = input("What should i call you? ").strip()
    if len(name) == 0:
        print("I cannot work without a name")
        return
    if not is_valid_ident(name):
        print("Your name is not a valid identifier. Try using a username?")
        return

    m = re.search(dob_regex, input("When were you born? (mm-dd) "))
    if m is None:
        print("I do not understand you")
        return

    month = int(m.group(1))
    day = int(m.group(2))

    if month < 1 or month > 12 or day < 1 or day > 31:
        # Let's asume user is not malicous and does know his date of birth,
        # so that there will be no invalid dates.
        print("Not a valid date, sorry.")
        return

    prev, ok = con.data_lookup("users", name)
    if ok and (prev["day"] != day or prev["month"] != month):
        prev_validated = f"{prev['month']:02}-{prev['day']:02}"
        print(
            f"Something fishy is going on here, "
            f"you previously stated that you were born on {prev_validated}. "
            f"I will assume this is an honest mistake and replace it for you."
        )

        def del_user(arr: list[str]) -> list[str]:
            try:
                while True:
                    arr.remove(name)
            except ValueError:
                pass
            return arr

        con.data_map("days", prev_validated, del_user)

    con.data_upsert("users", name, {"day": day, "month": month})

    validated = f"{month:02}-{day:02}"

    data, ok = con.data_lookup("days", validated)
    if not ok:
        data = []

    if name not in data:
        data.append(name)

    con.data_upsert("days", validated, data)

    if len(data) == 1:
        print("You are the only one with this birthday :(")
        return

    print("These people share their birthday with you:")
    for person in data:
        if person == name:
            continue
        print(f"- {person}")


if __name__ == "__main__":
    main()
