import random
N_total = int(input("Enter the total amount of points: "))
count = 0
n_inside = 0
pi = 0.0

while count < N_total:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x*x + y*y) < 1:
        n_inside += 1
        count = count + 1
    else:
        count = count + 1

pi = (4 * n_inside) / N_total
print(f"The estimate of pi is: ")
print(pi)
