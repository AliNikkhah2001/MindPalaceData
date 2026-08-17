import argparse
import math


def parse_function(expr):
    """Parse a mathematical expression string into a callable function."""
    safe_dict = {
        'x': None,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'exp': math.exp,
        'log': math.log,
        'log10': math.log10,
        'sqrt': math.sqrt,
        'pi': math.pi,
        'e': math.e,
        'abs': abs,
    }
    code = compile(expr, '<string>', 'eval')
    for name in code.co_names:
        if name not in safe_dict:
            raise ValueError(f"Disallowed name in expression: {name}")
    return lambda x: eval(code, {"__builtins__": {}}, {**safe_dict, 'x': x})


def riemann_left(f, a, b, n):
    dx = (b - a) / n
    return sum(f(a + i * dx) for i in range(n)) * dx


def riemann_right(f, a, b, n):
    dx = (b - a) / n
    return sum(f(a + (i + 1) * dx) for i in range(n)) * dx


def riemann_midpoint(f, a, b, n):
    dx = (b - a) / n
    return sum(f(a + (i + 0.5) * dx) for i in range(n)) * dx


def trapezoidal(f, a, b, n):
    dx = (b - a) / n
    return (f(a) + f(b)) / 2 * dx + sum(f(a + i * dx) for i in range(1, n)) * dx


def simpson(f, a, b, n):
    if n % 2 != 0:
        n += 1
    dx = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        coeff = 4 if i % 2 == 1 else 2
        total += coeff * f(a + i * dx)
    return total * dx / 3


METHODS = {
    'left': riemann_left,
    'right': riemann_right,
    'midpoint': riemann_midpoint,
    'trapezoidal': trapezoidal,
    'simpson': simpson,
}


def main():
    parser = argparse.ArgumentParser(description='Approximate definite integrals numerically.')
    parser.add_argument('function', type=str, help='Function of x (e.g. "x**2 + sin(x)")')
    parser.add_argument('a', type=float, help='Lower bound of integration')
    parser.add_argument('b', type=float, help='Upper bound of integration')
    parser.add_argument('-n', '--intervals', type=int, default=1000, dest='n', help='Number of intervals (default: 1000)')
    parser.add_argument('-m', '--method', type=str, default='simpson',
                        choices=list(METHODS.keys()), help='Integration method (default: simpson)')
    parser.add_argument('--all', action='store_true', help='Show results for all methods')

    args = parser.parse_args()

    f = parse_function(args.function)

    if args.all:
        print(f"Integrating f(x) = {args.function} from {args.a} to {args.b} with n={args.n}\n")
        print(f"{'Method':<15} {'Result':<25} {'Intervals'}")
        print('-' * 50)
        for name, func in METHODS.items():
            result = func(f, args.a, args.b, args.n)
            print(f"{name:<15} {result:<25.12f} {args.n}")
    else:
        result = METHODS[args.method](f, args.a, args.b, args.n)
        print(f"Method: {args.method}")
        print(f"Integral of f(x) = {args.function} from {args.a} to {args.b}")
        print(f"Result: {result:.12f}")


if __name__ == '__main__':
    main()
