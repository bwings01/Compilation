def my_max(num_1, num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2

def my_min(num_1, num_2):
    if num_1 < num_2:
        return num_1
    else:
        return num_2

def my_avg(num_1, num_2):
    avg = (num_1 + num_2) / 2
    return avg

if __name__ == "__main__":
    my_max(num_1, num_2)
    my_min(num_1, num_2)
    my_avg(num_1, num_2)