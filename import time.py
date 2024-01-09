import time
import random
import matplotlib.pyplot as plt

def algorithm_to_measure(data):
    people = [
    {'first_name': 'Raj', 'last_name': 'Nayyar'},
    {'first_name': 'Suraj', 'last_name': 'Sharma'},
    {'first_name': 'Karan', 'last_name': 'Kumar'},
    {'first_name': 'Jade', 'last_name': 'Canary'},
    {'first_name': 'Raj', 'last_name': 'Thakur'},
    {'first_name': 'Raj', 'last_name': 'Sharma'},
    {'first_name': 'Kiran', 'last_name': 'Kamla'},
    {'first_name': 'Armaan', 'last_name': 'Kumar'},
    {'first_name': 'Jaya', 'last_name': 'Sharma'},
    {'first_name': 'Ingrid', 'last_name': 'Galore'},
    {'first_name': 'Jaya', 'last_name': 'Seth'},
    {'first_name': 'Armaan', 'last_name': 'Dadra'},
    {'first_name': 'Ingrid', 'last_name': 'Maverick'},
    {'first_name': 'Aahana', 'last_name': 'Arora'},
]
sorted_people = sorted(people, key=lambda x: (x['first_name'], x['last_name']))
for person in sorted_people:
      print(f"{person['first_name']} {person['last_name']}")
      
sorted_data = sorted(data)


def measure_execution_time(data_size):
    # ایجاد داده‌های تصادفی
    data = [random.randint(1, 1000) for _ in range(data_size)]

    # ثبت زمان شروع
    start_time = time.time()

    # فراخوانی الگوریتم
    result = algorithm_to_measure(data)

    # ثبت زمان پایان
    end_time = time.time()

    # محاسبه زمان اجرا
    execution_time = end_time - start_time

    return execution_time

def main():
    data_sizes = [10, 100, 500, 1000, 2000]  # اندازه‌های مختلف داده
    execution_times = []

    for size in data_sizes:
        time_taken = measure_execution_time(size)
        execution_times.append(time_taken)
        print(f"Data size: {size}, Execution time: {time_taken} seconds")

    # رسم نمودار
    plt.plot(data_sizes, execution_times, marker='o')
    plt.title('Execution Time of the Algorithm')
    plt.xlabel('Data Size')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

if __name__ == "__main__":
    main()