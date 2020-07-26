import matplotlib.pyplot as plt

from random_walk import RandomWalk

#keep making the new walks, as long as the program is active

while True:
    #make a random walk

    rw = RandomWalk(50_000)
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 16), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #Emphasise the first and the last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    Keep_running = input("Make another walk ? (y/n): ")
    if Keep_running == 'n':
        break
        
    
