import numpy as np
import matplotlib.pyplot as plt
np.random.seed(10)
data = np.random.normal(50, 10, 1000)
mean_value = np.mean(data); std_value = np.std(data)
plt.hist(data, bins=30, density=True, alpha=0.6, edgecolor="black")
x = np.linspace(min(data), max(data), 300)
y = (1 / (std_value * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_value) / std_value) ** 2)
plt.plot(x, y); plt.axvline(mean_value, linestyle="--", label="Mean")
plt.xlabel("Value"); plt.ylabel("Density"); plt.title("Normal Distribution"); plt.legend(); plt.show()
for n in (1, 2, 3):
    count = np.sum((data >= mean_value - n * std_value) & (data <= mean_value + n * std_value))
    print(n, "standard deviations:", count, "values")
