from re import S
import plotly.figure_factory as px
import plotly.graph_objects as gx
import pandas as pd
import statistics
import random

list = pd.read_csv('medium_data.csv')
reading_time = list["reading_time"].tolist()

def random_set(counter):
    data = []
    for i in range(0,counter):
        index = random.randint(0,len(reading_time)-1)
        value = reading_time[index]
        data.append(value)
    mean = statistics.mean(data)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = px.create_distplot([df], ["reading_time"], show_hist=False)
   #fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    for i in range(1000):
            list = []
    for i in range(1000):
        sample = random_set(100)
        list.append(sample)       
    show_fig(list)
    mean = statistics.mean(list)
    standard_deviation = statistics.stdev(list)
    print("Mean of Sample: ",mean)
    print("Mean of Sample: ",standard_deviation)

Main_mean = statistics.mean(reading_time)
Main_deviation = statistics.stdev(reading_time)
print("Population Mean: ",Main_mean)
print("Population Deviation: ",Main_deviation)

if __name__ == '__main__':
    setup()