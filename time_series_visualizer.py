import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.set_index('date')

# Clean data
df = df.drop(df[(df['value'] < df['value'].quantile(0.025)) | (df['value'] > df['value'].quantile(0.975))].index)

def draw_line_plot():
    # Draw line plot
    plt.plot(df['value'], color='red', linewidth= .8)
  
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Data')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return
  
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar['Year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack()
    month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  
    # Draw bar plot
    df_bar.plot(kind='bar', figsize=(15,10))

    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    legend = plt.legend(title='Months', fontsize=15, labels=month_names)
    title = legend.get_title()
    title.set_fontsize(15)

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return 

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Month'] = pd.DatetimeIndex(df_box.index).month
    df_box['Year'] = pd.DatetimeIndex(df_box.index).year

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(15,6))
  
    sns.boxplot(x='Year', y='value', data=df_box, ax=ax[0])
    ax[0].set_title('Year-wise Box Plot')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    sns.boxplot(x='Month', y='value', data=df_box, ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Trend)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
  
    # Save image and return fig (don't change this part)
    plt.savefig('box_plot.png')
    return
