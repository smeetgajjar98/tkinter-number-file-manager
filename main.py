'''
Name: Smeet Bansibhai Gajjar
Student ID: 00853429
This is a final project of Intro to Script Programming/Python.
'''
import tkinter as tk
from tkinter import simpledialog
import random

class Project:
    def __init__(self): # Initialization of list and string.
        self.file_name = "" 
        self.nums = []


    # This method will create a file with the name of the user's choice.
    def select_Create_File(self, file_name):
        self.file_name = file_name + ".txt"
        try: # If the file already exists, it will read the numbers from the file.
            with open(self.file_name, "r") as file:
                # Read the contents of the file
                file_content = file.read()
                # Split the string into a list of strings
                content_list = file_content.split()
                # Create an empty list to store the numbers
                self.nums = []
                # Iterate through each string in the list
                for num in content_list:
                    # Convert the string to an integer and append it to the list
                    self.nums.append(int(num))


        except FileNotFoundError: # If the file does not exist, it will create a new file.
            open(self.file_name, "a").close()


    # This method display the numbers in the file.
    def display_All_Numbers(self, text_widget):
        if not self.file_name:
            text_widget.insert(tk.END, "No file selected!\n")
            return
        if not self.nums:
            text_widget.insert(tk.END, "No numbers in the file!\n")
            return
        total = sum(self.nums) # This will calculate the total of the numbers in the file.
        avg = total / len(self.nums)
        text_widget.insert(tk.END, f"Total: {total}\nAverage: {avg}\nNumbers: {self.nums}\n") # This will display the total and average of the numbers in the file.


    # This method will sort the numbers in the file
    def display_Sorted_Numbers(self, text_widget):
        if not self.file_name:
            text_widget.insert(tk.END, "No file selected!\n")
            return
        if not self.nums:
            text_widget.insert(tk.END, "No numbers in the file!\n")
            return
        sorted_numbers = sorted(self.nums)
        text_widget.insert(tk.END, f"Sorted Numbers: {sorted_numbers}\n")

    # This method will search for the number of occurrences of a number in the file.
    def search_Occurs(self, target, text_widget):
        if not self.file_name:
            text_widget.insert(tk.END, "No file selected!\n")
            return
        if not self.nums:
            text_widget.insert(tk.END, "No numbers in the file!\n")
            return
        try:
            target = int(target)
            count = self.nums.count(target)
            if count == 0:
                text_widget.insert(tk.END, f"{target} Number not found in the selected file.\n")
            else:
                text_widget.insert(tk.END, f"Number of occurrences of {target}: {count}\n")
        except ValueError:
            text_widget.insert(tk.END, "Please enter a valid number.\n")

    # This method will display the largest number in the file.
    def display_Largest_Number(self, text_widget):
        if not self.file_name:
            text_widget.insert(tk.END, "No file selected!\n")
            return
        if not self.nums:
            text_widget.insert(tk.END, "No numbers in the file!\n")
            return
        largest = max(self.nums) # Find the largest number in the list.
        text_widget.insert(tk.END, f"Largest Number: {largest}\n")

    # This method will append random numbers to the file based on the user's input.
    def append_Number(self, text_widget):
        if not self.file_name:
            text_widget.insert(tk.END, "No file selected!\n")
            return
        count = simpledialog.askinteger("Append Random Numbers", "How many random numbers do you want to add?")
        if count is not None:
            if count <=0:
                text_widget.insert(tk.END, "Please enter a positive number greater than 0.")
                return
            for _ in range(count):
                num = random.randint(1, 1000)
                self.nums.append(num)
            with open(self.file_name, "a") as file:
                file.write('\n'.join(map(str, self.nums[-count:])) + '\n')
            text_widget.insert(tk.END, f"{count} random numbers appended successfully!\n")

    # This method will encrypt tha contents of the file by calling the Caesar cipher.
    def encrypt_File(self, text_widget):
        if not self.file_name:
            text_widget.insert(tk.END, "No file selected!\n")
            return
        try:
            with open(self.file_name, "r") as file:
                data = file.read()
            cipher_text = self.caesar_cipher(data, 3)  # Shift by 3 positions
            with open(self.file_name, "w") as file:
                file.write(cipher_text)
            text_widget.insert(tk.END, "File encrypted successfully!\n")
        except Exception as e:
            text_widget.insert(tk.END, f"Encryption failed: {str(e)}\n")

    # This method will decrypt the contents of the file by calling the Caesar cipher.
    def decrypt_File(self, text_widget):
        if not self.file_name:
            text_widget.insert(tk.END, "No file selected!\n")
            return
        try:
            with open(self.file_name, "r") as file:
                data = file.read()
            plain_text = self.caesar_cipher(data, -3)  # Shift back by 3 positions
            with open(self.file_name, "w") as file:
                file.write(plain_text)
            text_widget.insert(tk.END, "File decrypted successfully!\n")
        except Exception as e:
            text_widget.insert(tk.END, f"Decryption failed: {str(e)}\n")

    # This method will encrypt the contents of the file by calling the Caesar cipher.
    def caesar_cipher(self, text, shift):
        data_cipher = ""
        for char in text:
            if char.isdigit():
                shifted = int(char) + shift
                if shifted < 0:
                    shifted += 10  # Wrap around for negative shifts
                elif shifted > 9:
                    shifted -= 10  # Wrap around for positive shifts
                data_cipher += str(shifted)
            else:
                data_cipher += char
        return data_cipher


