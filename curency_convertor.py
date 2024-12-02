# import tkinter as tk
# from tkinter import ttk, messagebox


# class CurrencyConverter:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Currency Converter")
#         self.root.geometry("400x300")
#         self.root.resizable(False, False)

#         # Exchange rates (modifiable)
#         self.exchange_rates = {
#             "USD": {"INR": 82.50, "EUR": 0.92, "GBP": 0.80},
#             "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0097},
#             "EUR": {"USD": 1.08, "INR": 88.80, "GBP": 0.87},
#             "GBP": {"USD": 1.25, "INR": 102.50, "EUR": 1.15},
#         }

#         self.create_widgets()

#     def create_widgets(self):
#         # Title Label
#         title_label = tk.Label(self.root, text="Currency Converter", font=("Arial", 16, "bold"))
#         title_label.pack(pady=10)

#         # Input Frame
#         input_frame = tk.Frame(self.root)
#         input_frame.pack(pady=10)

#         # From Currency
#         from_label = tk.Label(input_frame, text="From:")
#         from_label.grid(row=0, column=0, padx=5, pady=5)

#         self.from_currency = ttk.Combobox(input_frame, values=list(self.exchange_rates.keys()), state="readonly")
#         self.from_currency.grid(row=0, column=1, padx=5, pady=5)
#         self.from_currency.set("USD")

#         # To Currency
#         to_label = tk.Label(input_frame, text="To:")
#         to_label.grid(row=1, column=0, padx=5, pady=5)

#         self.to_currency = ttk.Combobox(input_frame, values=list(self.exchange_rates.keys()), state="readonly")
#         self.to_currency.grid(row=1, column=1, padx=5, pady=5)
#         self.to_currency.set("INR")

#         # Amount Entry
#         amount_label = tk.Label(input_frame, text="Amount:")
#         amount_label.grid(row=2, column=0, padx=5, pady=5)

#         self.amount_entry = tk.Entry(input_frame)
#         self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

#         # Convert Button
#         convert_button = tk.Button(self.root, text="Convert", command=self.convert_currency, bg="#4CAF50", fg="white")
#         convert_button.pack(pady=10)

#         # Result Label
#         self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"), fg="blue")
#         self.result_label.pack(pady=10)

#     def convert_currency(self):
#         from_currency = self.from_currency.get()
#         to_currency = self.to_currency.get()
#         amount = self.amount_entry.get()

#         try:
#             # Validate input amount
#             amount = float(amount)
#             if amount <= 0:
#                 raise ValueError("Amount must be positive.")

#             # Perform conversion
#             if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates[from_currency]:
#                 messagebox.showerror("Error", f"Conversion from {from_currency} to {to_currency} is not supported.")
#                 return

#             rate = self.exchange_rates[from_currency][to_currency]
#             converted_amount = amount * rate

#             # Display result
#             self.result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

#         except ValueError:
#             messagebox.showerror("Invalid Input", "Please enter a valid numeric amount.")

#         except Exception as e:
#             messagebox.showerror("Error", str(e))


# # Run the application
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = CurrencyConverter(root)
#     root.mainloop()
class CurrencyConverter:
    def __init__(self):
        # Initialize exchange rates (modifiable)
        self.exchange_rates = {
            "USD": {"INR": 82.50, "EUR": 0.92, "GBP": 0.80},
            "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0097},
            "EUR": {"USD": 1.08, "INR": 88.80, "GBP": 0.87},
            "GBP": {"USD": 1.25, "INR": 102.50, "EUR": 1.15},
        }

    def display_supported_currencies(self):
        print("Supported currencies:")
        for currency in self.exchange_rates:
            print(f"  {currency}")
        print()

    def convert_currency(self, from_currency, to_currency, amount):
        try:
            rate = self.exchange_rates[from_currency][to_currency]
            converted_amount = amount * rate
            return converted_amount
        except KeyError:
            print(f"Conversion from '{from_currency}' to '{to_currency}' is not supported.")
            return None

    def add_currency(self, currency_code):
        if currency_code in self.exchange_rates:
            print(f"{currency_code} already exists in the system.")
            return
        self.exchange_rates[currency_code] = {}
        print(f"Added currency '{currency_code}' successfully!")

    def add_conversion_rate(self, from_currency, to_currency, rate):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            print("One or both currencies are not supported. Add them first.")
            return
        self.exchange_rates[from_currency][to_currency] = rate
        print(f"Conversion rate from {from_currency} to {to_currency} set at {rate}.")

    def update_conversion_rate(self, from_currency, to_currency, new_rate):
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates[from_currency]:
            self.exchange_rates[from_currency][to_currency] = new_rate
            print(f"Updated conversion rate from {from_currency} to {to_currency} to {new_rate}.")
        else:
            print(f"No existing rate for {from_currency} to {to_currency}. Add it first.")

    def main_menu(self):
        while True:
            print("\nCurrency Converter Menu:")
            print("1. Display supported currencies")
            print("2. Convert currency")
            print("3. Add new currency")
            print("4. Add conversion rate")
            print("5. Update conversion rate")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_supported_currencies()
            elif choice == "2":
                self.handle_conversion()
            elif choice == "3":
                currency_code = input("Enter the new currency code (e.g., AUD): ").upper()
                self.add_currency(currency_code)
            elif choice == "4":
                from_currency = input("Enter the base currency: ").upper()
                to_currency = input("Enter the target currency: ").upper()
                rate = float(input("Enter the conversion rate: "))
                self.add_conversion_rate(from_currency, to_currency, rate)
            elif choice == "5":
                from_currency = input("Enter the base currency: ").upper()
                to_currency = input("Enter the target currency: ").upper()
                new_rate = float(input("Enter the new conversion rate: "))
                self.update_conversion_rate(from_currency, to_currency, new_rate)
            elif choice == "6":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def handle_conversion(self):
        from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., INR): ").upper()
        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
            result = self.convert_currency(from_currency, to_currency, amount)
            if result is not None:
                print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")


if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.main_menu()
