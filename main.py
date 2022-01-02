#let's start with writing empty classes by taking a look in the design.txt file
from fpdf import FPDF
import webbrowser
import os
class Bill: #first object writtin in the txt file
  def __init__(self, amount, period): #the attributes writtin under the object
    self.amount = amount #defining the attributes as always
    self.period = period

class Flatemate:
  def __init__(self, days_in_house, name):
      self.days_in_house = days_in_house
      self.name = name

  def pays(self, bill, flatmate2): #where going to make pays as a new function, because it actually has to do something(calculation of the bill) and that's why we need the bill attribute
    weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
    to_pay = bill.amount * weight
    #days_in_house_flatmate1 = self.days_in_house
    #bill_flatmate1 = (bill.amount / (days_in_house_flatmate1 + flatmate2.days_in_house)) * days_in_house_flatmate1
    #bill_flatmate2 = (bill.amount / (days_in_house_flatmate1 + flatmate2.days_in_house)) * flatmate2.days_in_house
    return to_pay#bill_flatmate1, #bill_flatmate2


class Pdfreport:
  def __init__(self, filename):
    self.filename = filename

  def generate(self, flatmate1, flatmate2, bill):

    pdf =  FPDF(orientation='P', unit='pt', format='A4') #info about the paper itself
    pdf.add_page() #this'll make the page

    pdf.set_font(family='Times', size=24, style='B')
    pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)#cell work kinda the same as div in html
    
    #period
    pdf.cell(w=100, h=40, txt="Period: ", border=0)
    pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)
    #flatmates and bill
    pdf.set_font(family='Times', size=12, style='B')
    pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
    pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), 2)), border=0, ln=1)

    pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
    pdf.cell(w=150, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), 2)), border=0, ln=1)

    pdf.output(self.filename)
    webbrowser.open('file://'+os.path.realpath(self.filename)) #after generating the pdf this line'll automatically open the pdf 

# out of the class


while True:
  try:
    bill_amount = int(input('Fill in the amount of the total bill: '))
    if type(bill_amount) == int:
      break
  except ValueError:
    print('the bill amount should be given in numbers.....')

period_input = input('Enter the period(E.g April 2021): ')
flatmate1_name = input("What is you name? ")
while True:
  try:
    flatmate1_inhouse = int(input("how many days did you stay in the house in that period? "))
    if type(flatmate1_inhouse) == int:
      break
  except ValueError:
    print('the amount of days should be given in numbers.....')

flatmate2_name = input('What is the name of your flatmate? ')
while True:
  try:
    flatmate2_inhouse = int(input("how many days did he/she stay in the house in that period? "))
    if type(flatmate2_inhouse) == int:
      break
  except ValueError:
    print('the amount of days should be given in numbers.....')
the_bill = Bill(amount = bill_amount, period = period_input)
john = Flatemate(name=flatmate1_name, days_in_house=flatmate1_inhouse)
marry = Flatemate(name=flatmate2_name, days_in_house=flatmate2_inhouse) #marry.days_in_house

print('john pays $', john.pays(bill=the_bill, flatmate2=marry)) #we set here marry as an attribute becasue we can do marry.days_in_house and thats more orgranizied
print('marry pays $', marry.pays(bill=the_bill, flatmate2=john)) #marry.pays = makes connection between pays function and days in house of marry
# bill=the_bill = this way we make connection between the bill amount and the Bill class without having to be in the class itself
pdf_report = Pdfreport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)