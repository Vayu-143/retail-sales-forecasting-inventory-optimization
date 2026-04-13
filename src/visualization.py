import matplotlib.pyplot as plt

def plot_sales(df, predictions):
    plt.figure(figsize=(10,5))

    plt.plot(df["date"], df["qty_sold"], label="Actual", marker='o')
    plt.plot(df["date"], predictions, label="Predicted", linestyle='--')

    plt.title("Sales Forecast vs Actual")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.grid()

    plt.savefig("outputs/forecast_plot.png")
    plt.show()