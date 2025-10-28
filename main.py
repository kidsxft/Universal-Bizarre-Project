import tkinter
import customtkinter
from PIL import Image, ImageTk
import backend as be

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

loggedUsername = ""

stats = {
    
}

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        be.create_table()

        self.title("Universal Bizarre Project")
        self.geometry("1000x600")

        self.minsize(750, 350)

        self.frames = {}
        self.initialize_frames()

        self.switch_screen("LoginFrame")

    def initialize_frames(self):
        self.frames["LoginFrame"] = LoginFrame(self, self.switch_screen)
        self.frames["MenuFrame"] = MenuFrame(self, self.switch_screen)
        self.frames["AUTFrame"] = autGame(self, self.switch_screen)
        self.frames["InventoryFrame"] = inventoryFrame(self, self.switch_screen)

    def switch_screen(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        frame = self.frames.get(frame_name)
        if frame:
            frame.pack(pady=20, padx=60, fill="both", expand=True)

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.master = master
        self.switch_screen = switch_screen

        self.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(self, text="Login System", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.extra = customtkinter.CTkLabel(self, text="", font=("Roboto", 12))
        self.extra.pack(pady=8, padx=10)

        self.usernameBox = customtkinter.CTkEntry(self, placeholder_text="Username")
        self.usernameBox.pack(pady=12, padx=10)

        self.passwordBox = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
        self.passwordBox.pack(pady=12, padx=10)

        self.loginBtn = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.loginBtn.pack(pady=12, padx=10)

        self.registerBtn = customtkinter.CTkButton(self, text="Register", command=self.register)
        self.registerBtn.pack(pady=12, padx=10)

        #self.checkbox = customtkinter.CTkCheckBox(self, text="Remember Me")
        #self.checkbox.pack(pady=12, padx=10)

    def login(self):
        global loggedUsername

        username = self.usernameBox.get()
        password = self.passwordBox.get()

        if "" in (username, password):
            print("MUST NOT HAVE EMPTY FIELDS")
            self.extra.configure(text = "MUST NOT HAVE EMPTY FIELDS")
        else:
            if password == be.get_login(username):
                print("Logged In")
                loggedUsername = username
                self.switch_screen("MenuFrame")
            else:
                self.extra.configure(text = "Incorrect Password/ Does not Exist")
                print("Incorrect Password/ Does not Exist")

    def register(self):
        username = self.usernameBox.get()
        password = self.passwordBox.get()

        if "" in (username, password):
            self.extra.configure(text = "MUST NOT HAVE EMPTY FIELDS")
            print("MUST NOT HAVE EMPTY FIELDS")
        else:
            if username not in be.get_all_usernames():
                be.create_login(username, password)
                self.extra.configure(text = "Registered Successfully")
                print("Registered Successfully")
            else:
                self.extra.configure(text = "Login already Exists")
                print("Login already Exists")

class MenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.master = master
        self.switch_screen = switch_screen

        self.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(self, text="SELECT GAME", font=("Roboto", 24))
        self.label.pack(pady=20)

        self.autBtn = customtkinter.CTkButton(self, text="A Universal Timeline", command=self.refresh)
        self.autBtn.pack(pady=12, padx=10)

        #self.abdBtn = customtkinter.CTkButton(self, text="A Bizarre Day", command=self.register)
        #self.abdBtn.pack(pady=12, padx=10)

        self.logoutBtn = customtkinter.CTkButton(self, text="Logout", command=lambda: self.switch_screen("LoginFrame"))
        self.logoutBtn.pack(pady=10)        

    def refresh(self):
        stand = be.getData("stand", loggedUsername)
        self.master.frames["AUTFrame"].currentStandLabel.configure(text = f"Current Stand: {stand}")
        self.switch_screen("AUTFrame")

class autGame(customtkinter.CTkFrame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.master = master
        self.switch_screen = switch_screen

        self.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(self, text="A Universal Timeline", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        # Display the user's stand
        stand = be.getData("stand", loggedUsername)
        self.currentStandLabel = customtkinter.CTkLabel(self, text=f"Current Stand: {stand}", font=("Roboto", 20))
        self.currentStandLabel.pack(pady=12, padx=10)

        self.playBtn = customtkinter.CTkButton(self, text="Play", command=lambda: print("PLAY"))
        self.playBtn.pack(pady=12, padx=10)

        self.invBtn = customtkinter.CTkButton(self, text="Inventory", command=lambda: self.switch_screen("InventoryFrame"))
        self.invBtn.pack(pady=12, padx=10)

        self.shopBtn = customtkinter.CTkButton(self, text="Store", command=lambda: print("BUY"))
        self.shopBtn.pack(pady=12, padx=10)

class inventoryFrame(customtkinter.CTkFrame):
    def __init__(self, master, switch_screen):
        super().__init__(master)
        self.master = master
        self.switch_screen = switch_screen

        self.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(self, text="A Universal Timeline", font=("Roboto", 24))
        self.label.pack(pady=12, padx=10)

        self.sidebar = Sidebar(self, switch_screen, self.update_main_content)
        self.sidebar.pack(side="left", fill="y", padx=(10, 5), pady=10)

        # Main Window (assuming MainWindow and other content)
        self.main_window = MainWindow(self)
        self.main_window.pack(side="right", fill="both", expand=True, padx=(5, 10), pady=10)

    def update_main_content(self, new_title, image_path):
        self.main_window.update_content(new_title, image_path)

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, master, switch_screen, update_main_content):
        super().__init__(master)

        self.master = master
        self.switch_screen = switch_screen
        self.update_main_content = update_main_content

        self.pack_propagate(False)
        self.configure(width=250)

        self.backBtn = customtkinter.CTkButton(
            self,
            text="Back",
            width=250,
            font=("Roboto", 24),
            command=lambda: self.switch_screen("AUTFrame")
        )
        self.backBtn.pack(padx=10, pady=5)

        self.itemList = customtkinter.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.itemList.pack(fill="both", expand=True, padx=10, pady=5)

        # List to hold buttons
        self.buttons = []

        lighter_color = "#212121"

        # Add multiple buttons
        button_texts = [
            ("Roka Fruit(s)", "images/rokaFruitIMG.png"),
            ("Arrow(s)", "images/arrowIMG.png"),
            ("Steel Ball(s)", "images/steelBallIMG.png"),
            ("Frog(s)", "images/frogIMG.png"),
            ("Tommy Gun(s)", "images/tommyGunIMG.png"),
            ("Sword(s)", "images/swordIMG.png"),
            ("Stone Mask(s)", "images/stoneMaskIMG.png"),
            ("Red Aja(s)", "images/redAjaIMG.png"),
            ("Requiem Arrow(s)", "images/requiemArrowIMG.png"),
            ("Rebirth Arrow(s)", "images/rebirthArrowIMG.png"),
            ("Aja Mask(s)", "images/ajaMaskIMG.png"),
            ("Diary(ies)", "images/diaryIMG.png"),
            ("Bone(s)", "images/boneIMG.png"),
            ("Corpse Part(s)", "images/corpsePartIMG.png"),
            ("Fruit(s)", "images/fruitIMG.png"),
            ("Disc(s)", "images/discIMG.png")
        ]
        for text, image_path in button_texts:
            button = customtkinter.CTkButton(self.itemList, text=text, command=lambda t=text, img=image_path: self.button_clicked(t, img))
            button.pack(fill="x", padx=10, pady=5)
            button.configure(fg_color=lighter_color)
            self.buttons.append(button)

    def button_clicked(self, text, image_path):
        self.update_main_content(text, image_path)

class MainWindow(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # Create widgets for Title and Body - Will readjust to fit the window
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.title = customtkinter.CTkLabel(
            self,
            fg_color="transparent",
            text=f"Roka Fruit(s): {be.getData('rokaFruit', loggedUsername)}",
            font=("Roboto", 24)
        )
        self.title.grid(
            column=0,
            row=0,
            padx=(0, 5),    
            pady=5,
            sticky="ew"
        )

        # Load the image
        self.image = Image.open("images/rokaFruitIMG.png")
        self.image = self.image.resize((100, 100), Image.LANCZOS)  # Use LANCZOS for high-quality downsampling
        self.photo = ImageTk.PhotoImage(self.image)

        self.image_label = tkinter.Label(self, image=self.photo)
        self.image_label.grid(
            column=0,
            row=1,
            padx=(0, 5),
            pady=5,
            sticky="ew"
        )

        self.useBtn = customtkinter.CTkButton(
            self,
            text="Use",
            width=250,
            height=50,  # Fixed height
            font=("Roboto", 24),
            command=lambda: self.master.switch_screen("AUTFrame")  # Assuming switch_screen method is in master
        )
        self.useBtn.grid(
            column=0,
            row=2,
            padx=(0, 5),
            pady=5,
            sticky="ew"
        )

    def update_content(self, new_title, image_path):
        self.title.configure(text=new_title)

        # Load and display image
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo  # Keep a reference to prevent image from being garbage collected

if __name__ == "__main__":
    app = App()
    app.mainloop()
