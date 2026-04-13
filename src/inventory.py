import numpy as np
from scipy.stats import norm

def calculate_inventory(forecast, on_hand=50, lead_time=3, service=0.95):
    z = norm.ppf(service)

    demand_mean = np.mean(forecast[:lead_time])
    demand_std = np.std(forecast[:lead_time])

    safety_stock = z * demand_std
    reorder_point = demand_mean + safety_stock

    order_qty = max(0, reorder_point - on_hand)

    return {
        "Safety Stock": round(safety_stock, 2),
        "Reorder Point": round(reorder_point, 2),
        "Order Quantity": round(order_qty, 2)
    }