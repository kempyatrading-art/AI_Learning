#code : 1   04-08-2026   --- 11:15 PM
# step1 
"""
import numpy as np 
numbers = np.array([10,20,30,40,50])
print("Array : ",numbers)
print("Type : ",type(numbers))

"""
"""
import numpy as np 
numbers = np.array([10,20,30,40,50])
print(numbers[2])
print(numbers[4])

"""
# Step 2 — Access Elements
"""
import numpy as np 
numbers =np.array([10,20,30,40,50])

print("Array : ",numbers)
print("First Element : ",numbers[0])
print("Second Element : ",numbers[1])
print("Lsat Element : ", numbers[-1])
print("Length :" , len(numbers))
print("Addition : ", numbers [1] + numbers[2])

"""
#code 3
"""
import numpy as np 
numbers =np.array([10,20,30,40,50])

print("Array : ",numbers)
print("Add 10 : ",numbers +10)
print("Multiply by 2 : ",numbers*2)
print("Divide by 10 : ", numbers/10)
print("square :" , numbers **2)

"""
#code = 4

import numpy as np  
marks = np.array([85,92,35,88,95])
print("Marks : ",marks)
print("Grace Marks : ",marks + 5)
print("Double : ", marks *2)
print ("Pass : ", marks >= 40 )