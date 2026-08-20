import pandas as pd
import numpy as np
from scipy.integrate import simpson
import matplotlib.pyplot as plt

#Loading the data
df = pd.read_csv("dolphin_telemetry.csv")

#Clasifying the data
df["Behaviour"] = np.where((df["Velocity_(m/s)"] > 4.0) & (abs(df["Acceleration_(m/s^2)"]) < 0.5), "Bow-riding", "Free-swim")
#Calculating the mean effort
dt = df["Time_(s)"].iloc[1] - df["Time_(s)"].iloc[0]
bw_a = abs(df.loc[df["Behaviour"] == "Bow-riding", "Acceleration_(m/s^2)"])
fs_a = abs(df.loc[df["Behaviour"] == "Free-swim", "Acceleration_(m/s^2)"])

bw_mean_effort = simpson(y=bw_a, dx=dt)/(len(bw_a)*dt)
fs_mean_effort = simpson(y=fs_a, dx=dt)/(len(fs_a)*dt)

print(f"The mean effort in Free Swim is {fs_mean_effort:.2f}m/s^2")
print(f"The mean effort in Bow-riding is {bw_mean_effort:.2f}m/s^2")

#PLotting the points
plt.figure(figsize=(12,6))
plt.scatter(
	df.loc[df["Behaviour"] == "Free-swim", "Time_(s)"],
	df.loc[df["Behaviour"] == "Free-swim", "Velocity_(m/s)"],
	color='royalblue', 
    label='Free-swim', 
    alpha=0.6, 
    s=15
	)
plt.scatter(
	df.loc[df["Behaviour"] == "Bow-riding", "Time_(s)"],
	df.loc[df["Behaviour"] == "Bow-riding", "Velocity_(m/s)"],
	color='crimson', 
    label='Bow-riding', 
    alpha=0.6, 
    s=15
	)

plt.axhline(4.0, color='black', linestyle='--', linewidth=1, label='Limit (4.0 m/s)')
plt.title('Velocity Profile', fontsize=13)
plt.xlabel('Time (s)', fontsize=11)
plt.ylabel('Velocity (m/s)', fontsize=11)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right', frameon=True)

plt.tight_layout()
plt.show()