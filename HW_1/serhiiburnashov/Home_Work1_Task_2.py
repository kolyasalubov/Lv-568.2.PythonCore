# Read values a and b from console and calculate: 
#   - a + b 
#   - a - b 
#   - a * b 
#   - a / b
#   - a**b.
# Output obtained results.


a, b = (int(input("Enter values \"a\": ")), 
        int(input("Enter values \"b\": ")))

print(  "\n"   + "a + b =",  a + b, 
        "\n"   + "a - b =",  a - b, 
        "\n"   + "a * b =",  a * b, 
        "\n"   + "a / b =",  a / b, 
        "\n"   + "a ** b =", a ** b)