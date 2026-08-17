import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.patches import Polygon
import sympy
from sympy.parsing.latex import parse_latex
from sympy import lambdify, Symbol, integrate, latex, Rational


class IntegralApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Integral Calculator")
        self.root.geometry("1000x750")
        self.root.configure(bg="#1e1e2e")

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#1e1e2e')
        self.style.configure('TLabel', background='#1e1e2e', foreground='#cdd6f4', font=('Segoe UI', 10))
        self.style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=8)
        self.style.configure('Header.TLabel', font=('Segoe UI', 16, 'bold'), foreground='#89b4fa')
        self.style.configure('Result.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#a6e3a1')
        self.style.configure('TLabelframe', background='#1e1e2e', foreground='#89b4fa')
        self.style.configure('TLabelframe.Label', background='#1e1e2e', foreground='#89b4fa', font=('Segoe UI', 10, 'bold'))

        self._build_ui()

    def _build_ui(self):
        header = ttk.Label(self.root, text="∫ Integral Calculator", style='Header.TLabel')
        header.pack(pady=(15, 5))

        subtitle = ttk.Label(self.root, text="Enter a function in LaTeX format (e.g. x^2, \\sin(x), \\frac{1}{x}, \\sqrt{x^2+1})")
        subtitle.pack(pady=(0, 10))

        # Input frame
        input_frame = ttk.LabelFrame(self.root, text="Input", padding=10)
        input_frame.pack(fill=tk.X, padx=20, pady=5)

        ttk.Label(input_frame, text="f(x) =").grid(row=0, column=0, padx=5)
        self.func_entry = ttk.Entry(input_frame, width=50, font=('Consolas', 12))
        self.func_entry.grid(row=0, column=1, padx=5, sticky='ew')
        self.func_entry.insert(0, "x^2")
        self.func_entry.bind('<Return>', self.on_keypress)

        bounds_frame = ttk.Frame(input_frame)
        bounds_frame.grid(row=1, column=0, columnspan=3, pady=10)

        ttk.Label(bounds_frame, text="From a =").grid(row=0, column=0, padx=5)
        self.a_entry = ttk.Entry(bounds_frame, width=10, font=('Consolas', 12))
        self.a_entry.grid(row=0, column=1, padx=5)
        self.a_entry.insert(0, "0")

        ttk.Label(bounds_frame, text="To b =").grid(row=0, column=2, padx=5)
        self.b_entry = ttk.Entry(bounds_frame, width=10, font=('Consolas', 12))
        self.b_entry.grid(row=0, column=3, padx=5)
        self.b_entry.insert(0, "1")

        ttk.Label(bounds_frame, text="Intervals n =").grid(row=0, column=4, padx=5)
        self.n_entry = ttk.Entry(bounds_frame, width=10, font=('Consolas', 12))
        self.n_entry.grid(row=0, column=5, padx=5)
        self.n_entry.insert(0, "100")

        # Method selection
        method_frame = ttk.Frame(input_frame)
        method_frame.grid(row=2, column=0, columnspan=3, pady=5)

        ttk.Label(method_frame, text="Method:").grid(row=0, column=0, padx=5)
        self.method_var = tk.StringVar(value='simpson')
        methods = ['simpson', 'trapezoidal', 'midpoint', 'left', 'right']
        self.method_combo = ttk.Combobox(method_frame, textvariable=self.method_var,
                                         values=methods, state='readonly', width=15)
        self.method_combo.grid(row=0, column=1, padx=5)

        # Buttons
        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=3, column=0, columnspan=3, pady=10)

        self.calc_btn = ttk.Button(btn_frame, text="Calculate", command=self.calculate)
        self.calc_btn.grid(row=0, column=0, padx=5)

        self.exact_btn = ttk.Button(btn_frame, text="Exact Integral", command=self.calc_exact)
        self.exact_btn.grid(row=0, column=1, padx=5)

        self.example_btn = ttk.Button(btn_frame, text="Load Example", command=self.load_example)
        self.example_btn.grid(row=0, column=2, padx=5)

        input_frame.columnconfigure(1, weight=1)

        # Result label
        self.result_label = ttk.Label(self.root, text="", style='Result.TLabel', wraplength=900)
        self.result_label.pack(pady=5)

        # Plot frame
        plot_frame = ttk.Frame(self.root)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.fig = Figure(figsize=(9, 5), dpi=100, facecolor='#1e1e2e')
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('#1e1e2e')
        self.ax.tick_params(colors='#cdd6f4')
        self.ax.xaxis.label.set_color('#cdd6f4')
        self.ax.yaxis.label.set_color('#cdd6f4')
        self.ax.title.set_color('#89b4fa')
        for spine in self.ax.spines.values():
            spine.set_color('#45475a')

        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        toolbar_frame = ttk.Frame(plot_frame)
        toolbar_frame.pack(fill=tk.X)
        self.toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        self.toolbar.update()

    def parse_latex_input(self, expr_str):
        import re
        expr_str = expr_str.strip()
        expr_str = expr_str.strip('$')

        try:
            sympy_expr = parse_latex(expr_str)
            return sympy_expr
        except Exception:
            pass

        s = expr_str

        s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'((\1)/(\2))', s)
        s = re.sub(r'\\sqrt\{([^}]+)\}', r'sqrt(\1)', s)
        s = re.sub(r'\\sqrt\[([^]]+)\]\{([^}]+)\}', r'((\2) ** (1/(\1)))', s)

        s = re.sub(r'\\(sin|cos|tan|cot|sec|csc|arcsin|arccos|arctan|sinh|cosh|tanh)', r'\1', s)
        s = re.sub(r'\\(ln|lg|exp|log)', r'\1', s)
        s = re.sub(r'\\(pi|infty)', r'\1', s)

        s = s.replace('^', '**')
        s = s.replace('\\', '')

        known_funcs = {'sin', 'cos', 'tan', 'cot', 'sec', 'csc',
                       'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh',
                       'sqrt', 'log', 'ln', 'lg', 'exp', 'abs'}

        s = re.sub(r'(\d)([a-zA-Z(])', r'\1*\2', s)
        s = re.sub(r'(\))(\d|[a-zA-Z(])', r'\1*\2', s)
        s = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', s)
        s = re.sub(r'([a-zA-Z\d])\s+([a-zA-Z])', r'\1*\2', s)
        s = re.sub(r'\)\s*\(', r')*(', s)

        s = s.replace('infty', 'oo')

        x = Symbol('x')
        local_dict = {
            'sin': sympy.sin, 'cos': sympy.cos, 'tan': sympy.tan,
            'cot': sympy.cot, 'sec': sympy.sec, 'csc': sympy.csc,
            'arcsin': sympy.asin, 'arccos': sympy.acos, 'arctan': sympy.atan,
            'sinh': sympy.sinh, 'cosh': sympy.cosh, 'tanh': sympy.tanh,
            'sqrt': sympy.sqrt, 'log': sympy.log, 'ln': sympy.log,
            'lg': lambda a: sympy.log(a, 10), 'exp': sympy.exp,
            'abs': sympy.Abs, 'pi': sympy.pi, 'oo': sympy.oo,
            'x': x,
        }
        sympy_expr = sympy.sympify(s, locals=local_dict)
        return sympy_expr

    def numerical_integrate(self, f, a, b, n, method):
        dx = (b - a) / n
        xs = np.linspace(a, b, n + 1)
        ys = f(xs)

        if method == 'left':
            return np.sum(ys[:-1]) * dx
        elif method == 'right':
            return np.sum(ys[1:]) * dx
        elif method == 'midpoint':
            mids = (xs[:-1] + xs[1:]) / 2
            return np.sum(f(mids)) * dx
        elif method == 'trapezoidal':
            return np.trapezoid(ys, xs)
        elif method == 'simpson':
            if n % 2 != 0:
                n += 1
                xs = np.linspace(a, b, n + 1)
                ys = f(xs)
            result = ys[0] + ys[-1]
            result += 4 * np.sum(ys[1:-1:2])
            result += 2 * np.sum(ys[2:-1:2])
            return result * dx / 3

    def parse_bound(self, val_str):
        val_str = val_str.strip()
        val_str = val_str.replace('\\pi', str(float(sympy.pi.evalf())))
        val_str = val_str.replace('\\e', str(float(sympy.E.evalf())))
        val_str = val_str.replace('pi', str(float(sympy.pi.evalf())))
        val_str = val_str.replace('\\infty', 'inf')
        val_str = val_str.replace('infty', 'inf')
        return float(val_str)

    def calculate(self):
        try:
            func_str = self.func_entry.get()
            a = self.parse_bound(self.a_entry.get())
            b = self.parse_bound(self.b_entry.get())
            n = int(self.n_entry.get())
            method = self.method_var.get()

            if a >= b:
                messagebox.showerror("Error", "Lower bound 'a' must be less than upper bound 'b'")
                return
            if n < 1:
                messagebox.showerror("Error", "Number of intervals must be positive")
                return

            sympy_expr = self.parse_latex_input(func_str)
            x = Symbol('x')
            f = lambdify(x, sympy_expr, modules=['numpy'])

            result = self.numerical_integrate(f, a, b, n, method)
            latex_str = latex(sympy_expr)

            self.result_label.config(
                text=f"∫ₐᵇ f(x) dx ≈ {result:.10f}  (method: {method}, n={n})"
            )

            self.plot_function(f, a, b, sympy_expr, result, method)

        except Exception as e:
            messagebox.showerror("Error", f"Could not parse or compute:\n{e}")

    def calc_exact(self):
        try:
            func_str = self.func_entry.get()
            a = self.parse_bound(self.a_entry.get())
            b = self.parse_bound(self.b_entry.get())

            sympy_expr = self.parse_latex_input(func_str)
            x = Symbol('x')
            exact = integrate(sympy_expr, (x, a, b))
            exact_val = float(exact.evalf())
            latex_str = latex(sympy_expr)
            exact_latex = latex(exact)

            self.result_label.config(
                text=f"Exact: ∫ₐᵇ f(x) dx = {exact_latex} = {exact_val:.12f}"
            )

        except Exception as e:
            messagebox.showerror("Error", f"Could not compute exact integral:\n{e}")

    def plot_function(self, f, a, b, sympy_expr, result, method):
        self.ax.clear()
        self.ax.set_facecolor('#1e1e2e')

        x_fine = np.linspace(a, b, 1000)
        y_fine = f(x_fine)

        self.ax.plot(x_fine, y_fine, color='#89b4fa', linewidth=2, label=f'$f(x) = {latex(sympy_expr)}$')

        n = int(self.n_entry.get())
        n = min(n, 200)
        x_trap = np.linspace(a, b, n + 1)
        y_trap = f(x_trap)

        self.ax.fill_between(x_trap, y_trap, alpha=0.25, color='#a6e3a1', step=None)

        for i in range(n):
            xs = [x_trap[i], x_trap[i], x_trap[i + 1], x_trap[i + 1]]
            ys = [0, y_trap[i], y_trap[i + 1], 0]
            color = '#a6e3a1' if (y_trap[i] + y_trap[i + 1]) / 2 >= 0 else '#f38ba8'
            self.ax.fill(xs, ys, alpha=0.15, color=color, edgecolor='#a6e3a1', linewidth=0.5)

        self.ax.axhline(y=0, color='#cdd6f4', linewidth=0.8, alpha=0.5)
        self.ax.axvline(x=0, color='#cdd6f4', linewidth=0.8, alpha=0.5)

        self.ax.set_xlabel('x', color='#cdd6f4')
        self.ax.set_ylabel('f(x)', color='#cdd6f4')
        self.ax.set_title(f'Approximate integral = {result:.8f} ({method})', color='#89b4fa')
        self.ax.legend(loc='upper right', facecolor='#313244', edgecolor='#45475a', labelcolor='#cdd6f4')
        self.ax.tick_params(colors='#cdd6f4')
        for spine in self.ax.spines.values():
            spine.set_color('#45475a')

        self.fig.tight_layout()
        self.canvas.draw()

    def load_example(self):
        examples = [
            ("x^2", "0", "1"),
            ("\\sin(x)", "0", "\\pi"),
            ("e^{-x^2}", "-2", "2"),
            ("\\frac{1}{x}", "1", "e"),
            ("x^3 - 3*x", "-2", "2"),
            ("\\sqrt{x}", "0", "4"),
            ("\\frac{1}{1+x^2}", "0", "1"),
            ("x\\sin(x)", "0", "\\pi"),
        ]
        func, a, b = examples[np.random.randint(len(examples))]
        self.func_entry.delete(0, tk.END)
        self.func_entry.insert(0, func)
        self.a_entry.delete(0, tk.END)
        self.a_entry.insert(0, a)
        self.b_entry.delete(0, tk.END)
        self.b_entry.insert(0, b)

    def on_keypress(self, event):
        if event.keysym == 'Return':
            self.calculate()


def main():
    root = tk.Tk()
    app = IntegralApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
