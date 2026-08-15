"""
Feature engineering
Feature engineering is the process of creating useful input variables from raw data.
"""

# Next topic: Time-Based Feature Engineering

import pandas as pd 

sensor_data = pd.read_csv("D:/AI_Learning/day4_pandas/cleaned_sensor_data.csv")
sensor_data["timestamp"]=pd.to_datetime(sensor_data["timestamp"])
print("Original Data :")
print(sensor_data)
print("\nshape:",sensor_data.shape)

# Step 2 — Sort by robot and time
#This is very important before calculating changes.

sensor_data=sensor_data.sort_values(["robot_id","timestamp"])
print("\n Sorted sensor Data :")
print(sensor_data)

# Time-series calculations must generally be performed in chronological order.

#Step 3 — Calculate battery change
#Now we'll use one of the most useful Pandas functions for time-series data: diff()

sensor_data["battery_change"]=(sensor_data.groupby("robot_id")["battery"].diff())
print("\nBattery Change")
print(sensor_data[["timestamp","robot_id","battery","battery_change"]])

#Step 4 — Calculate temperature change
#Now do the same thing:
sensor_data["temperature_change"]=(sensor_data.groupby("robot_id")["temperature"].diff())
print("\nTemperature change")
print(sensor_data[["timestamp","robot_id","temperature","temperature_change"]])

#Now we can see whether each robot's temperature is increasing or decreasing.

#Step 5 — Calculate vibration change
sensor_data["vibration_change"]=(sensor_data.groupby("robot_id")["vibration"].diff())
print("\nVibration change")
print(sensor_data[["timestamp","robot_id","vibration","vibration_change"]])

#Step 6 — Calculate current change
sensor_data["current_change"]=(sensor_data.groupby("robot_id")["current"].diff())
print("\ncurrent change")
print(sensor_data[["timestamp","robot_id","current","current_change"]])

"""
diff() : Calculates the difference between the current observation and the previous observation."""

# Next: calculate time between readings
# Time difference between consecutive readings for each robot

sensor_data["time_difference"]=(sensor_data.groupby("robot_id")["timestamp"].diff())
print("\n Time Difference :")
print(sensor_data[["timestamp","robot_id","time_difference"]])

"""Time difference:-
The amount of time elapsed between two consecutive observations."""

sensor_data["time_minutes"]=(sensor_data["time_difference"].dt.total_seconds()/60)
print("\n Time Difference In Minutes :")
print(sensor_data[["timestamp","robot_id","time_difference","time_minutes"]])

# dt.total_seconds() converts a Pandas timedelta into seconds.

# Then: Battery Consumption Rate 
#Now we can combine the two things we just learned:

sensor_data["battery_rate"]=(sensor_data["battery_change"] / sensor_data["time_minutes"])
print("\nBattery Consumption Rate :")
print(sensor_data[["timestamp","robot_id","battery_change","time_minutes","battery_rate"]])


# Then: temperature  Rate 

sensor_data["temperature_rate"]=(sensor_data["temperature_change"] / sensor_data["time_minutes"])
print("\nTemperature change Rate :")
print(sensor_data[["timestamp","robot_id","temperature_change","time_minutes","temperature_rate"]])

"""Temperature Rate :-
Measures how quickly the robot's temperature changes over time."""

# Then: vibration  Rate 

sensor_data["vibration_rate"]=(sensor_data["vibration_change"] / sensor_data["time_minutes"])
print("\nVibration change Rate :")
print(sensor_data[["timestamp","robot_id","vibration_change","time_minutes","vibration_rate"]])

# Then: current  Rate 

sensor_data["current_rate"]=(sensor_data["current_change"] / sensor_data["time_minutes"])
print("\nCurrent change Rate :")
print(sensor_data[["timestamp","robot_id","current_change","time_minutes","current_rate"]])


# Day 4 — Pandas: Rolling Average

# Next: Rolling average for Temperature
sensor_data["temperature_rolling_mean"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nTemperature Rolling Mean :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_mean"]])

# Next: Rolling average for vibration
sensor_data["vibration_rolling_mean"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nVibration Rolling Mean :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_mean"]])

# Next: Rolling average for Current
sensor_data["current_rolling_mean"]=(sensor_data.groupby("robot_id")["current"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nCurrent Rolling Mean :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_mean"]])

# Next: Rolling average for Battery
sensor_data["battery_rolling_mean"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).mean().reset_index(level=0,drop=True))
print("\nBattery Rolling Mean :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_mean"]])

"""rolling(3) means:
Take the current value and the previous 2 values for the same robot, then calculate their average."""



# Next: Rolling Standard Deviation

# Next: Rolling Standard Deviation for Temperature
sensor_data["temperature_rolling_std"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).std().reset_index(level=0,drop=True))
print("\nTemperature Rolling std :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_std"]])

