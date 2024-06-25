def rental_car_cost(d):
    return d * 40 - 50 if d >= 7 else (d * 40 - 20 if 3 <= d < 7 else d * 40)
