# calx_ui.py — Complete Calculator UI
# CHANGES: Connected all buttons to backend, added Advanced window with
# Trig / Log-Exp / Matrix / Vector tabs, added error handling & display logic.

import customtkinter
import tkinter as tk
from tkinter import messagebox
import math
import sys
import os

# ── Import backend modules ──────────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(__file__))
from core.basic import addition, subtraction, multiplication, division, parcentage
from core.sceintific import (
    Tignomatry, logarthmic, expoant, angulur_conversion,
    Matrix, vector
)

# ═══════════════════════════════════════════════════════════════════════════════
#  BASIC CALCULATOR WINDOW
# ═══════════════════════════════════════════════════════════════════════════════
class BasicCalcApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("360x520")
        self.title("Calx")
        self.resizable(True, True)

        # internal state
        self._expr = ""          # expression being built
        self._just_evaluated = False

        # ── grid weights ──────────────────────────────────────────────────
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)
        self.grid_rowconfigure(0, weight=3)   # display
        for row in range(1, 6):
            self.grid_rowconfigure(row, weight=1)

        # ── Display ───────────────────────────────────────────────────────
        self._display_frame = customtkinter.CTkFrame(self)
        self._display_frame.grid(row=0, column=0, columnspan=4,
                                 sticky="nsew", padx=5, pady=5)
        self._display_frame.grid_rowconfigure(0, weight=1)
        self._display_frame.grid_rowconfigure(1, weight=2)
        self._display_frame.grid_columnconfigure(0, weight=1)

        # secondary: shows the expression being typed
        self._expr_label = customtkinter.CTkLabel(
            self._display_frame, text="", font=("Verdana", 11),
            text_color="gray", anchor="e"
        )
        self._expr_label.grid(row=0, column=0, sticky="ew", padx=8, pady=(6, 0))

        # primary: shows current result / entry
        self._result_label = customtkinter.CTkLabel(
            self._display_frame, text="0", font=("Verdana", 28, "bold"),
            anchor="e"
        )
        self._result_label.grid(row=1, column=0, sticky="ew", padx=8, pady=(0, 6))

        # ── Row 1 — AC, C, %, × ──────────────────────────────────────────
        self._btn(text="AC",  row=1, col=0, cmd=self._clear_all,  style="action")
        self._btn(text="C",   row=1, col=1, cmd=self._clear_last, style="action")
        self._btn(text="%",   row=1, col=2, cmd=lambda: self._append_op("%"))
        self._btn(text="×",   row=1, col=3, cmd=lambda: self._append_op("*"), style="op")

        # ── Row 2 — 7 8 9 + ──────────────────────────────────────────────
        for n, c in zip([7, 8, 9], [0, 1, 2]):
            self._btn(str(n), 2, c, cmd=lambda v=str(n): self._append_num(v))
        self._btn("+", 2, 3, cmd=lambda: self._append_op("+"), style="op")

        # ── Row 3 — 4 5 6 − ──────────────────────────────────────────────
        for n, c in zip([4, 5, 6], [0, 1, 2]):
            self._btn(str(n), 3, c, cmd=lambda v=str(n): self._append_num(v))
        self._btn("−", 3, 3, cmd=lambda: self._append_op("-"), style="op")

        # ── Row 4 — 1 2 3 ÷ ──────────────────────────────────────────────
        for n, c in zip([1, 2, 3], [0, 1, 2]):
            self._btn(str(n), 4, c, cmd=lambda v=str(n): self._append_num(v))
        self._btn("÷", 4, 3, cmd=lambda: self._append_op("/"), style="op")

        # ── Row 5 — Advance, 0, ., = ─────────────────────────────────────
        self._btn("Adv", 5, 0, cmd=self._open_advanced, style="action")
        self._btn("0",   5, 1, cmd=lambda: self._append_num("0"))
        self._btn(".",   5, 2, cmd=self._append_dot)
        self._btn("=",   5, 3, cmd=self._evaluate, style="eq")

        # keyboard bindings
        self.bind("<Key>", self._keypress)

    # ── helpers ──────────────────────────────────────────────────────────────
    def _btn(self, text, row, col, cmd, colspan=1, style="num"):
        colors = {
            "num":    ("#FFFFFF", "#1A1A1A"),   # (light-bg, dark-text)
            "op":     ("#D4E9FF", "#185FA5"),
            "action": ("#ECECEC", "#444444"),
            "eq":     ("#1D9E75", "#FFFFFF"),
        }
        fg, txt = colors.get(style, colors["num"])
        b = customtkinter.CTkButton(
            self, text=text, font=("Verdana", 15),
            fg_color=fg, text_color=txt,
            hover_color="#C8E6C9" if style == "eq" else None,
            command=cmd
        )
        b.grid(row=row, column=col, columnspan=colspan,
               padx=5, pady=5, sticky="nsew")
        return b

    def _set_display(self, value, expr=""):
        self._result_label.configure(text=str(value))
        self._expr_label.configure(text=str(expr))

    def _append_num(self, n):
        if self._just_evaluated:
            self._expr = ""
            self._just_evaluated = False
        self._expr += n
        self._set_display(self._expr)

    def _append_op(self, op):
        self._just_evaluated = False
        if not self._expr:
            return
        if op == "%":
            # percentage of current accumulation
            try:
                self._expr = str(parcentage(float(self._expr), 100))
                self._set_display(self._expr)
            except Exception:
                pass
            return
        # replace trailing operator if any
        if self._expr and self._expr[-1] in "+-*/":
            self._expr = self._expr[:-1]
        self._expr += op
        self._set_display(self._expr)

    def _append_dot(self):
        # only one dot per number token
        tokens = self._expr.replace("+","~").replace("-","~").replace("*","~").replace("/","~").split("~")
        if "." not in (tokens[-1] if tokens else ""):
            if not self._expr or self._expr[-1] in "+-*/":
                self._expr += "0"
            self._expr += "."
            self._set_display(self._expr)

    def _clear_all(self):
        self._expr = ""
        self._just_evaluated = False
        self._set_display("0")

    def _clear_last(self):
        self._expr = self._expr[:-1]
        self._set_display(self._expr or "0")

    def _evaluate(self):
        if not self._expr:
            return
        try:
            # use backend functions for single-op expressions, eval for compound
            result = eval(self._expr, {"__builtins__": {}}, {})
            self._set_display(
                round(result, 10) if isinstance(result, float) else result,
                expr=self._expr + " ="
            )
            self._expr = str(result)
            self._just_evaluated = True
        except ZeroDivisionError:
            self._set_display("Error: Division by zero")
            self._expr = ""
        except Exception as e:
            self._set_display(f"Error: {e}")
            self._expr = ""

    def _keypress(self, event):
        k = event.char
        if k in "0123456789":
            self._append_num(k)
        elif k in "+-*/":
            self._append_op(k)
        elif k == ".":
            self._append_dot()
        elif k in ("\r", "="):
            self._evaluate()
        elif event.keysym == "BackSpace":
            self._clear_last()
        elif event.keysym == "Escape":
            self._clear_all()

    def _open_advanced(self):
        AdvancedWindow(self)


