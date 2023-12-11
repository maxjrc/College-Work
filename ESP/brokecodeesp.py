houses = [['LONDON','Terraced', 3, 735000], ['CARDIFF', 'Semi-Detached', 2, 100000], ['LEEDS','Terraced', 3,245000],['LONDON','Semi-Detatched', 1, 240000]]
sales = []
ourregions = ['LONDON', 'LEEDS', 'CARDIFF', 'BRISTOL']    
property_types =  ['TERRACED', 'SEMI-DETATCHED','DETATCHED']
unique_list = []

def return_stock():
    print("CURRENT HOUSES FOR SALE \n\n REGION - HOUSE TYPE - BEDROOMS - COST")
    for i in houses:
        print (i)

def unique_regions():
    print(unique_list)


def region_search():
    print("Available Regions")
    unique_regions()
    r_check = False

    while not r_check:
        region_select= input("Please enter region: ").capitalize()

        for x in houses:
            if region_select.upper() == x[0].upper():
                r_check = True
                if x[0] == region_select.upper():
                    print(x)

        if r_check == False:
            print("Entered region is not valid")



def show_sales():
    if len(sales) > 0:    
        print("Forename  Surname Property cost  Total")
        for i in sales:
            print(i)
    else:
        print('No Sales.')


def house_sale():
    sale = []
    customer_forename = input('Please enter customer forename:')
    customer_surname = input('Please enter customer surname:')
    for i, item in enumerate(houses, 1):
        print(i, item)

    sel_check = False

    while not sel_check:
        try:
            select = int(input('Please select a purchase: '))
            if select <= len(houses):
                sel_check = True
            else:
                print("ERROR PLEASE ENTER A VALID PROPERTY")
        except:
            print('ERROR PLEASE ENTER A VALID PROPERTY')

    sub_total = houses[select-1][3]
    print(sub_total)
    total_fees = 0


    if sub_total > 100000:
        total_fees += 3000+(sub_total-100000) * 0.2
    else:
        total_fees += sub_total *0.3

    

    final_total = sub_total+total_fees
    sale.append(customer_forename)
    sale.append(customer_surname)
    sale.append(sub_total)
    sale.append(final_total)
    sales.append(sale)

    print('Customer Receipt\n\n  FORENAME: {}  SURNAME: {}  PROPERTY COST:  {}  WITH STAMP DUTY:   {}'.format(*sales[-1]))
    print('\nTRANSACTION COMPLETE - PROPERTY REMOVED FROM SALES DATABASE\n')
    print (houses[select-1])
    del houses[select-1] 

def add_sale():
    print("Add a Sale")

    regioni = input("Please enter the region of the house: ")
    propertyi = input("Please enter the propety type: ")
    if propertyi in property_types:
        bedroomsi = input("Please enter the amount of bedrooms: ")
        costi = input("Please enter the cost: ")
        houses.insert(0, [regioni,propertyi,bedroomsi,costi])
        if regioni in ourregions:
            pass
        else:
            unique_list.insert(0, regioni)
            print("Added to unique regions!")
        print("Added to the market!")
    else:
            print("Not a valid property type.")



while True:
    menuselection = int(input(" WELCOME TO THE NEWHAVEN DASHBOARD \n\n Please select from the following menu options \n\n"
                              " 1: View current houses on market \n 2: Search for available houses in a region \n 3: Record"
                              " a sale \n 4: Add a new property for sale \n 5: Show Sales \n 6: Exit \n Please enter: "))


    if menuselection == 1:
        return_stock()
    if menuselection == 2:
        region_search()
    if menuselection ==3:
        house_sale()
    if menuselection==4:
        add_sale()
    if menuselection==5:
        show_sales()
         