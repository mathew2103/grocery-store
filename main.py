# TODO: BILLING


from tabulate import tabulate
import pickle
import time


# ---------------- Utility Functions ----------------------

      
def get_data():
    with open('items.pkl', 'rb') as fp:
        try:
            items = pickle.load(fp)
        except EOFError:
            return []
        return items

    
def format_data(items):
    
    for i in range(len(items)):
        item = items[i]
        item = list(item)
        item.insert(0, i+1)
        items[i] = item
    return items

# ---------------- User Interface ----------------------

def prompt(sleep = True):
    if sleep:
        time.sleep(5)
    print("")
    table = [
    ["Get Info", "1"],
    ["List all items", "2"],
    ["Billing", "3"],
    ["Admin Login", "4"],
    ["Exit", "5"]]
    
    
    print(tabulate(table))
    o = input("Select the suitable option: ")
    if o == "1":
        getInfo()
    elif o == "2":
        items = format_data(get_data())
        print(" ")
        print(tabulate(items, headers=["ID","Name","Cost","Stock"]))
        prompt()
    elif o == "4":
        login()
    else:
        exit()


def login():
    word = input("enter password:")
    if word == password:
        print("✅ Access Granted")
        
        adminmenu = [
            ["Add items", "1"],
            ["Update Stock", "2"],
            ["Remove item", "3"]]
        print(tabulate(adminmenu))

        o = input("Select the suitable option: ")
        if o == "1":
            addItems()
        elif o == "2":
            updateStock()
        elif o == "3":
            removeItem()
        
    else:
        print("❌ Access Denied")


# ---------------- OLD Admin Functions ----------------------

def getInfo():
    x = int(input("Enter ID of item: "))
    item = format_data(get_data())
    item = [items[x-1]]
    frame = tk.Frame(m)            

    print(tabulate(item, headers=["ID","Name","Cost","Stock"]))
    prompt()


def addItems():
    x = int(input("Enter number of items to add"))
    try:
        l = get_data()
    except FileNotFoundError:
        l = []

    for i in range(x):
        print(f"Item {i+1}/{x}")
        name = input("Enter name of item: ")
        cost = int(input("Enter cost of item: "))
        stock = int(input("Enter available stock: "))
        print(" ")
        l.append([name, cost, stock])
        
    with open('items.pkl', 'wb') as fp:
        pickle.dump(l, fp)
    print('Added',x, 'items')
    prompt()

def updateStock():
    x = int(input("Enter ID of item to update: "))
    
    items = get_data()
    if len(items) < x-1 or x < 1:
        print("No such item exists.. try again")
        return
    
    item = items[x-1]
    print("Item Name:", item[0])
    n = int(input("Enter new quantity: "))
    item[2] = n
    items[x-1] = item

    with open('items.pkl', 'wb') as fp:
        pickle.dump(items, fp)
    print('Updated stocks')
    prompt()

def removeItem():
    x = int(input("Enter ID of item to update: "))
    items = get_data()
    item = items[x-1]
    if input(f"Are you sure you want to remove {item[0]}? (yes/no)").lower() != "yes":
        return
    items.remove(item)

    with open('items.pkl', 'wb') as fp:
        pickle.dump(items, fp)
    print('Deleted')
    prompt()

#print("")
#print("Welcome to Mavika General Store")
#prompt(False)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# billing GUI
import PySimpleGUI as gui
# BASIC WORKING?  ILL INPUT (PRODUCT) ID AND QUANTIT
import tabulate as t

# WORKING!!!

#MAIN THINGS
price2 = []
infotable = []
head = ['ID','Product Name','Quantity','Price']
price1 = 0



import PySimpleGUI as gui
def gui_prompt():
    
    gui.theme("DarkAmber")
    
    #LAYOUT(S) AS PER REQUIREMENT
    layout1 = [
        ]


    layout2 = [
        ]


    layout3 = [
               [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False)],
               [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False)],
               [gui.Button("Add")],
               [gui.Table(values =  infotable, headings = head, key = "tablebill", justification = "centre")],
               [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
               [gui.Exit()] 
        ]


    layout4 = [
        ]
    
    #FINAL LAYOUT
    layout = [  [gui.TabGroup([[gui.Tab("Get information", layout1),
                                gui.Tab("admin", layout2),
                                gui.Tab("Make BILL", layout3),
                                gui.Tab("Stock OPADAtION", layout4)]])
        ]
]    

    window = gui.Window("General Mavika Store", layout)

    while True:
        event, values = window.read()

        
        if event == "Add":
            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            price1 = int(float(values["QTY"]))*int(float(data[int(values["ID"])][2]))
            infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price1])
            price2.append(price1)
            window["tablebill"].update(values = infotable)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)

        #MORE if if STATEMENTS AS REQUIRE HOPEFULLY
        
        
        if event == "Exit" or event == gui.WIN_CLOSED:
            break

    window.close()
