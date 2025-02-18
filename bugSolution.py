def my_function(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        return float('inf') # Or handle the error in a more appropriate way

print(my_function(0))
print(my_function(5))