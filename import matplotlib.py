import matplotlib.pyplot as plt
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(sort_function, data_size):
    data = generate_random_array(data_size)
    start_time = time.time()
    sort_function(data)
    end_time = time.time()
    return end_time - start_time

# اجرای مرتب‌سازی حبابی برای اندازه‌های مختلف
data_sizes = list(range(10, 1001, 50))
execution_times = []

for size in data_sizes:
    time_taken = measure_time(bubble_sort, size)
    execution_times.append(time_taken)

# نمایش نمودار
plt.plot(data_sizes, execution_times, marker='o')
plt.title('زمان اجرای مرتب‌سازی حبابی بر اساس اندازه داده')
plt.xlabel('اندازه داده')
plt.ylabel('زمان اجرا (ثانیه)')
plt.grid(True)
plt.show()
