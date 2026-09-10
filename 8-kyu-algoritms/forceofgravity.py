def solution(arr_val, arr_unit):
    # Константа гравитации
    G = 6.67e-11
    
    # Коэффициенты перевода масс в кг
    mass_units = {
        'kg': 1,
        'g': 0.001,
        'mg': 1e-6,
        'μg': 1e-9,
        'lb': 0.453592
    }
    
    # Коэффициенты перевода расстояний в метры
    distance_units = {
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'μm': 1e-6,
        'ft': 0.3048
    }
    
    # Переводим массы в кг
    m1 = arr_val[0] * mass_units[arr_unit[0]]
    m2 = arr_val[1] * mass_units[arr_unit[1]]
    
    # Переводим расстояние в метры
    r = arr_val[2] * distance_units[arr_unit[2]]
    
    # Вычисляем силу по формуле F = G * (m1 * m2) / r^2
    force = G * (m1 * m2) / (r ** 2)
    
    return force