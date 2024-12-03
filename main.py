import tkinter as tk
from tkinter import ttk

def create_home_window():
    # Initialize the Home window
    home = tk.Tk()
    home.title("Hunter's Guide")
    home.geometry("400x300")
    
    # Labels
    tk.Label(home, text="Welcome to Hunter's Guide", font=("Arial", 16)).pack(pady=10)
    tk.Label(home, text="Choose an option below:", font=("Arial", 12)).pack(pady=5)
    
    # Buttons
    tk.Button(home, text="Season Schedules", command=create_schedule_window).pack(pady=5)
    tk.Button(home, text="Tracking Tips", command=lambda: print("Tracking Tips Placeholder")).pack(pady=5)
    tk.Button(home, text="Exit", command=home.destroy).pack(pady=5)
    
    home.mainloop()

def create_schedule_window():
    # Create the Season Schedules window
    schedule = tk.Toplevel()
    schedule.title("Season Schedules")
    schedule.geometry("400x300")
    
    tk.Label(schedule, text="Season Schedules", font=("Arial", 16)).pack(pady=10)
    tk.Label(schedule, text="(Filters and schedules will be displayed here)", font=("Arial", 12)).pack(pady=5)
    
    tk.Button(schedule, text="Back to Home", command=schedule.destroy).pack(pady=5)

# Run the application
if __name__ == "__main__":
    create_home_window()
