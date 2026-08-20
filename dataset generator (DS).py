import pandas as pd
import numpy as np


np.random.seed(42)
seconds = np.arange(0, 3600)
velocity = np.abs(np.random.normal(2.0, 1.0, 3600))
acceleration = np.random.normal(0, 1.5, 3600)

velocity[600:900] = np.random.normal(5.5, 0.3, 300)
acceleration[600:900] = np.random.normal(0, 0.1, 300) 

velocity[2400:2880] = np.random.normal(6.0, 0.2, 480)
acceleration[2400:2880] = np.random.normal(0, 0.15, 480)

velocity = np.clip(velocity, 0, None)

df_biometrics = pd.DataFrame({
    'Time_(s)': seconds,
    'Velocity_(m/s)': velocity,
    'Acceleration_(m/s^2)': acceleration
})

df_biometrics.to_csv('dolphin_telemetry.csv', index=False)
print(f"Dataset generated with {len(df_biometrics)} registrations.")