import math

# ------------------ Helpers ------------------
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter matrix ({rows}x{cols}) row by row:")
    for i in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            print("Error: Row must have", cols, "elements")
            return None
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str,row)))

# ------------------ Basic Math ------------------
def fact(n):
    if n == 0 or n == 1: return 1
    var = 1
    for i in range(2, n+1): var *= i
    return var

def sqrt(n):
    for i in range(1, n+1):
        if i*i == n: return i
    return -1

def power(base, exp): return base ** exp

# ------------------ Geometry ------------------
def AreaSquare(n): return n*n
def ParameterSquare(n): return 4*n
def AreaRectangle(m,n): return m*n
def ParameterRectangle(m,n): return 2*(m+n)
def AreaCircle(r): return math.pi*r*r
def ParameterCircle(r): return 2*math.pi*r
def PerimeterTriangle(s): return 3*s

# ------------------ Algebra ------------------
def quadratic_solver(a, b, c):
    d = b**2 - 4*a*c
    if d < 0: return "No Real Roots"
    elif d == 0: return [-b/(2*a)]
    else: return [(-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a)]

def linear_solver(a, b):
    if a == 0: return "No Solution"
    return -b/a

# ------------------ Matrix Operations ------------------
def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mul_matrix(A, B):
    result = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k]*B[k][j]
    return result

def determinant_2x2(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def determinant_3x3(matrix):
    return (matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
          - matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
          + matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]))

# ------------------ Converters ------------------
def c_to_f(c): return (c*9/5)+32
def f_to_c(f): return (f-32)*5/9

# ------------------ Advanced Math ------------------
def log_e(x): return math.log(x)
def log10(x): return math.log10(x)
def percentage(part, whole): return (part/whole)*100

# ------------------ Statistics ------------------
def mean(data): return sum(data)/len(data)
def median(data):
    data = sorted(data)
    n = len(data)
    if n%2==0: return (data[n//2-1]+data[n//2])/2
    else: return data[n//2]
def mode(data):
    freq = {}
    for i in data: freq[i] = freq.get(i,0)+1
    return max(freq, key=freq.get)

# ------------------ Trigonometry ------------------
def sine(x): return math.sin(math.radians(x))
def cosine(x): return math.cos(math.radians(x))
def tangent(x): return math.tan(math.radians(x))

# ------------------ Calculator Interface ------------------
def calculator():
    while True:
        print("\n--- Final Calculator ---")
        print("1. Factorial")
        print("2. Square Root")
        print("3. Power")
        print("4. Area of Circle")
        print("5. Quadratic Solver")
        print("6. Temperature Converter (C->F)")
        print("7. Temperature Converter (F->C)")
        print("8. Logarithm (ln)")
        print("9. Logarithm (log10)")
        print("10. Percentage")
        print("11. Matrix Addition")
        print("12. Matrix Subtraction")
        print("13. Matrix Multiplication")
        print("14. Determinant 2x2")
        print("15. Determinant 3x3")
        print("16. Mean")
        print("17. Median")
        print("18. Mode")
        print("19. Sine")
        print("20. Cosine")
        print("21. Tangent")
        print("0. Exit")

        choice = int(input("Enter choice: "))

        if choice == 0:
            print("Exiting Calculator...")
            break
        elif choice == 1:
            n = int(input("Enter number: "))
            print("Factorial:", fact(n))
        elif choice == 2:
            n = int(input("Enter number: "))
            print("Square Root:", sqrt(n))
        elif choice == 3:
            base = float(input("Enter base: "))
            exp = int(input("Enter exponent: "))
            print("Power:", power(base, exp))
        elif choice == 4:
            r = float(input("Enter radius: "))
            print("Area of Circle:", AreaCircle(r))
        elif choice == 5:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            print("Roots:", quadratic_solver(a, b, c))
        elif choice == 6:
            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", c_to_f(c))
        elif choice == 7:
            f = float(input("Enter Fahrenheit: "))
            print("Celsius:", f_to_c(f))
        elif choice == 8:
            x = float(input("Enter number: "))
            print("ln(x):", log_e(x))
        elif choice == 9:
            x = float(input("Enter number: "))
            print("log10(x):", log10(x))
        elif choice == 10:
            part = float(input("Enter part: "))
            whole = float(input("Enter whole: "))
            print("Percentage:", percentage(part, whole))
        elif choice in [11,12]:
            r = int(input("Rows: "))
            c = int(input("Cols: "))
            print("Matrix A:")
            A = input_matrix(r,c)
            print("Matrix B:")
            B = input_matrix(r,c)
            if choice == 11:
                print("Result (A+B):")
                print_matrix(add_matrix(A,B))
            else:
                print("Result (A-B):")
                print_matrix(sub_matrix(A,B))
        elif choice == 13:
            r1 = int(input("Rows of A: "))
            c1 = int(input("Cols of A: "))
            A = input_matrix(r1,c1)
            r2 = int(input("Rows of B: "))
            c2 = int(input("Cols of B: "))
            if c1 != r2:
                print("Error: Columns of A must equal rows of B")
                continue
            B = input_matrix(r2,c2)
            print("Result (A*B):")
            print_matrix(mul_matrix(A,B))
        elif choice == 14:
            print("Enter 2x2 matrix:")
            M = input_matrix(2,2)
            print("Determinant:", determinant_2x2(M))
        elif choice == 15:
            print("Enter 3x3 matrix:")
            M = input_matrix(3,3)
            print("Determinant:", determinant_3x3(M))
        elif choice == 16:
            data = list(map(float, input("Enter numbers: ").split()))
            print("Mean:", mean(data))
        elif choice == 17:
            data = list(map(float, input("Enter numbers: ").split()))
            print("Median:", median(data))
        elif choice == 18:
            data = list(map(float, input("Enter numbers: ").split()))
            print("Mode:", mode(data))
        elif choice == 19:
            x = float(input("Angle in degrees: "))
            print("Sine:", sine(x))
        elif choice == 20:
            x = float(input("Angle in degrees: "))
            print("Cosine:", cosine(x))
        elif choice == 21:
            x = float(input("Angle in degrees: "))
            print("Tangent:", tangent(x))
        else:
            print("not in choice ..")
            
            
            
calculator()