#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from unittest.mock import patch


# # Food Ordering Application Project
# 
# ## Overview
# 
# A food vendor has requested the development of a simple Food Ordering Application.  
# The purpose of this application is to allow customers to select food items, specify quantities, and receive a receipt displaying their total order cost.
# 
# Each part of this project represents a different function of the application responsible for capturing user input and generating the final receipt.
# 
# ---
# 
# ## Menu
# 
# The vendor offers the following items:
# 
# - **Pizza** — $26.00
# 
# - **Burger** — $22.00
# 
#    
# - **Noodles** — $15.00  
# 
# ---
# 
# ## Project Requirements
# 
# The application must:
# 
# 1. Display the available menu items.
# 2. Allow the user to select an item.
# 3. Accept the quantity for each selected item.
# 4. Allow users to order multiple items.
# 5. Calculate the total price for each item ordered.
# 6. Display a formatted receipt showing:
#    - Item name
#    - Quantity ordered
#    - Total price per item
# 
# ---
# 
# ## Important Note
# 
# - Users may order multiple items.
# - Users may order different quantities for each item.
# - Input validation must be handled properly.

# In[2]:


def display_menu():
    """
    Description: Prints the menu options for the food items available in the ordering app.
                 since the app only has 3 food items you can order we add a fourth option to exit
                 the menu when they are done ordering.
    """
    print("Menu:")
    print("1. Pizza - 26.00")
    print("2. Burger - 22.00")
    print("3. Noodles - 15.00")
    print("4. Exit Menu")


# In[3]:


