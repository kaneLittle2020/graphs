import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()

def init():
  global data 
  data = {
  'x':np.array([3, 3, 4, 4, 3]),
  'y':np.array([3, 4, 4, 3, 3])
  }

def animate (frame):
  ax.cla()
  ax.set_xlim(0,10)
  ax.set_ylim(0,10)
  ax.plot(frame + data['x'], frame + data ['y'])

def run():
  simple_animation = animation.FuncAnimation (fig, animate, frames = 10, interval = 1000, init_func = init)
  

  plt.show()

run()