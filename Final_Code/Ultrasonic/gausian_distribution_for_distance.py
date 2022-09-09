import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
import numpy as np
import math
from scipy.stats import norm

# ============== Files ======================

files = ['D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\2cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\10cm_0degree.csv',
         'D:\\Research\\Swarm-Robot-USS-2022\\Attempt\\Data\\Ultrasonic\\angle_of_object\\0degree_v2\\20cm_0degree.csv',
         ]

if __name__=="__main__":
    rightSize = 20
    numSize = 19
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    # ==================== Plotting =================
    fig, ax = plt.subplots()
    binwidth = 0.1
    df = pd.read_csv(files[0])
    ax.hist((df['x']), density=False, bins=np.arange(0, 25,binwidth), lw=0, color='blue')
    ax.set_xlabel("Distance (cm)", fontsize=rightSize)
    ax.set_ylabel("Number of Samples", color='blue', fontsize=rightSize)

    # Plot the Normal Distribution Curve
    ax2 = ax.twinx()
    mean = (df['x']).mean()
    std = (df['x']).std()
    x_axis = np.arange(0,25,0.01)
    ax2.plot(x_axis, norm.pdf(x_axis, mean, std),color='orange')
    ax2.grid(False)
    ax2.set_ylabel("Probability Density", color='orange', fontsize=rightSize)


    # Align 2 axis
    ax_ylims = ax.axes.get_ylim()  # Find y-axis limits set by the plotter
    ax_yratio = ax_ylims[0] / ax_ylims[1]  # Calculate ratio of lowest limit to highest limit

    ax2_ylims = ax2.axes.get_ylim()  # Find y-axis limits set by the plotter
    ax2_yratio = ax2_ylims[0] / ax2_ylims[1]  # Calculate ratio of lowest limit to highest limit

    if ax_yratio < ax2_yratio:
        ax2.set_ylim(bottom=ax2_ylims[1] * ax_yratio)
    else:
        ax.set_ylim(bottom=ax_ylims[1] * ax2_yratio)

    ax.tick_params(axis='both', which='major', labelsize=numSize)
    ax2.tick_params(axis='both', which='major', labelsize=numSize)

    plt.title("Histogram with Gaussian Fit for 2cm Distance Object", fontsize=rightSize, fontweight="bold")
    plt.xticks(np.arange(0,25,5))
    plt.tight_layout()
    plt.show()

