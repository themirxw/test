# تعریف آرایه دو بعدی
cars = [
    ['Red', 'Blue', 'Green', 'Black'],  # رنگ‌ها
    ['BMW', 'Toyota', 'Honda', 'Ford']   # اسم‌ها
]

print(cars[0][2])
# چاپ آرایه
for i in range(len(cars[0])):  # فرض بر اینکه هر دو بعد یک طول دارند
    print(f'Car: {cars[1][i]}, Color: {cars[0][i]}')
