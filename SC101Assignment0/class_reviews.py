"""
File: class_reviews.py
Name:Eden
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = '-1'

def main():
    """
    TODO:
    """
    max_001 = -float('inf')
    min_001 = float('inf')
    count_001 = 0
    total_001 = 0
    max_101 = -float('inf')
    min_101 = float('inf')
    count_101 = 0
    total_101 = 0

    while True:
        course = input('Which class?')
        if course == EXIT:
            break
        course = course.upper()
        score = int(input('Score?' ))
        if course == 'SC001':
            if count_001 == 0:
                max_001 = score
                min_001 = score
            if score >  max_001:
                max_001 = score
            elif score <  min_001:
                min_001 = score
            total_001 += score
            count_001 += 1
        if course == 'SC101':
            if count_101 == 0:
                max_101 = score
                min_101 = score
            if score > max_001:
                max_101 = score
            elif score < min_001:
                min_101 = score
            total_101 += score
            count_101 += 1

    if count_101 == count_001 == 0:
        print('No class scores were entered.')
    elif count_001 == 0:
        avg_101 = float(total_101 / count_101)
        print('=============SC001=============')
        print('No score for SC001')
        print('=============SC101=============')
        print('Max(101): ' + str(max_101))
        print('Min(101): ' + str(min_101))
        print('Avg(101): ' + str(avg_101))
    elif count_101 == 0:
        avg_001 = float(total_001 / count_001)
        print('=============SC001=============')
        print('Max(001): ' + str(max_001))
        print('Min(001): ' + str(min_001))
        print('Avg(001): ' + str(avg_001))
        print('=============SC101=============')
        print('No score for SC101')
    else:
        avg_101 = float(total_101 / count_101)
        avg_001 = float(total_001 / count_001)
        print('=============SC001=============')
        print('Max(001): ' + str(max_001))
        print('Min(001): ' + str(min_001))
        print('Avg(001): ' + str(avg_001))
        print('=============SC101=============')
        print('Max(101): ' + str(max_101))
        print('Min(101): ' + str(min_101))
        print('Avg(101): ' + str(avg_101))

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
