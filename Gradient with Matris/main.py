import sympy as sp

# Define symbolic values
x_1, x_2, alfa = sp.symbols('x_1 x_2 alpha')

#Define the function
f = x_1**2 + 6*x_2**2 + x_1*x_2

# Derivative
df_dx1 = sp.diff(f, x_1)
df_dx2 = sp.diff(f, x_2)

# Define inital values
x_1_value = 1
x_2_value = 2
alpha_value = 0.1
iterations = 9


for i in range(iterations):
    # new values
    new_x_1_value = x_1_value - alpha_value * df_dx1.subs({x_1: x_1_value, x_2: x_2_value})
    new_x_2_value = x_2_value - alpha_value * df_dx2.subs({x_1: x_1_value, x_2: x_2_value})


    print(f"Iterasyon {i + 1}:")
    print(f"x_1 = {new_x_1_value}")
    print(f"x_2 = {new_x_2_value}\n")

    # update the new values
    x_1_value = new_x_1_value
    x_2_value = new_x_2_value
