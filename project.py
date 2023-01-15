#object oriented programing 
#calculation of Rental Income
#Use input 

#1-Income: Rental Income , Laundry, sotrage, misc
    #price of home $2000,000
        #Rental income/total monthly income = $2000 permonth 
#2-expenses: 
    #Tax =$150 month
    #Insurance = $100 month
    #utilities (electric, water, sewer, garbage, gas) = 0
    #HOA fee = 0
    #Lawn/snow = 0
    #Vecancy = $100 month
    #Repairs = $100 month
    #CapEX (replace thing/ for roof ect)= $100
    #property mangment = $200 month
    #Mortgage = $860 month
#total monthly expenses = $1610

#cash flow:
    # income - expenses
#total montly cashflow = $390

#4- cash on cash ROI= Annuel cash flow/ total investment(9.36%)
    #Down payment = $40,000
    #Closing Costs:$3,000
    #Rehab budget: $7,000
    #Misc other: 0
#total Investment: $ 50,000
#annual Cashflow:
    #$390 x 12 = $ 4,680

class foursquare():

    def __init__(self):
        self.rental_income =0
        self.tax = 0
        self.insurance = 0
        self.utilities =0
        self.hoa = 0
        self.lawn_snow = 0
        self.vacancy = 0
        self.repairs = 0
        self.cap_ex = 0 
        self.property_management = 0
        self.mortgage = 0
        self.down_payment = 0
        self.closing_cost = 0
        self.rehab_budget = 0
        self.misc_other = 0

    def calculate_box1(self):
        return self.rental_income

    def calculate_box2(self):
        print(self.tax, self.insurance, self.utilities, self.hoa, self.lawn_snow, \
            self.vacancy, self.repairs, self.cap_ex, self.property_management, self.mortgage)
        return self.tax + self.insurance + self.utilities + self.hoa + self.lawn_snow\
             + self.vacancy + self.repairs + self.cap_ex + self.property_management + self.mortgage
    
    def calculate_box3(self):
        return self.calculate_box1() - self.calculate_box2()

    def calculate_box4(self):
        return (self.calculate_box3() *12)/(self.down_payment + self.closing_cost + self.rehab_budget + self.misc_other)
        
    
    def set_rental_income(self, value):
        self.rental_income = value

    def set_tax(self, value):
        self.tax = value

    def set_insurance(self, value):
        self.insurance = value

    def set_utilities(self, value):
        self.utilities = value

    def set_hoa(self, value):
        self.hoa = value
    
    def set_lawn_snow(self, value):
        self.lawn_snow = value

    def set_vacancy(self, value):
        self.vacancy = value

    def set_repairs(self, value):
        self.repairs = value

    def set_cap_ex(self, value):
        self.cap_ex = value

    def set_property_management(self, value):
        self.property_management = value

    def set_mortgage(self, value):
        self.mortgage = value

    def set_montly_cash_flow(self, value):
        self.monthly_cash_flow = value

    def set_down_payment(self, value):
        self.down_payment = value

    def set_closing_cost(self, value):
        self.closing_cost = value

    def set_rehab_budget(self, value):
        self.rehab_budget = value

    def set_misc_other(self, value):
        self.misc_other = value
    



property = foursquare()

rental_income = int(input("How much will you collect per month on rent?"))
property.set_rental_income(rental_income)

tax = int(input("what is the monthly tax on the property?"))
property.set_tax(tax)

insurance = int(input("what is the monthly insurance on the property?"))
property.set_insurance(insurance)


utilities =  int(input("what is the monthly utilties on the property?"))
property.set_utilities(tax)

hoa = int(input("What is the HOA on the property?"))
property.set_hoa(hoa)

lawn_snow =  int(input("what is the monthly law and snow removal on the roperty?"))
property.set_tax(lawn_snow)

vacancy = int(input("what is the monthly vacancy on the roperty?"))
property.set_vacancy(vacancy)

repairs =  int(input("what is the monthly repairs  on the roperty?"))
property.set_repairs(repairs)

cap_ex =  int(input("what is the monthly cap ex on the roperty?"))
property.set_cap_ex(cap_ex)

property_management =  int(input("what is the monthly property management on the roperty?"))
property.set_property_management(property_management)

mortgage =  int(input("what is the monthly mortgage on the roperty?"))
property.set_mortgage(mortgage)

print("Total expenses:", property.calculate_box2())


print("Monthly cash flow:", property.calculate_box3())

# -- last box doesn't use setters --
down_payment = int(input("What is the downpayment?"))
property.set_down_payment(down_payment)

closing_cost = int(input("What is the closing cost?"))
property.set_closing_cost(closing_cost)

rehab = int(input("what is the rehab cost?"))
property.set_rehab_budget(rehab)

misc_other = int(input("what is the misc cost?"))
property.set_misc_other(misc_other)



final_cash_on_cash_profit = property.calculate_box4()
print("Forecasted profit:", round(final_cash_on_cash_profit*100, 2), "%")