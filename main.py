import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate (frame):
  print(f'Frame: {frame}')

fig, ax = plt.subplots()

simple_animation = animation.FuncAnimation(fig, animate, frames = 100, interval = 100 )

plt.show()
