def dating_range(age):
    if age > 14:
        minAge = int(age / 2 + 7)
        maxAge = int(2 * (age - 7))
        return (f"{minAge}-{maxAge}")
    else:
        minAge = int(age - 0.10 * age)
        maxAge = int(age + 0.10 * age)
        return (f"{minAge}-{maxAge}")


if __name__ == '__main__':
    print(dating_range(10))
