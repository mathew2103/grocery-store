# TODO: BILLING

from tabulate import tabulate
import pickle
import time

password = "mathew21"

def get_data():
    with open('items.pkl', 'rb') as fp:
        try:
            items = pickle.load(fp)
            print(items)
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


def getInfo():
    x = int(input("Enter ID of item: "))
    items = format_data(get_data())
    item = [items[x-1]]
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
        cost = input("Enter cost of item: ")
        stock = input("Enter available stock: ")
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

print("")
print("Welcome to Mavika General Store")
prompt(False)
