x = int(input("Wprowadź współrzędną x: "))
y = int(input("Wprowadź współrzędną y: "))
if x > 0 and y > 0:
    print(f"Twoje współrzędne ({x},{y}) znajdują się w pierwszym kwadracie układu współrzędnych")
elif x < 0 and y > 0:
     print(f"Twoje współrzędne ({x},{y}) znajdują się w drugim kwadracie układu współrzędnych")
elif x < 0  and y < 0:
    print(f"Twoje współrzędne ({x},{y}) znajdują się w trzecim kwadracie układu współrzędnych")
elif x > 0 and y < 0:
    print(f"Twoje współrzędne ({x},{y}) znajdują się w czwartym kwadracie układu współrzędnych")
else:
    print(f"Twoje współrzędne ({x},{y}) znajdują się na środku układu współrzędnych")