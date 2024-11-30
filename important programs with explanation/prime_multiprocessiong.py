import multiprocessing

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_prime_range(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes

if __name__ == '__main__':
    # Defining the range of numbers to check for primes
    start = 1
    end = 1000
    num_processes = 4
    pool = multiprocessing.Pool(processes=num_processes)
    
    # Splitting the range of numbers across multiple processes
    ranges = [(start + i * (end // num_processes), start + (i + 1) * (end // num_processes)) for i in range(num_processes)]
    
    # Getting results from different processes
    results = pool.starmap(check_prime_range, ranges)
    
    # Merging all results
    primes = [prime for result in results for prime in result]
    print("Primes:", primes)


"""
ranges = [(start + i * (end // num_processes), start + (i + 1) * (end // num_processes)) for i in range(num_processes)]
Purpose of the Line:
This line is creating sub-ranges of numbers that will be assigned to different processes. We have a big range of numbers (from start to end), and we want to split this range into smaller chunks, so each process can work on a smaller part of the whole range.

Parts of the Expression:
num_processes:
This is the number of processes we want to create. In the previous example, num_processes was set to 4, meaning we want to split the range into 4 chunks.

end // num_processes:
This is integer division. It divides the entire range into smaller parts. For example:

If end = 1000 and num_processes = 4, then end // num_processes = 1000 // 4 = 250.
This means that each process will handle 250 numbers.

start + i * (end // num_processes):
This expression calculates the starting number for each process’s range.

i is the index of the process (it starts from 0 and goes up to 3 because range(num_processes) gives us values [0, 1, 2, 3] for i).
For each process i, we calculate the start like this:

For i = 0:
start + 0 * 250 = start = 1
For i = 1:
start + 1 * 250 = start + 250 = 251
For i = 2:
start + 2 * 250 = start + 500 = 501
For i = 3:
start + 3 * 250 = start + 750 = 751
start + (i + 1) * (end // num_processes):
This expression calculates the ending number for each process's range.

It shifts the start point forward by 1 range to get the endpoint:

For i = 0:
start + (0 + 1) * 250 = start + 250 = 251
For i = 1:
start + (1 + 1) * 250 = start + 500 = 501
For i = 2:
start + (2 + 1) * 250 = start + 750 = 751
For i = 3:
start + (3 + 1) * 250 = start + 1000 = 1001 (but note that range in Python is exclusive, so 1001 isn’t included).
Final Breakdown of Ranges:
The list comprehension [(start + i * (end // num_processes), start + (i + 1) * (end // num_processes)) for i in range(num_processes)] creates a list of tuples, where each tuple contains a start and end for the range of numbers to check for each process.

For example:

When i = 0:
The range is (1, 251)
(this means the first process will check numbers from 1 to 250).

When i = 1:
The range is (251, 501)
(this means the second process will check numbers from 251 to 500).

When i = 2:
The range is (501, 751)
(this means the third process will check numbers from 501 to 750).

When i = 3:
The range is (751, 1001)
(this means the fourth process will check numbers from 751 to 1000).

The Result of the Expression:
The result of this list comprehension is a list of ranges that looks like this:

ranges = [(1, 251), (251, 501), (501, 751), (751, 1001)]
This means we have 4 ranges that will be handled by 4 processes:

Process 1 will check numbers from 1 to 250.
Process 2 will check numbers from 251 to 500.
Process 3 will check numbers from 501 to 750.
Process 4 will check numbers from 751 to 1000.
Each process will now work independently on its part of the range, speeding up the overall calculation by running in parallel.










results = pool.starmap(check_prime_range, ranges)
This line is key to running your multiprocessing task efficiently. It distributes the prime-checking function across multiple processes to speed up computation. Lets go over each part of this line in detail.

1. Multiprocessing and the pool object
The pool object is created from Python's multiprocessing module:


pool = multiprocessing.Pool(processes=num_processes)
multiprocessing.Pool(): This creates a "pool" of worker processes (separate Python processes) to run tasks in parallel.
num_processes: Defines the number of worker processes. In your example, this is set to 4, meaning 4 separate processes will be running in parallel.
Benefit: By using multiprocessing, the program can split the work and perform it faster by taking advantage of multiple CPU cores.
2. pool.starmap()
starmap() is a method from the multiprocessing library that allows parallel execution of a function across multiple input sets (or "arguments"). Here's how it works:

starmap(): This function is used to apply a given function (check_prime_range in your case) to each pair of arguments provided in ranges. It distributes the work across the processes in the pool.
Key feature: starmap takes multiple arguments as input for the function it is calling (in this case, check_prime_range). Each argument pair is passed to the function.










primes = [prime for result in results for prime in result]
This is a list comprehension used to flatten a list of lists. It extracts all the prime numbers from the results, which is a list containing smaller lists of prime numbers from each process. Let’s go step by step:

The Purpose:
We want to combine (or "flatten") all the individual lists of prime numbers that each process returns into a single list of prime numbers.
Understanding Variables:
results:
This is a list of lists. Each element of results is a list of prime numbers found by one process.
For example, results might look like this:


results = [[2, 3, 5, 7, 11, 13, 17], [19, 23, 29, 31, 37], [41, 43, 47], ... ]
Each small list inside results contains prime numbers from a specific range (handled by each process).

prime:
This is a single prime number from one of the lists in results.

Explanation of the List Comprehension:
1. Outer Loop (for result in results):
This part iterates over each small list in results.
result represents each small list of prime numbers.
Example: In the first iteration, result could be [2, 3, 5, 7, 11, 13, 17].
2. Inner Loop (for prime in result):
For every result (which is a list), this inner loop iterates over each prime number in that list.
Example: For the first result = [2, 3, 5, 7, 11, 13, 17], the loop will iterate over 2, then 3, then 5, and so on.
3. Combining the Results:
Each prime found by the inner loop is added to the final primes list.
This flattens the nested lists of primes from results into a single list of prime numbers.
Example Breakdown:
Let’s say results is:

results = [[2, 3, 5], [7, 11], [13, 17, 19]]
The list comprehension works like this:

First Iteration (result = [2, 3, 5]):

The inner loop runs for each prime in this result list:
prime = 2: Add 2 to the primes list.
prime = 3: Add 3 to the primes list.
prime = 5: Add 5 to the primes list.
Second Iteration (result = [7, 11]):

The inner loop runs for each prime in this result list:
prime = 7: Add 7 to the primes list.
prime = 11: Add 11 to the primes list.
Third Iteration (result = [13, 17, 19]):

The inner loop runs for each prime in this result list:
prime = 13: Add 13 to the primes list.
prime = 17: Add 17 to the primes list.
prime = 19: Add 19 to the primes list.
After combining all the primes from each list, the final primes list will be:

primes = [2, 3, 5, 7, 11, 13, 17, 19]
Why This Is Done:
The reason for this two-level iteration (for result in results and for prime in result) is that results is a list of lists, so we need to:

Access each small list of primes (using for result in results).
Extract each prime from those small lists (using for prime in result).
Finally, all the extracted primes are combined into a single list called primes.


"""