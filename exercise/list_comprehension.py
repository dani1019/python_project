squares = []
for x in range(10):
    squares.append(x**2)

print(f"squares: {squares}")

squares_2 = list(map(lamda x:x**2, range(10))