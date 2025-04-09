from sympy import symbols, Poly, gcd, mod_inverse


# Step 1: Given values
e = 3
n = 997
a = 2
b = 5
m1 = 42
m2 = a * m1 + b

# Step 2: Encrypt both messages
c1 = pow(m1, e, n)
c2 = pow(m2, e, n)

print(f"Encrypted c1: {c1}")
print(f"Encrypted c2: {c2}")

# Step 3: Construct polynomials
x = symbols('x')
f1 = Poly(x**e - c1, x, modulus=n)
f2 = Poly((a*x + b)**e - c2, x, modulus=n)

# Step 4: Perform GCD and extract root
g = gcd(f1, f2)
roots = g.all_roots()

if roots:
    print(f"\nRecovered original message (m1): {int(roots[0])}")
else:
    print("No root found. Attack failed.")