import math
import matplotlib.pyplot as plt

# radius of loop (in meters)
r = 0.0725

# acceleration due to gravity (in meters per second squared)
g = 9

# minimum speed needed to complete the loop (calculated using the formula v = sqrt(gr))
v = math.sqrt(g * r)

# mass of the ball (in kilograms)
m = 10

# initial position and velocity of the ball
x = 0
y = 0
vx = 0
vy = v

print("hey")
# time step (in seconds)
dt = 0.1

# list to store the positions of the ball
positions = []

# simulate the motion of the ball around the loop
while True:
  # calculate the force of gravity on the ball
  fx = 0
  fy = -m * g

  # calculate the acceleration of the ball
  ax = fx / m
  ay = fy / m

  # update the velocity of the ball
  vx += ax * dt
  vy += ay * dt

  # update the position of the ball
  x += vx * dt
  y += vy * dt

  # add the current position of the ball to the list of positions
  positions.append((x, y))

  # if the ball reaches the top of the loop, break out of the loop
  if y >= r:
    break

# create a scatter plot of the positions of the ball
plt.scatter([p[0] for p in positions], [p[1] for p in positions])
plt.show()