#gui_prompt()

#gui_prompt()
def gui_prompt2():
    #MAIN THINGS

    from PIL import Image
    price2 = []
    infotable = []
    head = ['ID','Product Name','Quantity','Price']
    price1 = 0
    
    gui.theme("DarkAmber")

    # DIFFERENT LAYOUTS
    
    #MAIN MENU
    layout0 = [ [gui.Text("!!Welcome To Mavika store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
#                [gui.Image(filename = "cat.png", size = (150, 220),  expand_x = True, expand_y = True)],
                [gui.Button("Get Information"), gui.Button("List all Items"), gui.Button("Make BILL"), gui.Button("Admin Login"), gui.Button("Exit")]
        ]


    #GET INFORMATION 
    layout1 = [
        ]

   
    #ADMIN LOGIN
    layout2 = [ [gui.Text("Welcome to Admin Login", expand_x = "True", justification = "centre")],
                [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "NAME", do_not_clear = False)],
                [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "PASSWORD", do_not_clear = False)],
                [gui.Button("Enter"), gui.Button("Back", key = "back_login")]
        ]

   
    #UNDER ADMIN LOGIN - "STOCK UPDATION"
    layout21 = [ [gui.Text("Stock Updation")],
                 [gui.Button("Back", key = "back_stock")]
        ]

  
    #MAK BILL
    layout3 = [
               [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False, justification = "left", enable_events=True)],
               [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False, justification = "left")],
               [gui.Button("Add")],
               [gui.Table(values =  infotable, headings = head, key = "tablebill", justification = "centre")],
               [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
               [gui.Button("Back", key = "back_bill")] 
        ]      

    #LIST ALL ITEMS 
    layout4 = [
        ]

    #MAIN LAYOUT
    layout = [ [gui.Column(layout0, key = "l0"),
                gui.Column(layout1, key = "l1", visible = False),
                gui.Column(layout2, key = "l2", visible = False),
                gui.Column(layout21, key = "l21", visible = False),
                gui.Column(layout3, key = "l3", visible = False),
                gui.Column(layout4, key = "l4", visible = False)]
        ]

    # WINDOW
    window = gui.Window("Mavika Store", layout, resizable = True)


    #while-event loop
    while True:
        event, values = window.read()

        if event in (gui.WIN_CLOSED, "Exit"):
            break
        #*Get Info* starts
        if event == "Get Information":
            pass
        #*Get Info* ends



        # *Admin* start
        if event == "Admin Login":
            window["l2"].update(visible = True)
            window["l0"].update(visible = False)
        if event == "back_login":
            window["l0"].update(visible = True)
            window["l2"].update(visible = False)

        if event == "Enter":
            name = ["vinay", "kalpit", "mathew"]
            password = ["ayo", "yo"]
            if values["NAME"] in name and values["PASSWORD"] in password:
                window["l21"].update(visible = True)
                window["l2"].update(visible = False)
                #stock updation
            else:
                gui.Popup("YOU'RE NOT AUTHORISED PERSONNEl!!!")


        if event == "back_stock":
            window["l0"].update(visible = True)
            window["l21"].update(visible = False)
        # *Admin* end



        # *Bill*
        if event == "Make BILL":
            window["l3"].update(visible = True)
            window["l0"].update(visible = False)

        if event == "back_bill":
             window["l0"].update(visible = True)
             window["l3"].update(visible = False)
            
             
        if event == "Add" and values["ID"] == '' and values["QTY"] == '':
            gui.Popup("Please Enter ID and QUANTITY")


        if (event == "Add" and values["ID"] != '' and values["QTY"] != '') or values["ID"]:
            data = get_data()
                        
            if values["QTY"] == "":
                infotable.append([values["ID"], data[int(values["ID"]) - 1][0],"",""])
                window["tablebill"].update(values = infotable)
            else:
                    
                price1 = int(float(values["QTY"]))*int(float(data[int(values["ID"])][2]))
                infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price1])
                price2.append(price1)
                window["tablebill"].update(values = infotable)
                price = 0
                for i in price2:
                    price+=i
                window["p"].update(price)
        #^Bill^ end


        #*Items*starts
        if event == "List all Items":
            pass
        #*Items*starts
    window.close()
gui_prompt2()





    
