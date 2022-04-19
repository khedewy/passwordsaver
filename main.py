from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generat_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for letter in range(nr_letters)]
    symbols_list = [random.choice(symbols) for symbol in range(nr_symbols)]
    number_list = [random.choice(numbers) for number in range(nr_numbers)]
    password_list = password_letter + symbols_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    new_data = {website: {
            "email": email,
            "password": password
      }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="check that you haven't left any thing empty")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"these are the information entered:"
                                                                f" \nEmail {email},\nPassword {password},is it ok?!  ")
        if is_okay:
            try:
                with open("data.json", "r") as data_file:
                    data_1 = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # updating the data
                data_1.update(new_data)

                with open("data.json", "w") as data_file:
                    # saving the data
                    json.dump(data_1, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="their is no such data for this website ")

    else:
        if website in data:
            #print(data)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"here is your email:{email} and \npassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"no such data for {website}")



window = Tk()
window.title("password Generator and saver")
window.config(pady=20, padx=20)
canvas = Canvas(width=200, height=200,bg="blue")
the_photo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=the_photo)
canvas.grid(column=1, row=0)




website_label = Label(text="website: ")
website_label.grid(column=0, row=1)


user_name_label = Label(text="user_name/Email:")
user_name_label.grid(column=0, row=2,)


password_label = Label(text="password")
password_label.grid(column=0, row=3,)

add_button = Button(text="Add", command=save)
add_button.grid(column=1,row=5, columnspan=2)

generate_password = Button(text="Generate Password", command=generat_password)
generate_password.grid(column=4, row=3)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=3, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
user_name_entry = Entry(width=35)
user_name_entry.grid(column=1, row=2)
user_name_entry.insert(0, "please, insert your e_mail")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)





window.mainloop()
