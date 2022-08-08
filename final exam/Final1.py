import pandas as pd
import matplotlib.pyplot as plt

# Read in csv file
YT = pd.read_csv("/Users/yangliu/Desktop/MBA-BUAN 446/BIS-346-446-liuyang/final exam/yellow_tripdata_2022-04.csv")

# Converting columns to more usable types

YT[['tpep_pickup_datetime','tpep_dropoff_datetime']].dtypes

YT['tpep_pickup_datetime'].head()

YT['pickup'] = pd.to_datetime(YT['tpep_pickup_datetime'],
                              infer_datetime_format=True)

YT['pickup'].head()

del YT['tpep_pickup_datetime']

YT['dropoff'] = pd.to_datetime(YT['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

del YT['tpep_dropoff_datetime']

YT['duration'] = YT['dropoff'] - YT['pickup']

YT[['pickup','dropoff','duration']].head()

# Deleting rows ("observations") that we don't want/need

YT['trip_distance'].describe()


YT['valid1'] = YT['trip_distance'] <= 100
YT['valid2'] = YT['passenger_count'] >= 1
YT['valid3'] = YT['trip_distance'] > 0
YT['valid4'] = YT['fare_amount'] < 1000
YT['valid5'] = YT['fare_amount'] > 0
YT['valid6'] = YT['extra'] >= 0

YT['valid'] = (YT['valid1'] & YT['valid2'] & YT['valid3'] & YT['valid4'] & YT['valid5'] & YT['valid6'])

YT['trip_distance'].describe()

YT = YT[YT.valid == True]

YT['trip_distance'].describe()

# Saving our altered data set

YT.to_csv('Yellow_Saved.csv', index = False)

# Read in csv file from first script
Yellow_Saved = pd.read_csv("Yellow_Saved.csv")

# Looking at dtypes
Yellow_Saved.dtypes

# pickup, dropoff, and duration were stored as strings!!!!
# Let's convert them back to datetimes
Yellow_Saved['pickup'] = pd.to_datetime(Yellow_Saved['pickup'],
                              infer_datetime_format=True)


Yellow_Saved['dropoff'] = pd.to_datetime(Yellow_Saved['dropoff'],
                              infer_datetime_format=True)

Yellow_Saved['duration'] = pd.to_datetime(Yellow_Saved['duration'],errors='coerce',
                              infer_datetime_format=True)


Yellow_Saved[['pickup','dropoff','duration']].head()

pd.set_option('display.float_format', lambda x: '%.2f' % x)

Yellow_Saved['trip_distance'].describe() #mean is 3.53

Yellow_Saved['duration'].describe()

Yellow_Saved['total_amount'].describe() #mean is 20.83

# Using plt.scatter with subplots
figs,subs = plt.subplots(2,sharex=True, sharey=True)
YT_1 = Yellow_Saved[Yellow_Saved.passenger_count == 1]
subs[0].scatter(YT_1['fare_amount'],YT_1['trip_distance'],
            color='red',marker='^',label='1')
YT_2 = Yellow_Saved[Yellow_Saved.passenger_count == 2]
subs[1].scatter(YT_2['fare_amount'],YT_2['trip_distance'],
            color='blue',marker='^',label='2')
plt.ylabel('fare_amount')
plt.xlabel('trip_distance')
plt.axis([-5,300,-1,60])
plt.title('Fare vs Distance by Passenger Count')
plt.figlegend(
    labels=('1 Passenger', '2 Passengers'),
    loc='upper right')
plt.show()
Yellow_Saved['durationtime_seconds'] = ( Yellow_Saved['dropoff'] - Yellow_Saved['pickup']).dt.total_seconds()
print('duration with minute unit',Yellow_Saved['durationtime_seconds'].mean()/60)
print('duration with hour unit',Yellow_Saved['durationtime_seconds'].mean()/(60*60))
print('duration with day unit',Yellow_Saved['durationtime_seconds'].mean()/(60*60*24))
