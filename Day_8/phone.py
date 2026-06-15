class phone:
    def __init__(self,brand,storage):
        self.brand=brand
        self.storage=storage
        self.is_on=False
        self.apps=[]

    def power_on(self) :
        self.is_on=True
        print(f"{self.brand} is now ON.")

    def power_off(self) :
        self.is_on=False
        print(f"{self.brand} is now OFF.")    

    def install_app(self,app_name):
        self.apps.append(app_name)
        print(f"{app_name} installed on {self.brand}")

    def show_status(self):
        print(f"Brand: {self.brand} | Storage: {self.storage}GB | ON : {self.is_on} | Apps: {self.apps}")

phone_1=phone("Samsung",128) 
phone_2=phone("Apple",256)                       

phone_1.show_status()
phone_1.power_on()
phone_1.install_app("Instagram")
phone_1.install_app("YouTube")
phone_1.show_status()
phone_1.power_off()
phone_1.show_status()

phone_2.show_status()
phone_2.power_on()
phone_2.install_app("Whatsapp")
phone_2.show_status()