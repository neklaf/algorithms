'''
Return the second maximum number in an array

Asymptotic time evaluation:
Linear time: O(n-2) -> O(n)
'''

def find_second_max(values):
    if len(values) == 0:
        return None
    elif len(values) == 1:
        return values[0]
    else:
        max_v,second_max_v = 0,0
        if values[0] > values[1]:
            max_v,second_max_v = values[0], values[1]
        else:
            max_v,second_max_v = values[1], values[0]

        if len(values) == 2:
            return second_max_v

        for i in range(2, len(values)):
            if values[i] > max_v:
                second_max_v = max_v
                max_v = values[i]
            elif values[i] > second_max_v:
                second_max_v = values[i]

        return second_max_v

if __name__ == '__main__':
    numbers = [1,7,11,14,25,3,2,16]
    numbers = [1]
    numbers = [1,5]
    numbers = [1,7,11]
    numbers = []
    print("Data: ",numbers)
    print(find_second_max(numbers))