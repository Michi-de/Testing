import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def KPI(product, place, price, promotion):
    return (product + place + price + promotion) / 4

# Additional functions for the original scoring logic would go here

def color_gradient(score):
    cmap = mcolors.LinearSegmentedColormap.from_list("kpi_color", ["red", "yellow", "green"])
    return cmap(score / 10)

# Sample function to generate a correlation heatmap between KPIs
def plot_correlation_heatmap(kpi_scores):
    data = np.array([
        [kpi_scores['product'], kpi_scores['place'], kpi_scores['price'], kpi_scores['promotion']],
        [kpi_scores['place'], kpi_scores['product'], kpi_scores['promotion'], kpi_scores['price']],
        [kpi_scores['price'], kpi_scores['promotion'], kpi_scores['place'], kpi_scores['product']],
        [kpi_scores['promotion'], kpi_scores['price'], kpi_scores['product'], kpi_scores['place']]
    ])
    plt.imshow(data, cmap='coolwarm', interpolation='nearest')
    plt.colorbar(label='Correlation Score')
    plt.xticks(np.arange(4), ['Product', 'Place', 'Price', 'Promotion'])
    plt.yticks(np.arange(4), ['Product', 'Place', 'Price', 'Promotion'])
    plt.title('KPI Correlation Heatmap')

# Simulated map plot for "Place" or "Geographic Reach"
def plot_geographical_map(kpi_scores):
    regions = ['North America', 'Europe', 'Asia', 'South America']
    reach_scores = [7.5, 8.3, 6.2, 5.8]  # Simulated data

    plt.scatter(np.arange(len(regions)), reach_scores, c='blue', s=100, label="Geographic Reach")
    plt.xticks(np.arange(len(regions)), regions)
    plt.ylim(0, 10)
    plt.title('Geographic Reach Based on KPI')
    plt.ylabel('Score')
    plt.xlabel('Region')

def plot_dashboard(kpi_scores):
    fig, axes = plt.subplots(3, 2, figsize=(18, 15))  # Adjusting layout to fit 6 plots

    # Pie Chart
    labels = ['Product', 'Place', 'Price', 'Promotion']
    sizes = [kpi_scores['product'], kpi_scores['place'], kpi_scores['price'], kpi_scores['promotion']]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
    explode = (0.1, 0, 0, 0)
    
    axes[0, 0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    axes[0, 0].axis('equal')
    axes[0, 0].set_title('KPI Pie Chart')

    # Bar Chart
    metrics = ['Product', 'Place', 'Price', 'Promotion', 'Overall KPI']
    scores = [
        kpi_scores['product'],
        kpi_scores['place'],
        kpi_scores['price'],
        kpi_scores['promotion'],
        kpi_scores['overall_kpi']
    ]
    bar_colors = [color_gradient(score) for score in scores]
    bars = axes[0, 1].bar(metrics, scores, color=bar_colors)
    axes[0, 1].set_ylim(0, 10)
    axes[0, 1].set_title('KPI Dashboard')
    axes[0, 1].set_xlabel('Metric')
    axes[0, 1].set_ylabel('Score')
    for bar in bars:
        yval = bar.get_height()
        axes[0, 1].text(bar.get_x() + bar.get_width()/2, yval + 0.2, f"{yval:.2f}", ha='center', fontsize=12)

    # Piktogramm
    axes[1, 0].scatter(kpi_scores['product'], kpi_scores['place'], s=100, c='blue', label='Product vs Place')
    axes[1, 0].scatter(kpi_scores['price'], kpi_scores['promotion'], s=100, c='red', label='Price vs Promotion')
    axes[1, 0].set_title('Piktogramm')
    axes[1, 0].set_xlabel('Score')
    axes[1, 0].set_ylabel('Score')
    axes[1, 0].legend()

    # Streuungsdiagramm
    axes[1, 1].scatter(metrics, scores, c=bar_colors)
    axes[1, 1].set_title('Streuungsdiagramm')
    axes[1, 1].set_xlabel('Metric')
    axes[1, 1].set_ylabel('Score')

    # Correlation Heatmap
    plt.sca(axes[2, 0])
    plot_correlation_heatmap(kpi_scores)

    # Geographic Map Simulation
    plt.sca(axes[2, 1])
    plot_geographical_map(kpi_scores)

    plt.tight_layout()
    plt.show()

# Input collection (for simplicity, using static values)
kpi_scores = {
    'product': 8.0,
    'place': 6.5,
    'price': 7.2,
    'promotion': 8.8,
    'overall_kpi': 7.63
}

# Display all diagrams on the dashboard
plot_dashboard(kpi_scores)

