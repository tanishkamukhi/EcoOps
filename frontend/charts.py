import matplotlib.pyplot as plt

def plot_pie_chart(footprint):
    labels = ["Your Footprint", "Sustainable Target"]
    sizes = [footprint, max(1, footprint * 0.98)]  # Target ~98% of footprint
    colors = ["#ff6666", "#66b3ff"]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.axis("equal")
    return fig

def plot_bar_chart(df):
    fig, ax = plt.subplots()
    ax.bar(df["mode"], df["footprint"], color="green")
    ax.set_ylabel("Carbon Footprint (kg CO₂)")
    ax.set_title("Carbon Footprint by Travel Mode")
    return fig
