from fake_math import divide as fake_divide
from try_math import divide as try_divide

print()
print('Задача "А как делить?"')
print()

result_1 = fake_divide(35, 7)
result_2 = fake_divide(21, 0)
result_3 = try_divide(15, 2)
result_4 = try_divide(72, 0)

print('35 / 7 =', result_1)
print('21 / 0 =', result_2)
print('15 / 2 =', result_3)
print('72 / 0 =', result_4)