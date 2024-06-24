from sympy import symbols, Eq, solve

equation_str = input('Entrez une équation : ')

left_side, right_side = equation_str.split('=')

x = symbols('x')
left_expr = eval(left_side.replace('^', '**'))
right_expr = eval(right_side)

equation = Eq(left_expr, right_expr)

solutions = solve(equation, x)

print('Les solutions de l\'équation sont :', solutions)
