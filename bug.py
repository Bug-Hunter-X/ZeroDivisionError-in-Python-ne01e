def my_function(x):
    if x == 0:
        return 0
    else:
        return 1 / x

print(my_function(0)) #This will raise a ZeroDivisionError
print(my_function(5))