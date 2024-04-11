import random as rand 
import datetime as dt 
import qrcode as qr 
import pandas as pd 
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import time, hashlib
import wsgiserver
import time as t 
import sys
'''
Datamining project that take a simulated to emulation to produce a blockchain 
Think about ACSII
'''

def CEOgreet():
    print("Welcome to the plaza datamining project.\n")
    print("CEO Tyler Eavey")
    print("Tylerwe69@gmail.com")
    
def select():
    command = input("Enter a command from the menu.\n")
    return command 

def genUsername(self):
    uname = self.fullname[0:10:2]
    #with open to save info to csv file
    return uname

app = Flask(__name__)

class Business():
    def __init__(self):
        self.business = [] #Task List to run to achieve objective of daily business
    
    def openBusiness():
        access_id = input("Enter access ID or username.\n")
        if len(access_id) == 3:
            emps =Employee()
            menu = Employee.mainMenu()
        elif len(access_id) == 4:
            mans = Manager()
            menu = Manager.mainMenu()
        elif access_id:
            customer = Customer()
            menu = Customer.mainMenu()
        else:
            print("GoodBye.\n")
            sys.exit()
        return access_id
    
    #Function to add the business
    
    #Function to close the business 
    
    
class Customer:
    def __init__(self):
        self.customer = {}
        
    def register():
        fname = input("Enter your first name.\n")
        while len(fname) == 0:
            fname = input("Please enter your first name.\n")
        lname = input("Enter your last name.\n")
        while len(lname) == 0:
            lname = input("Please enter your last name.\n")
        fullname = lname, fname 
        print("To generate a username type gen.\n")
        uname = input("Enter a usernameor type gen.\n")
        if uname.lower() == "gen":
            genUsername()
        else:
            uname = input("Enter a username.\n")
            
        pwd = input("Enter a password.\n")
        while len(pwd) == 0:
            pwd = input("Please enter a password.\n")
        confirm_pwd = input("Confirm Password.\n")
        while pwd != confirm_pwd:
            confirm_pwd = input("Password did not match. Try Again.\n")
        return fullname, uname, pwd, confirm_pwd
   
    def mainMenu():
        print("Customer Access.\n")
        print("1. place an order.\n")
        print("2. return to main menu\n")
        command = select()
        if command.lower() == "1":
            Order.add_items
            #Remeber to add a remove items 
        elif command.lower() == "2":
            Customer.mainMenu()
        else:
            sys.exit()
        
class Employee():
    def __init__(self):
        self.employee = {}
        self.current_emp = []
        
    def register(self):
          emp_id = rand.randint(100, 999)
          self.current_emp.append(self.current_emp)
          print(self.current_emp)
          return emp_id
    
    def mainMenu():
        print("Employee Access.\n")
        print("1. clock-in\n")
        print("2. clock-out.\n")
        print("3. to return to main menu.\n")
        command = select()
        if command.lower() == "1":
            Employee.clockIn()
        elif command.lower() == "2":
            Employee.clockOut()
        elif command.lower() == "3":
            Employee.mainMenu()
        else:
            sys.exit()
        
    def clockIn(self):
             current_time = dt.datetime.now()
             formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
             with open("work_hours.txt", "a") as file:
                file.write(f"Clock in: {formatted_time}\n")
        
    def clockOut(self):
           current_time = dt.datetime.now()
           formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
           with open("work_hours.txt", "a") as file:
                file.write(f"Clock out: {formatted_time}\n")
                
    def calculate_total_time():
            with open("work_hours.txt", "r") as file:
                lines = file.readlines()
                total_time = dt.timedelta()
                last_clock_in = None

            for line in lines:
                if line.startswith("Clock in"):
                    last_clock_in = dt.datetime.strptime(line.split(": ")[1].strip(), "%Y-%m-%d %H:%M:%S")
                elif line.startswith("Clock out") and last_clock_in:
                    clock_out_time = dt.datetime.strptime(line.split(": ")[1].strip(), "%Y-%m-%d %H:%M:%S")
                    total_time += clock_out_time - last_clock_in
                    last_clock_in = None

            return total_time
        
class Manager:
    def __init__(self):
        self.manager = {}
        
    def mainMenu():
        print("Manager Access.\n")
        print("1. to manage orders.\n")
        print("2. to manage inventory.\n")
        print("3. to view and manage reports\n")
        print("4. to manage the employee.\n")
        print("5. to terminate the application.\n")
        command = select()
        if command.lower() == "1":
            Order()
        elif command.lower() == "2":
            stock()
            Inventory.display_inventory()
            
        elif command.lower() == "3":
            pass
        elif command.lower() == "4":
            Manager.mainMenu()
        else:
            print("GoodBye.\n")
            sys.exit()
            
    def register():
        man_id = rand.randint(1000, 9999)
        return man_id 
    
    def inventory():
        stock()
        
     
class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self):
        name = input("Enter the item name to add to inventory: \n")
        quantity = int(input("Enter the quantity: \n"))
        price = float(input("Enter the price: \n"))
        item = InventoryItem(name, quantity, price)
        self.items.append(item)
        
    def remove_item(self):
        name = input("Enter the item name to remove from inventory: \n")
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"{name} removed from inventory.\n")
                return
        print(f"{name} not found in inventory.\n")

    def display_inventory(self):
        print("Inventory:\n")
        if not self.items:
            print("Inventory is empty.")
            return
        else:
            inventory_data = {'Name': [], 'Quantity': [], 'Price': []}
            for item in self.items:
                inventory_data['Name'].append(item.name)
                inventory_data['Quantity'].append(item.quantity)
                inventory_data['Price'].append(item.price)
            df = pd.DataFrame(inventory_data)
            print(df)

