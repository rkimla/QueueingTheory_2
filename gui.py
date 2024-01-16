from model import simulate_queue
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Function to update plot and statistics
def update_simulation():
    # Read values from entries
    arrival_rate = float(arrival_entry.get())
    service_rate = float(service_entry.get())
    N = int(n_entry.get())
    max_time = int(time_entry.get())

    # Run simulation
    events, avg_waiting_time = simulate_queue(arrival_rate, service_rate, N, max_time)

    # Update plot
    times, queue_lengths = zip(*events)
    ax.clear()
    ax.plot(times, queue_lengths)
    ax.set_xlabel('Time')
    ax.set_ylabel('Queue Length')
    ax.set_title('Queue Length Over Time')
    canvas.draw()

    # Update average waiting time
    avg_time_label.config(text=f"Average Waiting Time: {avg_waiting_time:.2f} units")

# Initialize main window
root = tk.Tk()
root.title("Queue Model Analysis")

# Input fields for parameters
arrival_label = ttk.Label(root, text="Arrival Rate:")
arrival_label.pack()
arrival_entry = ttk.Entry(root)
arrival_entry.pack()

service_label = ttk.Label(root, text="Service Rate:")
service_label.pack()
service_entry = ttk.Entry(root)
service_entry.pack()

n_label = ttk.Label(root, text="N Value:")
n_label.pack()
n_entry = ttk.Entry(root)
n_entry.pack()

time_label = ttk.Label(root, text="Total Time:")
time_label.pack()
time_entry = ttk.Entry(root)
time_entry.pack()

# Button to run simulation
run_button = ttk.Button(root, text="Run Simulation", command=update_simulation)
run_button.pack()

# Label for average waiting time
avg_time_label = ttk.Label(root, text="Average Waiting Time: ")
avg_time_label.pack()

# Plot area
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

root.mainloop()