# This class will handle the GUI for the program.
class GUI:
    def __init__(self, root):
        self.processor = Project()
        self.root = root


        # Actual GUI code starts.
        self.root.title("UNH Scripting w/Python")
        
        self.label = tk.Label(root, text="UNH Scripting w/Python", font=("Helvetica", 16))
        self.label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n")

        self.filename_entry = tk.Entry(root)
        self.filename_entry.grid(row=1, column=0, columnspan=2, pady=5, sticky="ew")

        self.select_button = tk.Button(root, text="Select/Create File", command=self.select_Create_File)
        self.select_button.grid(row=2, column=0, columnspan=2, sticky="ew")

        self.display_text = tk.Text(root, height=20, width=50)
        self.display_text.grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")

        self.display_all_button = tk.Button(root, text="Display All", command=self.display_All_Numbers)
        self.display_all_button.grid(row=4, column=0, pady=5, sticky="ew")

        self.display_sorted_button = tk.Button(root, text="Display Sorted", command=self.display_Sorted_Numbers)
        self.display_sorted_button.grid(row=4, column=1, pady=5, sticky="ew")

        self.search_button = tk.Button(root, text="Search/Occurs", command=self.search_Occurs)
        self.search_button.grid(row=5, column=0, pady=5, sticky="ew")

        self.display_largest_button = tk.Button(root, text="Display Largest", command=self.display_Largest_Number)
        self.display_largest_button.grid(row=5, column=1, pady=5, sticky="ew")

        self.append_button = tk.Button(root, text="Append Number", command=self.append_Number)
        self.append_button.grid(row=6, column=0, pady=5, sticky="ew")

        self.encrypt_button = tk.Button(root, text="Encrypt", command=self.encrypt_File)
        self.encrypt_button.grid(row=6, column=1, pady=5, sticky="ew")

        self.decrypt_button = tk.Button(root, text="Decrypt", command=self.decrypt_File)
        self.decrypt_button.grid(row=7, column=0, pady=5, sticky="ew")

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.grid(row=7, column=1, pady=5, sticky="ew")


    # This function gets a file name from user or creates a file.
    def select_Create_File(self):
        file_name = self.filename_entry.get()
        self.processor.select_Create_File(file_name)
        self.display_text.delete(1.0, tk.END)
        self.display_text.insert(tk.END, f"File {file_name}.txt selected/created successfully!\n")

    # This function displays all numbers from the file.
    def display_All_Numbers(self):
        self.display_text.delete(1.0, tk.END)
        self.processor.display_All_Numbers(self.display_text)

    # This function sorts the numbers from the file.
    def display_Sorted_Numbers(self):
        self.display_text.delete(1.0, tk.END)
        self.processor.display_Sorted_Numbers(self.display_text)

    # This function searches for a number in the file.
    def search_Occurs(self):
        target = simpledialog.askstring("Search", "Enter number to search:")
        if target is not None:
            self.processor.search_Occurs(target, self.display_text)

    # This function displays the largest number in the file.
    def display_Largest_Number(self):
        self.display_text.delete(1.0, tk.END)
        self.processor.display_Largest_Number(self.display_text)

    # This function displays the smallest number from the file.
    def append_Number(self):
        self.display_text.delete(1.0, tk.END)
        self.processor.append_Number(self.display_text)

    # This function encrypts the file content.
    def encrypt_File(self):
        self.display_text.delete(1.0, tk.END)
        self.processor.encrypt_File(self.display_text)

    # This function decrypts the file content.
    def decrypt_File(self):
        self.display_text.delete(1.0, tk.END)
        self.processor.decrypt_File(self.display_text)


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
