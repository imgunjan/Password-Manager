import random
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_pass():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(letters) for _ in range(nr_symbols)]
    password_number = [random.choice(letters) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

    # password = ""
    # for char in password_list:
    #     password += char
    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    # checking the user has input the text or not
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="opps", message="please make sure you havent left any box empty"
        )
    else:
        # showing the user the message box
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"these are the detailed entered:\n email:{email} \n password: {password}\n Is it ok to save")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Genator")
window.config(padx=20, pady=20)
# window.minsize(width=200, height=200)


# Setting an image in tk inter gui
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Setting the lable for the password genarator app
website_lable = Label(text="Website:")
website_lable.grid(column=0, row=1)

email_lable = Label(text="Email/Username:")
email_lable.grid(column=0, row=2)

password_lable = Label(text="Password:")
password_lable.grid(column=0, row=3)

# Setting the  button of the gui
pass_generator_button = Button(text="genarator", command=generate_pass)
pass_generator_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

# Setting an input field to the gui
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "gunjanpokhrel7@gmail.com")

password_input = Entry(width=25)
password_input.grid(column=1, row=3)

window.mainloop()
