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

Very important :-
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

# Next → StandardScaler in practice

"""
Next → StandardScaler in practice

Now we understand why scaling is needed. Let's understand exactly how StandardScaler works.

1. Import it
from sklearn.preprocessing import StandardScaler

StandardScaler is the Scikit-learn tool that performs standardization.

2. Create the scaler
scaler = StandardScaler()

At this point, the scaler hasn't learned anything from our data yet.

3. fit() — learn from training data
scaler.fit(X_train)

The scaler calculates the mean and standard deviation of each feature using only X_train.

For example:
Training temperature:
45, 47, 49, 50, 52, ...
It learns:
mean = ...
std  = ...
It does this separately for every numerical feature.

4. transform() — scale the data
X_train_scaled = scaler.transform(X_train)
Now the original values are converted into standardized values.
5. Transform the test data
X_test_scaled = scaler.transform(X_test)
Notice something important:
❌ Don't do:
scaler.fit(X_test)

Instead:
X_train
    ↓
fit()
    ↓
Scaler learns training statistics
    ↓
transform X_train
    ↓
transform X_test

The test data must remain unseen during the fitting process.

🚨 Why is this so important?

Imagine we're predicting robot failure.

If we calculate the mean and standard deviation using both training and test data, information from the test set has leaked into the preprocessing stage.

That's called data leakage.

The model would indirectly get information about data that is supposed to be unseen.

So remember this rule:

FIT → Training data only.

TRANSFORM → Training and test data.

📝 Write this in your notes
StandardScaler
    ↓
fit(X_train)
    ↓
learn mean + standard deviation
    ↓
transform(X_train)
transform(X_test)

Never fit the scaler on the test set.
"""

"""
Note this :-

fit() learns the scaling parameters from training data.
transform() applies those learned parameters to data.
"""


# 1. Why do some ML models need scaling?

"""
1. Why do some ML models need scaling?

Imagine your robot dataset has:

Feature	Example
Temperature	50 °C
Vibration	2.5
Current	3.2 A
Battery	80 %

The numerical ranges are very different.

For example:

Temperature → 50
Vibration   → 2.5
Current     → 3.2
Battery     → 80

If an algorithm calculates distance or is affected by the size/magnitude of features, the larger-valued feature can dominate.

Scaling puts features onto a comparable numerical range.

2. K-Nearest Neighbors (KNN)

KNN literally means:

Find the closest data points and use them to make a prediction.

For example, imagine we want to determine whether a robot is:

Normal
Fault

KNN looks at nearby robots in feature space.

k = 3: Class A wins 2–1; the point is Class A.
k
k
Give feedback

Suppose:

Temperature = 80
Vibration   = 2

Temperature has a much larger numerical value.

Without scaling, the distance calculation can be dominated by temperature.

So KNN is very sensitive to feature scale.

📝 Note

KNN needs scaling because it uses distance to find the nearest data points.

3. K-Means

K-Means also uses distance.

It tries to divide data into groups called clusters.

For example, your robot data might naturally form:

Cluster 1 → Healthy robots
Cluster 2 → Warning condition
Cluster 3 → Fault condition

If temperature ranges from 20–100 while vibration ranges from 0–10, temperature can have much more influence on the distance.

So scaling is normally important.

📝 Note

K-Means needs scaling because it uses distance to determine which cluster a data point belongs to.

4. SVM — Support Vector Machine

SVM tries to find a boundary that separates classes.

For example:

Normal robots | Faulty robots

The scale of features affects the geometry of that boundary.

If one feature has a much larger scale, it can disproportionately influence the model.

So scaling is generally recommended for SVM.

📝 Note

SVM benefits from scaling because feature magnitude affects the geometry of the decision boundary.

5. Logistic Regression

This one is slightly different.

Logistic Regression doesn't primarily use distance like KNN or K-Means.

But its optimization process is affected by feature scales.

Suppose:

temperature = 80
vibration   = 2
current      = 3

Very different scales can make optimization less efficient and make regularization behave unevenly across features.

Scaling usually makes training more stable and efficient.

📝 Note

Logistic Regression benefits from scaling because its optimization and regularization are affected by feature magnitude.

6. Neural Networks

Neural networks also benefit strongly from properly scaled input features.

Imagine feeding:

temperature = 80
vibration   = 2
current     = 3
battery     = 80

The network has to learn weights while dealing with very different feature magnitudes.

Scaling the inputs generally makes training easier and more stable.

For example:

Before:


temperature = 80
vibration   = 2
current     = 3


After scaling:


temperature = 0.4
vibration   = -0.2
current     = 0.1

The exact values depend on the scaler and dataset.

📝 Note

Neural networks generally train better when numerical input features are appropriately scaled.

7. What about Random Forest?

This is important.

Random Forest generally doesn't require feature scaling.

Why?

A decision tree mostly asks questions like:

Is temperature > 70?

or:

Is vibration > 4?

It isn't calculating distances between points in the same way KNN does.

So:

KNN          → Scaling important
K-Means      → Scaling important
SVM          → Scaling important
Logistic Reg → Usually beneficial
Neural Net   → Usually beneficial


Decision Tree → Usually NOT required
Random Forest → Usually NOT required

This is why we don't blindly scale every dataset for every model. 
"""

