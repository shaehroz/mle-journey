import numpy as np

x = np.array([2, 4, 6, 8, 10])

print(np.mean(x))
print(np.var(x))
print(np.std(x))

mean_x = np.mean(x)

by_hand_mean = np.sum(x) / len(x)

print(by_hand_mean)


by_hand_var = np.mean(x ** 2) - np.mean(x) ** 2


var_def = np.mean((x - mean_x) ** 2)


std = np.var(x , ddof=1)
print(std)

rng = np.random.default_rng(0)
true_var = 4.0   # draws from Normal(0, sd=2)

n_vals = []
d0 = []
d1 = []
for _ in range(100000):
    s = rng.normal(0, 2, size=5)
    d0.append(np.var(s))
    d1.append(np.var(s, ddof=1))

print("True:    " + str(true_var))
print("ddof=0:  " + str(np.mean(d0)))
print("ddof=1:  " + str(np.mean(d1)))