# Next: Rolling Standard Deviation for vibration
sensor_data["vibration_rolling_std"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).std().reset_index(level=0,drop=True))
print("\nVibration Rolling std :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_std"]])

# Next: Rolling Standard Deviation for Current
sensor_data["current_rolling_std"]=(sensor_data.groupby("robot_id")["current"].rolling(3).std().reset_index(level=0,drop=True))
print("\nCurrent Rolling std :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_std"]])

# Next: Rolling Standard Deviation for Battery
sensor_data["battery_rolling_std"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).std().reset_index(level=0,drop=True))
print("\nBattery Rolling std :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_std"]])



# 1. Rolling minimum — .rolling().min()

# Next: Rolling minimum for Temperature
sensor_data["temperature_rolling_min"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).min().reset_index(level=0,drop=True))
print("\nTemperature Rolling min :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_min"]])

# Next: Rolling minimum for vibration
sensor_data["vibration_rolling_min"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).min().reset_index(level=0,drop=True))
print("\nVibration Rolling min :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_min"]])

# Next: Rolling minimum for Current
sensor_data["current_rolling_min"]=(sensor_data.groupby("robot_id")["current"].rolling(3).min().reset_index(level=0,drop=True))
print("\nCurrent Rolling min :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_min"]])

# Next: Rolling minimum for Battery
sensor_data["battery_rolling_min"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).min().reset_index(level=0,drop=True))
print("\nBattery Rolling min :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_min"]])


#2. Rolling maximum — .rolling().max()

# Next: Rolling maximum for Temperature
sensor_data["temperature_rolling_max"]=(sensor_data.groupby("robot_id")["temperature"].rolling(3).max().reset_index(level=0,drop=True))
print("\nTemperature Rolling max :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_rolling_max"]])

# Next: Rolling maximum for vibration
sensor_data["vibration_rolling_max"]=(sensor_data.groupby("robot_id")["vibration"].rolling(3).max().reset_index(level=0,drop=True))
print("\nVibration Rolling max :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_rolling_max"]])

# Next: Rolling maximum for Current
sensor_data["current_rolling_max"]=(sensor_data.groupby("robot_id")["current"].rolling(3).max().reset_index(level=0,drop=True))
print("\nCurrent Rolling max :")
print(sensor_data[["timestamp","robot_id","current","current_rolling_max"]])

# Next: Rolling maximum for Battery
sensor_data["battery_rolling_max"]=(sensor_data.groupby("robot_id")["battery"].rolling(3).max().reset_index(level=0,drop=True))
print("\nBattery Rolling max :")
print(sensor_data[["timestamp","robot_id","battery","battery_rolling_max"]])

#Next → shift() and lag features.

"""
shift(1) = previous reading
shift(2) = 2 readings ago
shift(3) = 3 readings ago
"""

# Temperature Lag 1
sensor_data["temperature_previous"] =(sensor_data.groupby("robot_id")["temperature"].shift(1))
print("\nTemperature Lag 1 :")
print(sensor_data[["timestamp","robot_id","temperature","temperature_previous"]])

# Vibration Lag 1 
sensor_data["vibration_previous"] =(sensor_data.groupby("robot_id")["vibration"].shift(1))
print("\nVibration Lag 1 :")
print(sensor_data[["timestamp","robot_id","vibration","vibration_previous"]])

# Current Lag 1
sensor_data["current_previous"] =(sensor_data.groupby("robot_id")["current"].shift(1))
print("\nCurrent Lag 1 :")
print(sensor_data[["timestamp","robot_id","current","current_previous"]])

# Battery Lag 1
sensor_data["battery_previous"] =(sensor_data.groupby("robot_id")["battery"].shift(1))
print("\nBattery Lag 1 :")
print(sensor_data[["timestamp","robot_id","battery","battery_previous"]])


# Next topic → Categorical Features: One-Hot Encoding
"""
Categorical features are converted into numerical representations so ML algorithms can use them.For binary categories, 
0/1 encoding is simple. For multiple unordered categories, One-Hot Encoding is commonly used.
"""
# pd.get_dummies() converts categorical values into separate binary columns.
# dtype=int makes the output explicitly 0 and 1 instead of False and True.

sensor_data=pd.get_dummies(sensor_data,columns=["status"],dtype=int)
print("\nOne-Hot Encoding in status :")
print(sensor_data)

