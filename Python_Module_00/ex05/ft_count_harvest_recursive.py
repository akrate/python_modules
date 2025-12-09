def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_day(1, days)
    print("Harvest time!")


def count_day(current, total):
    if current > total:
        return
    print(f"Day {current}")
    count_day(current + 1, total)
