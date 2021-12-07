import numpy as np
import pandas as pd

path = "https://github.com/SparrowOP/sample.project/blob/main/CSV/in.csv"
df = pd.read_csv(path, skiprows=1, header=None)
vol = df.to_numpy()
mean = vol.mean()
median = np.median(vol)
sd = vol.std()
print("The Median of the Volumes is :", median)
print("The Mean of the Volumes is :", mean)
print("The Standard Deviation of the Volumes is :", sd)
