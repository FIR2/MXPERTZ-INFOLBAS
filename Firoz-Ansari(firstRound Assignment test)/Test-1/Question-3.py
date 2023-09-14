
class Nokia:
    # take a attribute----------
    company = "Nokia India"
    webiste = "www.nokia-india.com"
    
    # define method---------------
    def contact_details(self):
        print("Address : Cherry Road,Near Bus Stand ,Salem")
 
 
# create a child which inherite parent class properties and charactristcs---
class Nokia1100(Nokia):
    def __init__(self):
        self.name = "Nokia 1100"
        self.year = 1998
 
    def product_details(self):
        print("Name     : ", self.name)
        print("Year     : ", self.year)
        print("Company  : ", self.company)
        print("Website  : ", self.webiste)
 
# create object of the child class-----
mobile = Nokia1100()
mobile.product_details()
mobile.contact_details()
 