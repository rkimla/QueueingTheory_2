import numpy as np


def simulate_queue(arrival_rate, service_rate, N, max_time):
    current_time = 0
    queue_length = 0
    events = []
    waiting_times = []

    next_arrival_time = np.random.exponential(1 / arrival_rate)

    while current_time < max_time:
        if queue_length < N:
            current_time += next_arrival_time
            queue_length += 1
            next_arrival_time = np.random.exponential(1 / arrival_rate)
        else:
            service_time = np.random.exponential(1 / service_rate)
            current_time += service_time
            waiting_times.append(service_time)
            queue_length = max(queue_length - 1, 0)

        events.append((current_time, queue_length))

    average_waiting_time = np.mean(waiting_times) if waiting_times else 0
    return events, average_waiting_time
