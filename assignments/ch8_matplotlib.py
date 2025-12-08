import matplotlib.pyplot as plt
def plot_sample():
    x = [1,2,3,4,5]
    y = [1,4,9,16,25]
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sample Plot')
    plt.savefig('sample_plot.png')
if __name__ == '__main__':
    plot_sample()
