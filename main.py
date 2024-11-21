import sqlite3
import tkinter as tk
from tkinter import messagebox
from database import create_database, add_user, add_booking, get_booking_analysis, get_all_bookings
import matplotlib.pyplot as plt

class HallTicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hall Ticket Booking System")

        # User Registration
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()

        self.register_button = tk.Button(root, text="Register", command=self.register_user)
        self.register_button.pack()

        # Booking Section
        self.user_id_label = tk.Label(root, text="User  ID:")
        self.user_id_label.pack()
        self.user_id_entry = tk.Entry(root)
        self.user_id_entry.pack()

        self.event_label = tk.Label(root, text="Event Name:")
        self.event_label.pack()
        self.event_entry = tk.Entry(root)
        self.event_entry.pack()

        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()

        self.seats_label = tk.Label(root, text="Number of Seats:")
        self.seats_label.pack()
        self.seats_entry = tk.Entry(root)
        self.seats_entry.pack()

        self.book_button = tk.Button(root, text="Book Ticket", command=self.book_ticket)
        self.book_button.pack()

        self.analysis_button = tk.Button(root, text="Show Booking Analysis", command=self.show_analysis)
        self.analysis_button.pack()

        self.view_bookings_button = tk.Button(root, text="View All Bookings", command=self.view_bookings)
        self.view_bookings_button.pack()

    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        try:
            add_user(name, email)
            messagebox.showinfo("Success", "User  registered successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")

    def book_ticket(self):
        user_id = self.user_id_entry.get()  # Get user ID from input
        event_name = self.event_entry.get()
        date = self.date_entry.get()
        seats = int(self.seats_entry.get())
        
        try:
            add_booking(user_id, event_name, date, seats)
            messagebox.showinfo("Success", "Ticket booked successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_analysis(self):
        data = get_booking_analysis()
        events = [row[0] for row in data]
        seats = [row[1] for row in data]

        plt.bar(events, seats)
        plt.xlabel('Events')
        plt.ylabel('Total Seats Booked')
        plt.title('Booking Analysis')
        plt.show()

    def view_bookings(self):
        bookings = get_all_bookings()
        booking_details = "\n".join([f"Booking ID: {b[0]}, User ID: {b[1]}, Event: {b[2]}, Date: {b[3]}, Seats: {b[4]}" for b in bookings])
        messagebox.showinfo("All Bookings", booking_details)

if __name__ == "__main__":
    create_database()  # Create the database and tables
    root = tk.Tk()
    app = HallTicketBookingApp(root)
    root.mainloop()