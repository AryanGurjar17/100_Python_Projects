from curses.ascii import DC1


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you did not provide vailid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("what is your first name ?"), input("What is your last name ?")))

# BufferErrorDEF
# DC1