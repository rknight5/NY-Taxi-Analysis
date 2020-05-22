#Importing the necessary libraries 

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
%matplotlib inline

#Importing the datafiles for the analysis

data_filename = ('nyc_data.csv')
data_filename2 = ('nyc_fare.csv')

data = pd.read_csv(data_filename, 
                   parse_dates=['pickup_datetime', 'dropoff_datetime'] )

data2 = pd.read_csv(data_filename2)
#pd.read_csv?

#Viewing the first few rows of the nyc_data data set
data.head()

#Viewing the first few rows of the nyc_fares data set
data2.head()

#Identifying the data types of all the variables 
data.dtypes

#The number of rows
rownum = len(data.axes[0])
print("Number of Rows: "+str(rownum))

#The number of columns
colnum = len(data.axes[1])
print("Number of Columns: "+str(colnum))

#Calculating summary statistics
summary = data.describe()

#Transposing statistics
summary = summary.transpose()

#Visualizing summary statistics in console 
summary.head()

#categorical variable frequencies 
print (data['vendor_id'].value_counts())

print (data['store_and_fwd_flag'].value_counts())

Get the actual coordinates: four DataFrame columns
These four variables are all Series objects:

p_lng = data.pickup_longitude
p_lat = data.pickup_latitude
d_lng = data.dropoff_longitude
d_lat = data.dropoff_latitude

# a Series is an indexed list of values.
p_lng.head()

# Getting the coordinates of points in pixels from geographical coordinates.
def lat_lng_to_pixels(lat, lng):
    lat_rad = lat * np.pi / 180.0
    lat_rad = np.log(np.tan((lat_rad + np.pi / 2.0) / 2.0))
    x = 100 * (lng + 180.0) / 360.0
    y = 100 * (lat_rad - np.pi) / (2.0 * np.pi)
    return (x, y)

# Getting pickup coordinates from pickup latitude and longitude
px, py = lat_lng_to_pixels(p_lat, p_lng)
py.head()

#Displaying a scatter plot of pickup locations
plt.scatter(px, py)

plot2 = data[data['vendor_id'] == 'CMT'].plot(x='pickup_longitude', y='pickup_latitude',kind='line',marker='.',linestyle='None',label='CMT',color='yellow')
        
data[data['vendor_id'] == 'VTS'].plot(x='pickup_longitude', y='pickup_latitude',kind='line',marker='.',linestyle='None',label='VTS',color='purple',ax=plot2)

### Customize our plot:
- Make markers smaller
- Make fewer points by making some points transparent
- Zoom in around Manhattan
- Make figure bigger
- Don't display the axes

# Specify the figure size
plt.figure(figsize=(8, 6))
# s argument is used to make the marker size smaller
# alpha specifies opacity
plt.scatter(px, py, s=.1, alpha=0.03)
# equal aspect ratio
plt.axis('equal')
# zoom in
plt.xlim(29.40, 29.55)
plt.ylim(-37.63, -37.54)
# remove the axes
plt.axis('off')

#Finding the frequency counts for all the vendors that have made pickups
vendor = data['vendor_id'].value_counts()

#Finding the vendor with the highest frequency = most pickups
vendor.nlargest(1)

## Display a histogram of the trip distances.
Manhattan Island is 13.4 miles long and 2.3 miles wide.

bin_array = np.linspace(start=0., stop=10., num=100)
bin_array

data.trip_distance.hist(bins=bin_array)

#Trip ride with the highest frequency
print (np.bincount(data.trip_distance).argmax())

print (data.trip_distance.value_counts().nlargest(1))

from collections import Counter 

def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0] 

print(most_frequent(data.trip_distance))

#plotting a fares histogram using the bins array
data2.total_amount.hist(bins=bin_array)

#Rides with fares in the range of $6-$10 stay pretty consistent with each other
#Inference is that most rides within NYC cost within that range
#Passengers tend to ride longer distances on average based on fares


## Filtering with boolean indexing
### Select long rides

a = data.loc[data.trip_distance > 100]
len(a)

data.loc[data.trip_distance > 100]

a.head()

#End

