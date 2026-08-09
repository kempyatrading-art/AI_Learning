# code 1
""" 
import pandas as pd 
print ("pandas version : ",pd.__version__)
"""
# Step 2 — First Pandas Series:- #code 2

"""
import pandas as pd 
battery = pd.Series([92,87,95,61,15])
print("\nRobot Battery Data :")
print(battery)
"""
# Step 3 — Give the Series Robot IDs :- CODE 3 
"""
import pandas as pd 

robot_ids = [101,102,103,104,105]
battery = [92,87,95,61,15]

robot_battery = pd.Series(
    battery,
    index=robot_ids
)

print("\nRobot Battery Data : ")
print(robot_battery)
"""
# Step 4 — Access data by Robot ID :- code 4
"""
import pandas as pd 

robot_ids =[101,102,103,104,105]
battery = [92,87,95,61,15]

robot_battery = pd.Series(
    battery,
    index=robot_ids
)

print ("\n Battery of Robot 102 :",robot_battery[102],"%")
print (" Battery of Robot 105 :",robot_battery[105],"%")
"""
# Step 5 — Filtering :- code 5

import pandas as pd 

robot_ids =[101,102,103,104,105]
battery = [92,87,95,61,15]

robot_battery = pd.Series(
    battery,
    index=robot_ids
)
low_battery = robot_battery [robot_battery <20]
print("\n Robots with Low Battery :")
print(low_battery)

high_battery = robot_battery [robot_battery >= 90]

print("\nRobots with Battery >= 90%:")
print(high_battery)

medium_battery = robot_battery [(robot_battery >=60) & (robot_battery<=90)]
print("\n Robot With Battery between 60% and 90% :")
print(medium_battery)