print("Hello")

val1 = 1.23
val2 = 2.80
val3 = True

print(val1+val2)

global_var = "vegetable"
def letsprint():
    global global_var
    global_var = "fruit"
    return global_var


print(global_var)
print(letsprint())
print(global_var)

