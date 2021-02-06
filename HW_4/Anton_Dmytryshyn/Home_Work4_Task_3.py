fibonacci_previous_number = 0
fibonacci_next_number = 1
i = 0

n = int(input("I will print fibonaccis number not more than "))

while i < n and fibonacci_previous_number <= n:
    print(fibonacci_previous_number)
    fibonacci_number = fibonacci_previous_number + fibonacci_next_number
    fibonacci_previous_number = fibonacci_next_number
    fibonacci_next_number = fibonacci_number
    i += 1

    




