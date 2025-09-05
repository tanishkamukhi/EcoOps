import matplotlib.pyplot as plt

def plot_breakdown(breakdown):
    fig, ax = plt.subplots()
    ax.pie(breakdown.values(), labels=breakdown.keys(), autopct="%1.1f%%")
    ax.axis("equal")
    return fig