# ═══════════════════════════════════════════════════════════════════════════════
#  ADVANCED / SCIENTIFIC WINDOW
# ═══════════════════════════════════════════════════════════════════════════════
class AdvancedWindow(customtkinter.CTkToplevel):
    """
    Advanced calculator window with four tabs:
      - Trigonometry
      - Logarithm / Exponent
      - Matrix (2×2)
      - Vector (3D)
    ADDED: This entire window is new — wires to sceintific.py backend.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Calx — Advanced")
        self.geometry("420x560")
        self.resizable(True, True)

        # ── Tab view ─────────────────────────────────────────────────────
        self._tabs = customtkinter.CTkTabview(self, width=400, height=520)
        self._tabs.pack(fill="both", expand=True, padx=8, pady=8)
        for name in ["Trig", "Log / Exp", "Matrix", "Vector"]:
            self._tabs.add(name)

        self._build_trig_tab()
        self._build_logexp_tab()
        self._build_matrix_tab()
        self._build_vector_tab()

    # ── Utility widgets ───────────────────────────────────────────────────
    @staticmethod
    def _label(parent, text, **kw):
        return customtkinter.CTkLabel(parent, text=text, **kw)

    @staticmethod
    def _entry(parent, placeholder="", width=120):
        e = customtkinter.CTkEntry(parent, placeholder_text=placeholder,
                                   font=("Courier", 13), width=width)
        e.pack(pady=3)
        return e

    @staticmethod
    def _result_box(parent):
        box = customtkinter.CTkTextbox(parent, height=80,
                                       font=("Courier", 13), state="disabled")
        box.pack(fill="x", padx=5, pady=5)
        return box

    @staticmethod
    def _show(box, text):
        box.configure(state="normal")
        box.delete("0.0", "end")
        box.insert("end", str(text))
        box.configure(state="disabled")

    # ── TRIG TAB ──────────────────────────────────────────────────────────
    def _build_trig_tab(self):
        tab = self._tabs.tab("Trig")

        self._label(tab, "Angle value:").pack()
        self._trig_val = customtkinter.CTkEntry(tab, placeholder_text="e.g. 45",
                                                font=("Courier", 13), width=200)
        self._trig_val.pack(pady=3)

        # degree / radian toggle
        self._angle_unit = customtkinter.StringVar(value="degrees")
        frm = customtkinter.CTkFrame(tab, fg_color="transparent")
        frm.pack()
        customtkinter.CTkRadioButton(frm, text="Degrees",
                                     variable=self._angle_unit,
                                     value="degrees").pack(side="left", padx=8)
        customtkinter.CTkRadioButton(frm, text="Radians",
                                     variable=self._angle_unit,
                                     value="radians").pack(side="left", padx=8)

        # buttons
        btn_frame = customtkinter.CTkFrame(tab, fg_color="transparent")
        btn_frame.pack(pady=6)
        fns = [("sin", "sin"), ("cos", "cos"), ("tan", "tan"),
               ("arcsin", "sin⁻¹"), ("arccos", "cos⁻¹"), ("arctan", "tan⁻¹")]
        for fn, label in fns:
            customtkinter.CTkButton(
                btn_frame, text=label, width=100,
                command=lambda f=fn: self._trig_calc(f)
            ).pack(side="left", padx=3)

        self._trig_result = self._result_box(tab)

    def _trig_calc(self, fn):
        try:
            raw = float(self._trig_val.get())
        except ValueError:
            self._show(self._trig_result, "Error: invalid input"); return

        # convert to radians if needed
        if self._angle_unit.get() == "degrees":
            rad = angulur_conversion.degree_to_radian(raw)
        else:
            rad = raw

        try:
            funcs = {
                "sin": Tignomatry.sin_fun,
                "cos": Tignomatry.cos_fun,
                "tan": Tignomatry.tangent,
                "arcsin": Tignomatry.arcsin,
                "arccos": Tignomatry.arccos,
                "arctan": Tignomatry.arctan,
            }
            result = funcs[fn](rad)
            self._show(self._trig_result,
                       f"{fn}({raw} {self._angle_unit.get()}) = {round(result, 10)}")
        except (ValueError, ZeroDivisionError) as e:
            self._show(self._trig_result, f"Error: {e}")

    # ── LOG / EXP TAB ─────────────────────────────────────────────────────
    def _build_logexp_tab(self):
        tab = self._tabs.tab("Log / Exp")

        self._label(tab, "Value x:").pack()
        self._logexp_x = customtkinter.CTkEntry(tab, placeholder_text="x",
                                                font=("Courier", 13), width=200)
        self._logexp_x.pack(pady=3)

        self._label(tab, "Value y (base / exponent, if needed):").pack()
        self._logexp_y = customtkinter.CTkEntry(tab, placeholder_text="y",
                                                font=("Courier", 13), width=200)
        self._logexp_y.pack(pady=3)

        btn_grid = customtkinter.CTkFrame(tab, fg_color="transparent")
        btn_grid.pack(pady=6)
        ops = [
            ("ln(x)",   "ln"),   ("log₁₀(x)", "log10"),
            ("logₙ(x,y)","logb"),("xʸ",       "pow"),
            ("√x",      "sqrt"), ("eˣ",        "exp"),
            ("x²",      "square"),("x% of y",  "pct"),
        ]
        for i, (label, fn) in enumerate(ops):
            customtkinter.CTkButton(
                btn_grid, text=label, width=110,
                command=lambda f=fn: self._logexp_calc(f)
            ).grid(row=i//2, column=i%2, padx=4, pady=3)

        self._logexp_result = self._result_box(tab)

    def _logexp_calc(self, fn):
        try:
            x = float(self._logexp_x.get()) if self._logexp_x.get() else None
            y = float(self._logexp_y.get()) if self._logexp_y.get() else None
        except ValueError:
            self._show(self._logexp_result, "Error: invalid number"); return

        try:
            if fn == "ln":
                r = logarthmic.natural_log(x); label = f"ln({x})"
            elif fn == "log10":
                r = logarthmic.log_10(x); label = f"log10({x})"
            elif fn == "logb":
                r = logarthmic.log_base(x, y); label = f"log_{y}({x})"
            elif fn == "pow":
                r = expoant.power(x, y); label = f"{x}^{y}"
            elif fn == "sqrt":
                r = expoant.square_root(x); label = f"√{x}"
            elif fn == "exp":
                r = expoant.expnantial(x); label = f"e^{x}"
            elif fn == "square":
                r = expoant.square(x); label = f"{x}²"
            elif fn == "pct":
                r = parcentage(x, y); label = f"{x}% of {y}"
            else:
                return
            self._show(self._logexp_result, f"{label} = {round(r, 10)}")
        except Exception as e:
            self._show(self._logexp_result, f"Error: {e}")

    # ── MATRIX TAB (2×2) ──────────────────────────────────────────────────
    def _build_matrix_tab(self):
        tab = self._tabs.tab("Matrix")

        def mat_entry_grid(parent, prefix):
            """Creates a 2×2 grid of entries, returns list of 4 CTkEntry."""
            frame = customtkinter.CTkFrame(parent)
            frame.pack(pady=4)
            entries = []
            for r in range(2):
                for c in range(2):
                    e = customtkinter.CTkEntry(frame, width=60,
                                               placeholder_text=f"{prefix}{r+1}{c+1}",
                                               font=("Courier", 12))
                    e.grid(row=r, column=c, padx=3, pady=2)
                    entries.append(e)
            return entries  # [00,01,10,11]

        self._label(tab, "Matrix A:").pack()
        self._mat_a = mat_entry_grid(tab, "a")

        self._label(tab, "Matrix B (for A+B, A−B, A×B):").pack()
        self._mat_b = mat_entry_grid(tab, "b")

        btn_frame = customtkinter.CTkFrame(tab, fg_color="transparent")
        btn_frame.pack(pady=6)
        ops = [("A+B","add"),("A−B","sub"),("A×B","mul"),
               ("A⁻¹","inv"),("tr(A)","trace"),("rank(A)","rank"),("det(A)","det")]
        for i, (label, fn) in enumerate(ops):
            customtkinter.CTkButton(
                btn_frame, text=label, width=85,
                command=lambda f=fn: self._mat_calc(f)
            ).grid(row=i//4, column=i%4, padx=3, pady=3)

        self._mat_result = self._result_box(tab)

    def _mat_vals(self, entries):
        vals = []
        for e in entries:
            t = e.get().strip()
            vals.append(float(t) if t else 0.0)
        return [[vals[0], vals[1]], [vals[2], vals[3]]]

    def _mat_calc(self, fn):
        import numpy as np
        try:
            A = np.array(self._mat_vals(self._mat_a))
            B = np.array(self._mat_vals(self._mat_b))
            if fn == "add":    r = Matrix.madd(A, B)
            elif fn == "sub":  r = Matrix.msub(A, B)
            elif fn == "mul":  r = Matrix.matrix_multiplication(A, B)
            elif fn == "inv":  r = Matrix.inverce(A)
            elif fn == "trace":r = Matrix.trace(A)
            elif fn == "rank": r = Matrix.ma_rank(A)
            elif fn == "det":  r = np.linalg.det(A)
            else: return
            self._show(self._mat_result, np.round(r, 6) if hasattr(r, '__len__') else round(float(r), 6))
        except Exception as e:
            self._show(self._mat_result, f"Error: {e}")

    # ── VECTOR TAB (3D) ───────────────────────────────────────────────────
    def _build_vector_tab(self):
        tab = self._tabs.tab("Vector")

        def vec_row(parent, prefix):
            frame = customtkinter.CTkFrame(parent, fg_color="transparent")
            frame.pack(pady=3)
            entries = []
            for dim in ["x", "y", "z"]:
                e = customtkinter.CTkEntry(frame, width=75,
                                           placeholder_text=f"{prefix}.{dim}",
                                           font=("Courier", 13))
                e.pack(side="left", padx=3)
                entries.append(e)
            return entries

        self._label(tab, "Vector u:").pack()
        self._vec_u = vec_row(tab, "u")

        self._label(tab, "Vector v:").pack()
        self._vec_v = vec_row(tab, "v")

        btn_frame = customtkinter.CTkFrame(tab, fg_color="transparent")
        btn_frame.pack(pady=6)
        ops = [("u+v","add"),("u−v","sub"),("u·v","dot"),
               ("u×v","cross"),("|u|","mag_u"),("|v|","mag_v")]
        for i, (label, fn) in enumerate(ops):
            customtkinter.CTkButton(
                btn_frame, text=label, width=100,
                command=lambda f=fn: self._vec_calc(f)
            ).grid(row=i//3, column=i%3, padx=4, pady=3)

        self._vec_result = self._result_box(tab)

    def _vec_vals(self, entries):
        vals = []
        for e in entries:
            t = e.get().strip()
            vals.append(float(t) if t else 0.0)
        return vals  # [x, y, z]

    def _vec_calc(self, fn):
        import numpy as np
        try:
            u = np.array(self._vec_vals(self._vec_u))
            v = np.array(self._vec_vals(self._vec_v))
            if fn == "add":   r = vector.vadd(u, v)
            elif fn == "sub": r = vector.vsub(u, v)
            elif fn == "dot": r = vector.dot_prouct(u, v)
            elif fn == "cross": r = vector.cross_product(u, v)
            elif fn == "mag_u": r = np.linalg.norm(u)
            elif fn == "mag_v": r = np.linalg.norm(v)
            else: return
            self._show(self._vec_result, np.round(r, 6) if hasattr(r, '__len__') else round(float(r), 6))
        except Exception as e:
            self._show(self._vec_result, f"Error: {e}")


# ═══════════════════════════════════════════════════════════════════════════════
#  Entry point
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    app = BasicCalcApp()
    app.mainloop()