def get_user_choice():
    """
    Description: Takes user input to get the number corresponding to the chosen food item from the menu.
                 Ensures the input is a valid choice between 1 and 4.
                 
                 If the input is not an integer return the error 
                 'Invalid input. Please enter a valid number.' 
                 
                 If the input is an integer but not between 1 and 4 return the error
                 'Invalid choice. Please enter a number between 1 and 4.' 
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return None if choice == 4 else choice
            else:
                print ('Invalid choice. Please enter a number between 1 and 4.' )
                
        except ValueError:
            print( 'Invalid input. Please enter a valid number.')


# In[4]:


class TestGetUserChoice(unittest.TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_valid_choice(self, mock_input):
        result = get_user_choice()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['invalid', '3'])
    def test_invalid_then_valid_choice(self, mock_input):
        result = get_user_choice()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['5', '4'])
    def test_invalid_then_exit_choice(self, mock_input):
        result = get_user_choice()
        self.assertIsNone(result)

tester = TestGetUserChoice()
tester.test_valid_choice()
tester.test_invalid_then_valid_choice()
tester.test_invalid_then_exit_choice()


# In[5]:


def get_quantity():
    """
    Description: Takes user input to get the quantity of the selected food item.
                 and ensures the input is a positive integer.

                 If the input is not an integer return the error 
                 'Invalid input. Please enter a valid number.' 
                 
                 If the input is a negative integer or zero return the error
                 'Quantity must be greater than 0.'
    """
    while True: 
        try:
            quantity = int(input("Enter quantity to buy: "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0")
        except ValueError:
            print ("Invalid input. Please enter a valid number.")


# In[6]:


class TestGetQuantity(unittest.TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_valid_quantity(self, mock_input):
        result = get_quantity()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['invalid', '5'])
    def test_invalid_then_valid_quantity(self, mock_input):
        result = get_quantity()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['0', '-2', '4'])
    def test_invalid_then_valid_quantity_with_negative_input(self, mock_input):
        result = get_quantity()
        self.assertEqual(result, 4)

tester = TestGetQuantity()
tester.test_valid_quantity()
tester.test_invalid_then_valid_quantity()
tester.test_invalid_then_valid_quantity_with_negative_input()


# In[7]:


def get_item_name(choice):
    """
    Description: Retrieves and returns the name of a food item 
    based on the user's choice number from the menu.
    """
    # YOUR CODE HERE
    food_name = {1:'Pizza',
                   2: 'Burger',
                   3: 'Noodles',
                   4: 'Exit menu'}
    return food_name[choice]


# In[8]:


assert get_item_name(1) == 'Pizza'
assert get_item_name(2) == 'Burger'
assert get_item_name(3) == 'Noodles'


# In[9]:


def get_item_price(choice):
    """
    Description: Retrieves and returns the price of a food item based on 
    the user's choice number from the menu.
    """

    display_price = {1: 26.00,
                   2: 22.00,
                   3: 15.00,}
                   
    return display_price[choice] 


# In[10]:


assert get_item_price(1) == 26.00
assert get_item_price(2) == 22.00
assert get_item_price(3) == 15.00


# In[11]:


def calculate_total_price(item_price, quantity):
    """
    Description: Calculates and returns the total price of a specific food item 
    based on its price and the quantity ordered.
    """
    
    total_price = item_price * quantity
    return total_price 


# In[12]:


assert calculate_total_price(5, 2) == 10


# In[13]:


def place_order():
    """
    Description: Manages the process of adding items to a shopping cart. 
                 USES A DICTIONARY FOR THE CART.
                 Calls other functions to get user choices, quantities, and calculates total prices.

                 Your cart should look something like this assuming this user ordered 3 pizzas and 3 burgers.
                 {
                    'Pizza': {'quantity': 3, 'total_price': 19500},
                    'Burger': {'quantity': 3, 'total_price': 9000}
                 }
    """
    
    cart = {}
    while True:
        display_menu()
        choice = get_user_choice()
        if choice is None:
            break
        
        
        item_name = get_item_name(choice)
        item_price = get_item_price(choice)
        quantity = get_quantity()
                
        total_price = calculate_total_price(item_price, quantity)
        
        cart[item_name] = {
                "quantity": quantity,
                "total_price" : total_price}
        
        
        
        print (cart)
    return cart


# In[14]:


class TestPlaceOrder(unittest.TestCase):
    @patch('__main__.get_user_choice', side_effect=[1, 2, None])
    @patch('__main__.get_quantity', return_value=3)
    def test_place_order(self, mock_get_quantity, mock_get_user_choice):
        result = place_order()

        # Assertions based on the expected behavior of place_order
        expected_result = {'Pizza': {'quantity': 3, 'total_price': 78.00},
                           'Burger': {'quantity': 3, 'total_price': 66.00}}
        self.assertEqual(result, expected_result)

        # Check that get_user_choice was called three times
        self.assertEqual(mock_get_user_choice.call_count, 3)

        # Check that get_quantity was called twice (for the two items added)
        self.assertEqual(mock_get_quantity.call_count, 2)

tester = TestPlaceOrder()
tester.test_place_order()


# In[15]:


def check_out(cart):
    """
    Description: Finalizes the order by displaying the contents of the shopping cart, including quantities and total prices.
                 Prints the total order price like a receipt.

                 The reciept would look like this if the cart is empty
                 
                     Your cart is empty. No items to check out.


                 If the Cart is has items in it then the receipt should look exactly like this

                     Checking out...
                     Your order details:
                     Item 1: Quantity - 2, Total Price - 52.00
                     Item 2: Quantity - 3, Total Price - 44.00
                     Total Order Price: 96.00
                     Thank you for ordering!
    """

    if not cart:
        print("Your cart is empty. No items to check out.")
        return
    print ("Checking out...")
    print("Your order details:")

    total_order_price = 0
    for i, (item, details) in enumerate(cart.items(), start=1 ):
        quantity = details["quantity"]
        total_price = details["total_price"]
        print(f"Item {i}: Quantity - {quantity}, Total Price - {total_price}")
        total_order_price += total_price

    print(f"Total Order Price: {total_order_price}")
    print("Thank you for ordering!")


# In[16]:


class TestCheckOut(unittest.TestCase):
    @patch('builtins.print')
    def test_check_out_empty_cart(self, mock_print):
        cart = {}
        check_out(cart)
        mock_print.assert_called_with("Your cart is empty. No items to check out.")

    @patch('builtins.print')
    def test_check_out_non_empty_cart(self, mock_print):
        cart = {
            'Item 1': {'quantity': 2, 'total_price': 20},
            'Item 2': {'quantity': 3, 'total_price': 15}
        }
        check_out(cart)

        # Verify that the expected output was printed
        expected_output_1 = [
            "Checking out...",
            "Your order details:",
            "Item 1: Quantity - 2, Total Price - $20",
            "Item 2: Quantity - 3, Total Price - $15",
            "Total Order Price: $35",
            "Thank you for ordering!"
        ]
        
        # Second expected output (alternate formatting, for example)
        expected_output_2 = [
            "Checking out...",
            "Your order details:",
            "Item 1: Quantity - 2, Total Price - 20",
            "Item 2: Quantity - 3, Total Price - 15",
            "Total Order Price: 35",
            "Thank you for ordering!"
        ]

        # Convert expected outputs to lists of mock calls
        calls_1 = [unittest.mock.call(output) for output in expected_output_1]
        calls_2 = [unittest.mock.call(output) for output in expected_output_2]

        try:
            # Check first expected output
            mock_print.assert_has_calls(calls_1, any_order=False)
        except AssertionError:
            # If the first expected output fails, check the second one
            mock_print.assert_has_calls(calls_2, any_order=False)


tester = TestCheckOut()
tester.test_check_out_empty_cart()
tester.test_check_out_non_empty_cart()


# In[17]:


def food_ordering_app():
    """
    Description: The main function that initiates the food ordering application.
                 Calls place_order() to build the shopping cart and then calls check_out() to complete the order.

                 NOTE THAT IF ANY OF THE OTHER FUNCTIONS ARE NOT CORRECTLY WRITTEN THIS WILL FAIL
                 PLEASE DO NOT MODIFY THIS CELL
    """
    print("Welcome to the Food Ordering App!")
    cart = place_order()
    check_out(cart)


# In[18]:


class TestFoodOrderingApp(unittest.TestCase):
    @patch('builtins.print')
    @patch('__main__.place_order', return_value={'Item 1': {'quantity': 2, 'total_price': 20}})
    @patch('__main__.check_out')
    def test_food_ordering_app(self, mock_check_out, mock_place_order, mock_print):
        food_ordering_app()

        # Verify that the expected calls were made
        mock_print.assert_called_with("Welcome to the Food Ordering App!")
        mock_place_order.assert_called_once()
        mock_check_out.assert_called_once()

tester = TestFoodOrderingApp()
tester.test_food_ordering_app()

if __name__ == "__main__":
    food_ordering_app()
