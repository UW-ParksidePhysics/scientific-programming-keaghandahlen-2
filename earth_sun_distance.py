import math

# The average distance between the Earth and the Sun in kilometers
AU = 149597870.7

def distance(t):
    # Convert time t in days to angle phi in radians
    phi = 2 * math.pi * t / 365.25

    # Calculate the distance between the Earth and the Sun using the equation
    # r = AU * (1 + e * cos(phi)) where e is the eccentricity of the Earth's orbit
    e = 0.01671022
    r = AU * (1 - e**2) / (1 + e * math.cos(phi))

    return r

print(distance(0))   # prints the distance between the Earth and the Sun at the beginning of the year
print(distance(365)) # prints the distance between the Earth and the Sun at the end of the year
print(distance(185)) # prints the distance between the Earth and the Sun at a given time selected

from datetime import datetime

# Get the current time as a datetime object
now = datetime.now()
time_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Assign the time string to a variable z
z = time_str
print(z)

from datetime import datetime

# Convert time_str to a datetime object
dt_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

# Convert datetime to a number of days since January 1
days = (dt_obj - datetime(2023, 1, 1)).days

print(days)

print(distance(days)) # prints the distance between the Earth and the Sun on today's date
