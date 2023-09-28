import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  """Creates a scatter plot of sea level data with two lines of best fit.

  Returns:
    The plot object.
  """

  # Read data from file
  data = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], edgecolors='g')

  # Create line of best fit for entire dataset
  slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
  plt.plot(data['Year'], intercept + slope * data['Year'], 'k')

  # Create line of best fit for data from year 2000 onwards
  slope, intercept, r_value, p_value, std_err = linregress(data['Year'][data['Year'] >= 2000], data['CSIRO Adjusted Sea Level'][data['Year'] >= 2000])
  plt.plot(data['Year'][data['Year'] >= 2000], intercept + slope * data['Year'][data['Year'] >= 2000], 'b')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Draw lines of best fit through year 2050
  plt.plot([1880, 2050], [intercept, intercept + slope * 2050], 'k')
  plt.plot([2000, 2050], [intercept, intercept + slope * 2050], 'b')

  return plt.gca()

# Draw plot and save it as a PNG image
plot = draw_plot()
plt.savefig('sea_level_plot.png')