def stock():
    inventory = Inventory()
    while True:
        print("\n1. Add Item\n2. Remove Item\n3. Display Inventory\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): \n")
        if choice == '1':
            inventory.add_item()
        elif choice == '2':
            inventory.remove_item()
        elif choice == '3':
            inventory.display_inventory()
        elif choice == '4':
            print("Exiting program. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")
            
class Application:
    def __init__(self):
        self.applications = {}

    def submit_application(self, application_id, name, position):
        """
        Submit a job application.

        Args:
            application_id (int): The unique identifier for the application.
            name (str): The name of the applicant.
            position (str): The position applied for.

        Returns:
            str: Confirmation message.
        """
        if application_id in self.applications:
            return f"Application with ID {application_id} already exists."
        self.applications[application_id] = {'name': name, 'position': position}
        return f"Application submitted successfully with ID {application_id}."

    def get_application_info(self, application_id):
        """
        Retrieve information about a job application.

        Args:
            application_id (int): The unique identifier for the application.

        Returns:
            dict: Information about the application if found, None otherwise.
        """
        return self.applications.get(application_id)

    def remove_application(self, application_id):
        """
        Remove a job application.

        Args:
            application_id (int): The unique identifier for the application.

        Returns:
            str: Confirmation message.
        """
        if application_id not in self.applications:
            return f"Application with ID {application_id} not found."
        del self.applications[application_id]
        return f"Application with ID {application_id} removed successfully."
    
      
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.total_price = 0

    def add_item(self):
        self.product_name = input("Enter the product name.\n")
        self.quantity = input("How much at one time?\n")
        self.price = int(input("How many pennies are we counting?\n"))
        self.items.append((self.product_name, self.quantity, self.price))
        self.total_price += self.quantity * self.price

    def remove_item(self, product_name, quantity):
        for item in self.items:
            if item[0] == product_name:
                if item[1] >= quantity:
                    item[1] -= quantity
                    self.total_price -= quantity * item[2]
                    if item[1] == 0:
                        self.items.remove(item)
                    return True
                else:
                    print(f"Requested quantity exceeds available quantity in the order.")
                    return False
        print(f"{product_name} not found in the order.")
        return False
    
    def orderStaus():
        time = 120
        while time == 120:
            time -= 2
        if time == 0:
            print("Order is done.\n")
            print("Driver is on the way.\n")
        else:
            print(f"Remaining Time: {time}.\n")
            
    def calculate_total_price(quantity, price):
        sub_total = quantity * price
        tax = 0.09
        total = sub_total * tax 
        grand_total = sub_total + total
        print(f"Your grand total for this order {grand_total}.\n")
        

    # Other methods for updating order status, calculating total price, etc.

class POS:
    def __init__(self, manager):
        self.manager = manager
        self.cart = []
        self.current_order = None

    def start_order(self, customer):
        self.current_order = Order(customer)

    def add_to_cart(self, product_name, quantity):
        if self.current_order:
            if self.manager.add_to_cart(product_name, quantity):
                self.current_order.add_item(product_name, quantity, self.manager.get_price(product_name))
                print(f"{quantity} {product_name}(s) added to cart.")
        else:
            print("Please start an order first.")

    def remove_from_cart(self, product_name, quantity):
        if self.current_order:
            if self.manager.remove_from_cart(product_name, quantity):
                self.current_order.remove_item(product_name, quantity)
                print(f"{quantity} {product_name}(s) removed from cart.")
        else:
            print("Please start an order first.")

    def checkout(self):
        if self.current_order:
            self.current_order.calculate_total_price()
            #Process Payment 
            # Update inventory
            # Generate receipt
            self.current_order = None
            self.cart = []
        else:
            print("Please start an order first.")

    # Other methods for viewing cart, managing inventory, etc.

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", time.time(), "Genesis Block", calculate_hash(0, "0", time.time(), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

@app.route('/')
def index():
    return render_template('index.html, blockchain=blockchain')

@app.route('/mine', methods=['GET', 'POST'])
def mine():
    if request.method == 'POST':
        data = request.form['blocks']
        new_block = create_new_block(previous_block, data)
        blockchain.append(new_block)
        previous_block = new_block
        return redirect(url_for('index'))
    return render_template('mine.html')


# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add blocks to the blockchain
num_blocks_to_add = 100

for i in range(1, num_blocks_to_add + 1):
    new_block_data = f"Block #{i} Data"
    new_block = create_new_block(previous_block, new_block_data)
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block #{i} has been added to the blockchain!\n")
    print(f"Hash: {new_block.hash}\n")
    
class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

    def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=self.current_data)
        self.current_data = []
        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.calculate_hash != block.prev_hash:
            return False
        elif not BlockChain.verifying_proof(block.proof_no,
                                            prev_block.proof_no):
            return False
        elif block.timestamp <= prev_block.timestamp:
            return False
        return True

    @staticmethod
    def proof_of_work(last_proof):
        '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
         f is the previous f'
         f' is the new proof
        '''
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        #verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self):
        return self.chain[-1]

    def block_mining(self, details_miner):
        self.new_data(
            sender="0",  #it implies that this node has created a new block
            receiver=details_miner,
            quantity=
            1,  #creating a new block (or identifying the proof number) is awarded with 1
        )

        last_block = self.latest_block
        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)
        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)
        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):
        #obtains block object from the block data
        print(Block( block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data(['timestamp'])))
        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data(['timestamp']))

if __name__ == "__main__":
    print("the plaze project.\n")
    CEOgreet()
    Business.openBusiness()
    '''server = wsgiserver.WSGIServer(app)
    server.start()
    app.run(debug=True)'''
   
    
    
    


    



