import backend as be
import tkinter
import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        be.create_table()

        self.title("Universal Bizarre Project")
        self.geometry("1000x600")

        self.minsize(750, 350)

        self.label = customtkinter.CTkLabel(self, text="Admin Panel", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.extra = customtkinter.CTkLabel(self, text="", font=("Roboto", 12))
        self.extra.pack(pady=8, padx=10)

        self.usernameBox = customtkinter.CTkEntry(self, placeholder_text="Username")
        self.usernameBox.pack(pady=12, padx=10)

        self.dataBox = customtkinter.CTkEntry(self, placeholder_text="Data")
        self.dataBox.pack(pady=12, padx=10)

        self.valueBox = customtkinter.CTkEntry(self, placeholder_text="Value")
        self.valueBox.pack(pady=12, padx=10)

        self.excecuteBtn = customtkinter.CTkButton(self, text="Excecute", command=self.runCommand)
        self.excecuteBtn.pack(pady=12, padx=10)

    def runCommand(self):
        self.username = self.usernameBox.get()
        self.data = self.dataBox.get()
        self.value = self.valueBox.get()

        try:
            be.updateData(self.data, self.value, self.username)
            self.extra.configure(text = "Update Successful")
        except:
            self.extra.configure(text = "Update Unsuccessful")

app = App()
app.mainloop()