import tkinter as tk
from tkinter import messagebox

class CookiequeMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Cookieque Menu")
        self.root.geometry("400x600")

        # Set pastel background color for root
        self.root.configure(bg="#FFF5EE")  # Cream

        # Menu items
        self.menu_items = {
            "Chocolate Cookie": 3500,
            "Peanut Cookie": 4000,
            "Minty Cookie": 4500,
            "Berry Cookie": 5000,
            "Tropical Cookie": 5500
        }

        # Cart dictionary
        self.cart = {}

        # Initialize order queue number
        self.queue_number = 1

        # Title
        tk.Label(
            root,
            text="Cookieque Menu",
            font=("Helvetica", 18, "bold"),
            bg="#FFF5EE",  # Cream
            fg="#FFB6C1"  # Pink
        ).pack(pady=10)

        # Menu selection label
        tk.Label(
            root,
            text="Select Variant:",
            font=("Helvetica", 14),
            bg="#FFF5EE",  # Cream
            fg="#000000"  # Peach
        ).pack(anchor="w", padx=20)

        # Checkbox variables for menu items
        self.item_vars = {}
        for item, price in self.menu_items.items():
            var = tk.IntVar()
            tk.Checkbutton(
                root,
                text=f"{item} - Rp {price:,}",
                variable=var,
                font=("Helvetica", 12),
                bg="#FFF5EE",  # Cream
                fg="#000000",  # Pink
                activebackground="#FFF5EE",  # Peach
                activeforeground="#98FB98"  # Green pastel
            ).pack(anchor="w", padx=30)
            self.item_vars[item] = var

        # Add to cart button
        tk.Button(
            root,
            text="Add to Cart",
            command=self.add_to_cart,
            bg="#FFB6C1",  # Pink
            fg="#FFF5EE",  # Cream
            font=("Helvetica", 12)
        ).pack(pady=10)

        # Cart display
        self.cart_text = tk.Text(
            root,
            height=10,
            width=40,
            state="disabled",
            bg="#FFFFFF",  # Peach
            fg="#000000"   # Cream
        )
        self.cart_text.pack(pady=10)

        # Total label
        self.total_label = tk.Label(
            root,
            text="Total: Rp 0",
            font=("Helvetica", 14),
            bg="#FFF5EE",  # Cream
            fg="#000000"  # Green pastel
        )
        self.total_label.pack(pady=5)

        # Place order button
        tk.Button(
            root,
            text="Place Order",
            command=self.place_order,
            bg="#98FB98",  # Green pastel
            fg="#FFF5EE",  # Cream
            font=("Helvetica", 12)
        ).pack(pady=10)

    def add_to_cart(self):
        # Track if any item was added
        item_added = False

        # Add selected items to cart
        for item, var in self.item_vars.items():
            if var.get() == 1:
                item_added = True  # Mark that an item was added
                if item in self.cart:
                    self.cart[item] += self.menu_items[item]
                else:
                    self.cart[item] = self.menu_items[item]
                var.set(0)  # Reset checkbox

        # If no items were selected, show a warning
        if not item_added:
            messagebox.showwarning("No Items Selected", "Please select at least one item before adding to the cart.")
            return

        self.update_cart()

    def update_cart(self):
        # Update cart display
        self.cart_text.configure(state="normal")
        self.cart_text.delete(1.0, "end")

        total = 0
        for item, price in self.cart.items():
            count = price // self.menu_items[item]
            self.cart_text.insert("end", f"{item} (x{count}): Rp {price:,}\n")
            total += price

        self.cart_text.configure(state="disabled")
        self.total_label.config(text=f"Total: Rp {total:,}")

    def place_order(self):
        # Ensure cart is not empty
        if not self.cart:
            messagebox.showwarning("Cart Empty", "Please add items to the cart before placing an order.")
            return

        # Order details
        order_details = "\n".join(
            [f"{item} (x{price // self.menu_items[item]}): Rp {price:,}" for item, price in self.cart.items()]
        )
        total = sum(self.cart.values())

        # Display order summary with queue number
        messagebox.showinfo(
            "Order Placed",
            f"Order Number: #{self.queue_number}\n\nYour order:\n\n{order_details}\n\nTotal: Rp {total:,}\n\nThank you!"
        )

        # Increment queue number
        self.queue_number += 1

        # Clear cart after placing order
        self.cart.clear()
        self.update_cart()


if __name__ == "__main__":
    root = tk.Tk()
    app = CookiequeMenu(root)
    root.mainloop()