# Next useful topic : Feature selection / choosing which features actually matter for ML.
# Which columns should be inputs (X), and which column should be the prediction target (y)?

"""
Important note :-

NaN does matter for ML, but NaN created naturally by shift(), diff(), or rolling() is expected. 
We handle it at the appropriate preprocessing stage before model training.
"""
# Next → Feature Selection :-
"""
1. What is Feature Selection?
Feature selection means:
Choosing the useful input columns (features) for an ML model and leaving out columns that don't help or shouldn't be used.
"""

# Next topic → Train/Test Split
# 1. Why do we split the data?
"""
1. Why do we split the data?
Suppose we have robot sensor data:
battery
temperature
vibration
current
...
and we want our ML model to predict something.
We cannot train the model using all the data and then test it on the exact same data.
Why?
Imagine I give you 100 questions to study, then give you the same 100 questions in the exam.
You might get 100%.
But that doesn't prove you can solve new questions.
ML is similar.
We want to know:
Can the model make good predictions on data it has never seen before?
"""
#  2. Training data vs Testing data
"""
2. Training data vs Testing data
We divide our dataset into two parts:

                Dataset
                    ↓
            ┌─────────┴─────────┐
            ↓                   ↓
        Training data       Testing data
            ↓                   ↓
        Model learns       Model is evaluated
        
Usually, something like:
80% → Training
20% → Testing

For example, if we had 1,000 samples:
800 → training
200 → testing
The model sees the 800 training samples during learning.
The 200 test samples are kept aside until evaluation.
"""
# 3. In our robot project
"""
3. In our robot project

Suppose:
X = battery, temperature, vibration, current...
y = robot status

We could split them:
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
Don't worry about memorizing every argument yet.
The important part is understanding what comes out:

X_train → training inputs
X_test  → testing inputs

y_train → training answers
y_test  → testing answers

Then:
X_train + y_train
        ↓
    ML model learns
        ↓
X_test
        ↓
Model predicts
        ↓
Compare prediction with y_test
"""

# 4. What is test_size=0.2?
"""
4. What is test_size=0.2?
It means:
20% → testing
80% → training

So:
test_size=0.2
means 20% of the data is reserved for testing.
"""

# 5. What is random_state=42?
"""
5. What is random_state=42?
This is not an ML algorithm.
It simply makes the random split repeatable.
Without it, you could run your program today and get one split, then run it again and get a different split.
With:
random_state=42
you get the same split every time, assuming the data and setup are unchanged.
The number 42 isn't special. You could use another fixed integer.
"""

#Write this in your notes :
"""
Train/Test Split: Dividing a dataset into training and testing portions. 
The training data is used to train the ML model, while the testing data is kept separate to evaluate how well the model performs on unseen data.
"""

# Next → Feature Scaling

"""
Next → Feature Scaling
Now we move to another very important ML preprocessing step.
Our robot features have very different numerical ranges.

For example:
battery      → 3 to 95
temperature  → 43 to 97
vibration    → 1.1 to 8.1
current      → 2.0 to 6.5

If we directly give these to some ML algorithms, the features with larger numerical scales can have an unwanted influence.

What is Feature Scaling?
Feature scaling means transforming numerical features so that they are on comparable scales.

For example:
Before:
battery       = 92
temperature   = 45
vibration    = 1.2
current      = 2.1

After scaling, they might become values roughly around:
battery       → 0.8
temperature   → -0.5
vibration     → -0.9
current       → -0.7

The exact values depend on the scaling method.
The important method for us → Standardization
One of the most commonly used methods is StandardScaler from Scikit-learn.
It transforms the feature using its mean and standard deviation:
Where:
x = original value
μ = mean of that feature
σ = standard deviation
z = scaled value
After standardization, a feature generally has:
mean ≈ 0
standard deviation ≈ 1
Why is this useful?
Consider two features:
temperature → 40–100
vibration   → 1 –8
After standardization, both are represented relative to their own distributions rather than simply their raw numerical magnitude.
Very important ⚠️
We don't scale everything blindly.

For example:
battery → numerical → can be scaled
temperature → numerical → can be scaled
vibration → numerical → can be scaled
current → numerical → can be scaled
status_Offline → binary → usually leave as 0/1
status_Running → binary → usually leave as 0/1

And columns such as robot_id are not automatically useful just because they're numbers.

# Write this in your notes :-
Feature Scaling: Transforming numerical features to comparable scales so that differences in their original numerical ranges do not unnecessarily affect ML algorithms.
Standardization: A scaling technique that transforms data using the feature's mean and standard deviation.
"""

