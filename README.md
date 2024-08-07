# Basic Banking System with Python

## About Project
This project is a simple banking system implemented in Python. It allows users to create accounts, deposit money, withdraw money, and check account details. The data is managed using a dictionary. 

## Project Structure
1. Defining the Banking Class
2. Initialization (__init__ method)
3. Menu Method
4. Account Creation Method
5. Deposit Method
6. Withdrawal Method
7. Check Account Details Method
8. Creating Object and Displaying Data

## Step-by-Step Process:

### Defining The Banking Class:

<img width="691" alt="Screenshot 2024-08-07 at 20 05 59" src="https://github.com/user-attachments/assets/61dd53eb-25e6-493d-8790-73e343443e12">

#### Key Points - 
1. We created a Banking Class
2. Initialize a Dictionary to store all the information
3. Calling the menu method to display the user interaction input

### Menu Method

<img width="691" alt="Screenshot 2024-08-07 at 20 14 30" src="https://github.com/user-attachments/assets/6de8ed8b-6cf9-4f47-bd13-645a402710e4">

#### Key Points - 
1. Displays a menu with options to create an account, deposit money, withdraw money, check account details, or exit the system.
2. Based on the user's choice, it calls the respective method.

### Account Creation Method

<img width="691" alt="Screenshot 2024-08-07 at 20 22 48" src="https://github.com/user-attachments/assets/1cf3006f-9a92-4bea-93d7-efb88264f5ba">

<img width="691" alt="Screenshot 2024-08-07 at 20 26 05" src="https://github.com/user-attachments/assets/a2b03108-937d-42ae-87f0-7d8a0ea48ebb">

#### Key Points - 
1. Prompts the user for various details (account number, first name, last name, etc.) and stores them in the dictionary.
2. Includes nested functions phone, pin, and aadhar to validate the input length for phone number, pincode, and Aadhar number.
3. Initializes the account balance to 0.

### Account Deposit Method

<img width="691" alt="Screenshot 2024-08-07 at 20 29 42" src="https://github.com/user-attachments/assets/73bc8296-5557-4b08-a299-1207eb6b0da4">

#### Key Points - 
1. Asks for the account number and amount to deposit.
2. If the account exists, it adds the amount to the current balance and prints the updated balance.
3. If the account doesn't exist, it prints an error message.

### Withdrawal Method

<img width="691" alt="Screenshot 2024-08-07 at 20 32 20" src="https://github.com/user-attachments/assets/0c6682be-f90f-4158-9960-e2600e493292">

#### Key Points - 
1. Asks for the account number and amount to withdraw.
2. If the account exists, it checks if there is enough balance to withdraw the amount.
3. If there is enough balance, it deducts the amount and prints the remaining balance.
4. If there is not enough balance, it prints an "Insufficient Balance" message.
5. If the account doesn't exist, it prints an error message "Account Does Not Exist".

### Check Method

<img width="691" alt="Screenshot 2024-08-07 at 20 38 07" src="https://github.com/user-attachments/assets/8678a1a4-b009-4e8d-be82-e09865ecf500">

#### Key Points - 
1. Asks for the account number to check the details.
2. If the account exists, it prints all the details of the account.
3. If the account doesn't exist, it prints an error message.

## Creating Object and Displaying Data
1. Creates an object y of the Banking class, which starts the program and displays the menu.

### Usage
1. Run the Program: Execute the script.
2. Follow the Menu: Choose the desired option from the menu to create an account, deposit money, withdraw money, or check account details.
4. Enter Details: Provide the required details based on the chosen option.
5. View Data: The program prints the current data stored in the banking system.
