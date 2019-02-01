
def compute_hw_average(grades, num_dropped):
    if len(grades) == 0 or num_dropped >= len(grades):
        return 0
    return sum(grades)/len(grades)
