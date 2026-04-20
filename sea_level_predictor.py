import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', alpha=0.5)

    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    years_extended = pd.Series([i for i in range(1880, 2051)])
    
    plt.plot(years_extended, reg1.slope * years_extended + reg1.intercept, 'r', label='Best Fit Line 1')

    df_recent = df[df['Year'] >= 2000]
    reg2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    years_recent = pd.Series([i for i in range(2000, 2051)])
    
    plt.plot(years_recent, reg2.slope * years_recent + reg2.intercept, 'green', label='Best Fit Line 2')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
