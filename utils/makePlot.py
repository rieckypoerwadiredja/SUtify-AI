import matplotlib.pyplot as plt

def make_plot(component=False):
    if component == False:
        print("<!> Error at make_plot, make sure the component is loaded correctly")
        return
    component.draw()
    plt.show()