# Now → Data Leakage

"""
Now → Data Leakage 🚨

This is a very important ML concept.

Data leakage means:

Information that should not be available to the model during training accidentally gets into the training process.

The model then appears extremely good during testing, but when you give it real-world data, its performance can drop badly.

Simple example

Imagine we're building a robot fault prediction model.

We have:

Temperature
Vibration
Current
Battery
Fault

We split:

80% → Training
20% → Testing

Correct.

But suppose we calculate the scaler using the entire dataset before splitting:

All data
    ↓
fit StandardScaler
    ↓
split train/test

Now the scaler has already seen information from the test set.

That's a form of data leakage.

Instead:

All data
    ↓
split
↙   ↘
Train  Test
↓      ↓
fit    transform
↓      ↓
transform

More precisely:

X_train
    ↓
scaler.fit(X_train)
    ↓
scaler.transform(X_train)


X_test
    ↓
scaler.transform(X_test)

Never:

scaler.fit(X_test)

and don't do:

scaler.fit(X)   # before train/test split
Why is this important for your robot project?

Suppose your future system receives sensor data:

Temperature
Vibration
Current
Battery

and predicts:

Normal / Warning / Failure

We want the model to behave as if it is seeing new robot data for the first time.

If information from the future/test data leaks into training, your model may look excellent on paper while being unreliable on the actual robot.

📝 Important note

Data leakage = information from outside the training process unintentionally influences the model.

And one of the most common mistakes is:

Preprocessing the entire dataset before train/test splitting.

The ML workflow we are building
Raw Data
    ↓
Clean Data
    ↓
Feature Engineering
    ↓
Train/Test Split
    ↓
Fit preprocessing ONLY on Train
    ↓
Transform Train + Test
    ↓
Train Model
    ↓
Evaluate Model

This is the workflow I want you to understand rather than memorizing individual small pandas functions.
"""


# `fit()` vs `transform()`


