# Imports the required package
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Pd.read_csv function will read csv file and perform operations.
filetoread = pd.read_csv("boardmeetingnew.csv")

# Initialises the data for the x,y coordinates
averagex = filetoread["Age"]
averagey = filetoread["Salary"]

# Zip/sorted function will plot points in ascending order
averagex, averagey = zip(*sorted(zip(averagex, averagey)))

heading = plt.ylabel("Salary (GBP)")
labelingX = plt.xlabel("Age of Workers")
labelingY = plt.title("Average/Median Salary According to Age.")

# These lines will plt the figures and plot the result
plt.plot(averagex, averagey,)
plt.show()