expressions = [
    "5 + 2 * 3 - 4 / 2",
    "(3 + 5) * (2 + 4) / 2",
    "-3 + 6 / 2 * 4",
    "5 + 4 * 5**2 + 7"
]
for expr in expressions:
    result = eval(expr)
    print(f"Значение выражения '{expr}' равно: {result}")