"""Let's continue. **No rushing—we'll take one useful concept at a time.**

# `fit()` vs `transform()`

This is extremely important because it connects directly to **data leakage**.

Think of a `StandardScaler`:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
```

Now there are two main operations.

### 1. `fit()`

`fit()` means:

> **Learn the necessary information from the data.**

For example:

```python
scaler.fit(X_train)
```

The scaler looks at `X_train` and learns things such as:

* mean
* standard deviation

It **doesn't change the data yet**.

---

### 2. `transform()`

`transform()` means:

> **Use what was learned to convert the data.**

```python
X_train_scaled = scaler.transform(X_train)
```

The scaler uses the mean and standard deviation it learned during `fit()` and converts the values.

---

### 3. `fit_transform()`

There is also a shortcut:

```python
X_train_scaled = scaler.fit_transform(X_train)
```

This means:

```text
fit()
+
transform()
```

in one operation.

---

# 🚨 The important rule

For training data:

```python
X_train_scaled = scaler.fit_transform(X_train)
```

For test data:

```python
X_test_scaled = scaler.transform(X_test)
```

**Do NOT do this:**

```python
X_test_scaled = scaler.fit_transform(X_test)
```

Why?

Because then you're allowing the scaler to **learn from the test data**.

That's exactly what we were talking about with **data leakage**.

### Remember this:

> **Training data → `fit_transform()`**
> **Test data → `transform()`**

---

## Simple way to remember

Imagine you are teaching the scaler:

```text
TRAINING DATA
    ↓
    FIT
"Learn from this"
    ↓
TRANSFORM
"Now convert it"
```

Then test data comes:

```text
TEST DATA
    ↓
TRANSFORM
"Use what you already learned"
```

You **don't teach it again** using the test data.

---

### 📝 Put this in your notes

```text
fit()            → learn from data
transform()      → convert data using what was learned
fit_transform()  → fit + transform

Training → fit_transform()
Testing  → transform()

Never fit the scaler on test data.
```

This concept will become much clearer when we build our **first actual ML model**, so we don't need to spend more time on tiny examples.

**Next → First ML model: Linear Regression / classification?** We'll choose based on our robot dataset so you're actually building something useful.
"""


# Next → Our first real ML model 🤖


"""Next → Our first real ML model 🤖

Now we're moving from Pandas → actual Machine Learning.

Before choosing the model, we need to understand one very important distinction:

1. Regression vs Classification

Almost every supervised ML problem starts with identifying what we are trying to predict.

Regression

Regression predicts a number.

Examples:

Predict robot temperature → 72.5 °C
Predict battery remaining → 63.2 %
Predict motor current → 4.8 A
Predict house price → ₹45,00,000

So:

Regression → output is a continuous numerical value.

Classification

Classification predicts a category/class.

For your robot:

Temperature
Vibration
Current
Battery
    ↓
    ML
    ↓
Normal / Fault

Or:

0 → Normal
1 → Fault

So:

Classification → output is a class/category.

2. Which one should we build first?

For our robot dataset, I recommend classification first.

Why?

We already have:

robot_id
battery
temperature
vibration
current
status

We can create a useful target such as:

fault

and train a model to predict whether a robot is likely to be in a normal or faulty condition.

This is much closer to a real robotics/automation application than doing an unrelated house-price example.

3. One important ML concept: X and y

You will see these two variables everywhere in ML.

X = Features

These are the inputs given to the model.

For example:

X = df[
    [
        "battery",
        "temperature",
        "vibration",
        "current"
    ]
]

So:

X
↓
Battery
Temperature
Vibration
Current
y = Target

This is what we want the model to predict.

For example:

y = df["fault"]

So:

X                    y
-------------------------
Battery       ─┐
Temperature    │
Vibration      ├──→ Fault
Current        ─┘
📝 Notes

X = input/features
y = target/output

This is one of the most important things to remember in ML.

4. Then we split the data

We already studied this:

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Conceptually:

        Dataset
            │
        ┌─────┴─────┐
        ↓           ↓
        Training      Testing
        80%           20%
        │             │
        ↓             ↓
    Learn          Evaluate

The model learns from the training data.

Then we test whether it can handle data it didn't learn from.

5. The first model we'll use

For classification, we'll start with:

Logistic Regression

Don't let the word Regression confuse you.

Despite its name, Logistic Regression is commonly used for classification.

For example:

Input:
Battery = 20
Temperature = 85
Vibration = 6
Current = 5

        ↓

Logistic Regression

        ↓

Fault probability = 0.94

        ↓

Fault = 1

So the model can produce a probability and then classify the result.

Why start with Logistic Regression?

Because it teaches several fundamental ML concepts at once:

Features X
Target y
Train/test split
Scaling
fit()
predict()
Probability
Classification
Evaluation

Later we'll move to models that are particularly useful for your robotics data, such as:

Logistic Regression
        ↓
Decision Tree
        ↓
Random Forest
        ↓
Gradient Boosting
        ↓
More advanced ML

And eventually we can use these concepts for predictive maintenance, which is directly relevant to robotics and automation.

One thing before we code

We shouldn't blindly create a fault column just to make the model run.

We need to define what actually counts as a fault and create a meaningful target from the sensor data.

That's the next practical step.

Next → Creating a proper ML target (y) from our robot sensor data → then we train our first model.
"""


