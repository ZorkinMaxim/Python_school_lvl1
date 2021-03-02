from tkinter import Tk, Label, Button, Text
from faker import Faker
import yagmail

class Application:
    def __init__(self, master):
        self.master = master
        master.title("Send emails")

        self.emil_input = Text(master, width=40, height=1)
        self.emil_input.pack()

        self.greet_button = Button(master, text="Send", command=self.sendEmail, width=5, height=2)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit, width=5, height=2)
        self.close_button.pack()

    def sendEmail(self):
        f = Faker("ru")
        target_email = self.emil_input.get(1.0, 10.0).strip()
        author_name = f.name()
        author_email = f.email()
        subject = "Hi, you have been hacked!"
        body = "Please send your password :D!"

        yag = yagmail.SMTP("xtendmd@gmail.com", "SBOM2015")
        yag.send(target_email, subject, body)

        print("Sending email!", target_email, author_name, author_email)

root = Tk()
root.geometry("600x400")
my_gui = Application(root)
root.mainloop()

