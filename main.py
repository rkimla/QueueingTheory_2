from visualization import plot_characteristics

# Queue model parameters
arrival_rate = 0.5  # customers per unit time
service_rate = 1.0  # services per unit time
N = 5  # Threshold for N-policy
max_time = 1000  # Total simulation time

# Plotting the characteristics
plot_characteristics(arrival_rate, service_rate, N, max_time)