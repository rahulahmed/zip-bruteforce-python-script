# Custom Python Script for Brute-Forcing Password-Protected Zip Files by Rahul Ahmed.

##This simple Python script is designed to brute-force a password-protected zip file by trying various passwords from a provided list. Follow the steps below to configure and use the script.

### Prerequisites
A password list (password_list.txt or similar).
A zip file that is password-protected and locked.
Usage Instructions
### Step 1: Configure the Password List
Make sure you have a list of passwords in a .txt file. This list will be used to attempt unlocking the zip file.

### Step 2: Update the Script with Your Password List
In the zip.py file, locate line 25:
### password_list = 'path/to/your/password_list.txt'
### Replace 'path/to/your/password_list.txt' with the actual path to your password list file.

### Step 3: Update the Script with the Target Zip File
Locate line 27 in the zip.py file:

zip_file = 'path/to/your/locked.zip'
Replace 'path/to/your/locked.zip' with the correct path and name of your password-protected zip file.

### Step 4: Run the Script
Once the above configurations are made, you can execute the script using any Python-compatible IDE or terminal.
