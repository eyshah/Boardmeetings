# Imports the required packages
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Pd.read_csv function will read csv file and perform operations.
readcsvfile = pd.read_csv("boardmeetingnew.csv")

# Initialises the data for the x,y coordinates -mode() returns mode in dataset
getthemodesalaryX = readcsvfile["Salary"].mode()
getthemodesalaryY = readcsvfile["Age"].mode()

# Labeling the axis/graph title
labely = plt.ylabel("Salary (GBP)")
labelx = plt.xlabel("Age of Workers")
Heading = plt.title("Mode Salary According to Age.")

# These lines will plot the figures and show result
plt.plot(getthemodesalaryX, getthemodesalaryY)
plt.show()


