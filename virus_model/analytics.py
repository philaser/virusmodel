import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

class LinePlot:

    def __init__(self, graph):
        self.dataframe = graph.data
        self.ax = None

    def plot(self):
        print(self.dataframe)
        self.ax = sns.lineplot(x = 'Day', y = 'Infected', data = self.dataframe)
        plt.show()

    def show(self):
        plt.show()

