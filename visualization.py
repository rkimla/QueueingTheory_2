import matplotlib.pyplot as plt


def plot_characteristics(arrival_rate, service_rate, N, max_time):
    from model import simulate_queue

    events, average_waiting_time = simulate_queue(arrival_rate, service_rate, N, max_time)

    times, queue_lengths = zip(*events)
    plt.plot(times, queue_lengths)
    plt.xlabel('Time')
    plt.ylabel('Queue Length')
    plt.title('Queue Length Over Time')

    # Display average waiting time
    annotation_text = f"Average Waiting Time: {average_waiting_time:.2f} units"
    plt.annotate(annotation_text, xy=(0.5, 0.05), xycoords='axes fraction', ha='center', va='center',
                 bbox=dict(boxstyle="round,pad=0.5", fc="yellow", ec="black", lw=2))

    plt.show()
