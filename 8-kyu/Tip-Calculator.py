from math import ceil


def calculate_tip(amount, rating):
    if rating.lower() not in ['terrible', 'poor', 'excellent', 'great', 'good']:
        return 'Rating not recognised'
    else:
        if rating.lower() == 'terrible':
            return ceil(amount * 0)
        if rating.lower() == 'poor':
            return ceil(amount * 0.05)
        if rating.lower() == 'good':
            return ceil(amount * 0.1)
        if rating.lower() == 'great':
            return ceil(amount * 0.15)
        if rating.lower() == 'excellent':
            return ceil(amount * 0.2)


print(calculate_tip(20, 'Excellent'))


def calculate_tip_more(amount, rating):
    tips = {
        'terrible': 0,
        'poor': .05,
        'good': .1,
        'great': .15,
        'excellent': .2
    }
    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
    else:
        return 'Rating not recognised'