# Creating the ML Target — y

"""
Creating the ML Target — y

Before training a model, we need to tell it:

"What exactly am I trying to predict?"

For our robot dataset, we'll use:

fault = 0 → Normal
fault = 1 → Fault

But we shouldn't randomly label rows. The target should come from a meaningful rule based on the robot's condition.

For example, a robot showing:

very high temperature
high vibration
high current
very low battery

could be considered a potential fault condition.

Conceptually:

Temperature ─┐
Vibration   ─┤
Current     ─┼──→ Robot condition → fault
Battery     ─┘
Important ML idea

The sensor measurements are our features (X):

X = df[[
    "battery",
    "temperature",
    "vibration",
    "current"
]]

And the condition we want the model to predict is y:

y = df["fault"]

So the complete idea is:

              X
       ┌───────────────┐
       │ Battery       │
       │ Temperature   │
       │ Vibration     │
       │ Current       │
       └───────┬───────┘
               ↓
          ML MODEL
               ↓
              y
       ┌───────────────┐
       │ 0 = Normal    │
       │ 1 = Fault     │
       └───────────────┘
⚠️ One thing we need to be careful about

If we create fault directly from temperature/vibration/current thresholds and then give those same measurements to the model, the model may simply learn the exact rule we used.

That's useful for learning how ML works, but it isn't yet a genuine predictive-maintenance dataset.

So for our first learning model, we'll use a simple rule-based target to understand the complete ML pipeline. Later, we'll work with a more realistic target such as an actual recorded failure/event.

📝 Notes

X = features/input data
y = target/output we want to predict

For our robot project:

X → battery, temperature, vibration, current
y → fault (0/1)

Next → We'll actually create fault, inspect the class distribution, and then do the train/test split.
"""

# Step 1 — Create the fault column : -
sensor_data["fault"] = (
    (sensor_data["temperature"]>=80) |
    (sensor_data["vibration"]>=5) |
    (sensor_data["current"]>=4.5) |
    (sensor_data["battery"]<=20)
) .astype(int)
print("\nFault Target :")
print(sensor_data[["robot_id","temperature","vibration","current","battery","fault"]])

# Next → Create X and y 

# features (x)
x = sensor_data[["battery","temperature","vibration","current"]]

# Target (y)
y = sensor_data["fault"]

print("\nFeatures x :")
print(x)

print("\nTarget y :")
print(y)

"""
X = features/input variables
battery, temperature, vibration, current

y = target/output variable
fault
"""
# Next → Train/Test Split :- 

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("\nx_train :")
print(x_train)

print("\nx_test :")
print(x_test)

print("\ny_train :")
print(y_train)

print("\ny_test :")
print(y_test)

print("\nShapes :")
print("x_train:",x_train.shape)
print("x_test:",x_test.shape)
print("y_train:",y_train.shape)
print("y_test:",y_test.shape)

# Topic: Logistic Regression :- Logistic Regression learns the relationship between your input features and the target.

# Create the model :-

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

#Train the model
model.fit(x_train,y_train)  # .fit() means: Learn the relationship between X and y from the training data.

# Make predictions :-
y_pred = model.predict(x_test)

print("\nActual:",y_test.values)
print("predicted:",y_pred)