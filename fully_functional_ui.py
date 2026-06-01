
import customtkinter as ctk
from tkinter import messagebox
import numpy as np

from calculator_engine import Basic
from scientific_engine import (
    Trigonometry,
    AdvancedMath,
    VectorOperations,
    MatrixOperations,
    EquationSolver
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class SmartCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Calculator")
        self.geometry("450x650")
        self.resizable(False, False)

        self.basic = Basic()

        self.nav = ctk.CTkFrame(self, width=110)
        self.nav.pack(side="left", fill="y", padx=5, pady=5)

        self.container = ctk.CTkFrame(self)
        self.container.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        self.frames = {}

        pages = [
            ("Basic", BasicPage),
            ("Scientific", ScientificPage),
            ("Vector", VectorPage),
            ("Matrix", MatrixPage),
            ("Equation", EquationPage),
        ]

        for text, page in pages:
            ctk.CTkButton(
                self.nav,
                text=text,
                command=lambda p=page: self.show_frame(p)
            ).pack(fill="x", pady=4, padx=4)

        for _, page in pages:
            frame = page(self.container)
            frame.place(relwidth=1, relheight=1)
            self.frames[page] = frame

        self.show_frame(BasicPage)

    def show_frame(self, page):
        self.frames[page].tkraise()


class BasicPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Basic Calculator", font=("Arial", 20, "bold")).pack(pady=10)

        self.a = ctk.CTkEntry(self, placeholder_text="First Number")
        self.a.pack(pady=5)

        self.b = ctk.CTkEntry(self, placeholder_text="Second Number")
        self.b.pack(pady=5)

        self.result = ctk.CTkTextbox(self, height=100)
        self.result.pack(fill="x", padx=10, pady=10)

        buttons = [
            ("Add", self.add),
            ("Subtract", self.sub),
            ("Multiply", self.mul),
            ("Divide", self.div),
            ("Percentage", self.per)
        ]

        for text, cmd in buttons:
            ctk.CTkButton(self, text=text, command=cmd).pack(pady=3)

    def values(self):
        return float(self.a.get()), float(self.b.get())

    def show(self, value):
        self.result.delete("1.0", "end")
        self.result.insert("end", str(value))

    def add(self):
        a, b = self.values()
        self.show(self.basic.addition(a, b))

    def sub(self):
        a, b = self.values()
        self.show(self.basic.subtraction(a, b))

    def mul(self):
        a, b = self.values()
        self.show(self.basic.multiplication(a, b))

    def div(self):
        a, b = self.values()
        self.show(self.basic.division(a, b))

    def per(self):
        a, b = self.values()
        self.show(self.basic.percentage(a, b))


class ScientificPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Scientific", font=("Arial", 20, "bold")).pack(pady=10)

        self.entry = ctk.CTkEntry(self, placeholder_text="Value")
        self.entry.pack(pady=10)

        self.output = ctk.CTkTextbox(self, height=120)
        self.output.pack(fill="x", padx=10)

        funcs = [
            ("sin", Trigonometry.sin),
            ("cos", Trigonometry.cos),
            ("tan", Trigonometry.tan),
            ("log10", AdvancedMath.log10),
            ("ln", AdvancedMath.ln),
        ]

        for name, func in funcs:
            ctk.CTkButton(
                self,
                text=name,
                command=lambda f=func: self.run(f)
            ).pack(pady=3)

    def run(self, func):
        value = float(self.entry.get())
        result = func(value)
        self.output.delete("1.0", "end")
        self.output.insert("end", str(result))


class VectorPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Vectors", font=("Arial", 20, "bold")).pack(pady=10)

        self.v1 = ctk.CTkEntry(self, placeholder_text="1,2,3")
        self.v1.pack(pady=5)

        self.v2 = ctk.CTkEntry(self, placeholder_text="4,5,6")
        self.v2.pack(pady=5)

        self.output = ctk.CTkTextbox(self, height=120)
        self.output.pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(self, text="Add", command=self.add).pack(pady=2)
        ctk.CTkButton(self, text="Subtract", command=self.sub).pack(pady=2)
        ctk.CTkButton(self, text="Dot Product", command=self.dot).pack(pady=2)
        ctk.CTkButton(self, text="Cross Product", command=self.cross).pack(pady=2)

    def get_vectors(self):
        v1 = np.array(list(map(float, self.v1.get().split(","))))
        v2 = np.array(list(map(float, self.v2.get().split(","))))
        return v1, v2

    def show(self, data):
        self.output.delete("1.0", "end")
        self.output.insert("end", str(data))

    def add(self):
        v1, v2 = self.get_vectors()
        self.show(VectorOperations.add(v1, v2))

    def sub(self):
        v1, v2 = self.get_vectors()
        self.show(VectorOperations.subtract(v1, v2))

    def dot(self):
        v1, v2 = self.get_vectors()
        self.show(VectorOperations.dot_product(v1, v2))

    def cross(self):
        v1, v2 = self.get_vectors()
        self.show(VectorOperations.cross_product(v1, v2))


class MatrixPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Matrix", font=("Arial", 20, "bold")).pack(pady=10)

        ctk.CTkLabel(self, text="Format: 1,2;3,4").pack()

        self.matrix = ctk.CTkEntry(self)
        self.matrix.pack(pady=5)

        self.output = ctk.CTkTextbox(self, height=150)
        self.output.pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(self, text="Determinant", command=self.det).pack(pady=2)
        ctk.CTkButton(self, text="Inverse", command=self.inv).pack(pady=2)
        ctk.CTkButton(self, text="Transpose", command=self.trans).pack(pady=2)
        ctk.CTkButton(self, text="Rank", command=self.rank).pack(pady=2)

    def get_matrix(self):
        rows = self.matrix.get().split(";")
        return np.array([list(map(float, r.split(","))) for r in rows])

    def show(self, data):
        self.output.delete("1.0", "end")
        self.output.insert("end", str(data))

    def det(self):
        self.show(MatrixOperations.determinant(self.get_matrix()))

    def inv(self):
        self.show(MatrixOperations.inverse(self.get_matrix()))

    def trans(self):
        self.show(MatrixOperations.transpose(self.get_matrix()))

    def rank(self):
        self.show(MatrixOperations.rank(self.get_matrix()))


class EquationPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Quadratic Solver", font=("Arial", 20, "bold")).pack(pady=10)

        self.a = ctk.CTkEntry(self, placeholder_text="a")
        self.a.pack(pady=5)

        self.b = ctk.CTkEntry(self, placeholder_text="b")
        self.b.pack(pady=5)

        self.c = ctk.CTkEntry(self, placeholder_text="c")
        self.c.pack(pady=5)

        self.output = ctk.CTkTextbox(self, height=180)
        self.output.pack(fill="x", padx=10, pady=10)

        ctk.CTkButton(self, text="Solve", command=self.solve).pack()

    def solve(self):
        result = EquationSolver.solve_quadratic(
            float(self.a.get()),
            float(self.b.get()),
            float(self.c.get())
        )

        self.output.delete("1.0", "end")
        self.output.insert("end", str(result))


if __name__ == "__main__":
    SmartCalculator().mainloop()
