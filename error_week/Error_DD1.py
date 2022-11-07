g = 9.81
t = np.linspace(0, 10, num=11)
s = 1/2 * g * t ** 2
print(f"At time {t[0]} s, the apple fell {s[0]} m.")
print(f"At time {t[3]} s, the apple fell {s[3]} m.")