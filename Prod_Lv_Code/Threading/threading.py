'''Threading is a feature in Python that allows a program to run multiple operations concurrently within the same process.
Think of a process as a single running application (like your web browser). Threads are independent sub-tasks running inside that application 
(like one thread downloading a file while another thread renders the webpage UI). By breaking a program into multiple threads, tasks can run side-by-side instead of waiting for each other to finish.'''


import threading
import time

def cook_pasta():
    print("Starting pasta...")
    time.sleep(4)  # Simulates waiting 4 seconds for water to boil
    print("Pasta is ready!")

def make_sauce():
    print("Starting sauce...")
    time.sleep(2)  # Simulates simmering sauce for 2 seconds
    print("Sauce is ready!")

# 1. Create the threads and assign them tasks
thread1 = threading.Thread(target=cook_pasta)
thread2 = threading.Thread(target=make_sauce)

start_time = time.time()

# 2. Start both threads concurrently
thread1.start()
thread2.start()

# 3. Wait for both threads to finish before moving forward in the main script
thread1.join()
thread2.join()

end_time = time.time()
print(f"Dinner served in {end_time - start_time:.2f} seconds!")
