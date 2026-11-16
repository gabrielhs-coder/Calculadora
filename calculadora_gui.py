import FreeSimpleGUI as sg

OPS = ("+", "-", "*", "/")
MAX_CHARS = 18


def criar_layout():
    sg.theme("DarkBlue3")
    b = {"size": (4, 2), "font": ("Consolas", 13, "bold")}
    calc = [
        [sg.Input("0", key="-DISP-", size=(19, 1), font=("Consolas", 18, "bold"), justification="right", readonly=True)],
        [sg.Button("C", **b), sg.Button("←", **b), sg.Button("Limpar Hist.", key="-CHIST-", size=(10, 2), font=("Consolas", 10, "bold"))],
        [sg.Button("7", **b), sg.Button("8", **b), sg.Button("9", **b), sg.Button("/", **b)],
        [sg.Button("4", **b), sg.Button("5", **b), sg.Button("6", **b), sg.Button("*", **b)],
        [sg.Button("1", **b), sg.Button("2", **b), sg.Button("3", **b), sg.Button("-", **b)],
        [sg.Button("0", **b), sg.Button(".", **b), sg.Button("=", **b), sg.Button("+", **b)],
    ]
    hist = [[sg.Text("Histórico")], [sg.Listbox([], size=(22, 13), key="-HIST-")]]
    return [[sg.Column(calc), sg.VerticalSeparator(), sg.Column(hist)]]


def atualizar_display(win, val):
    win["-DISP-"].update(val)


def tratar_erro(win, msg):
    atualizar_display(win, f"Erro: {msg}")


def adicionar_ao_historico(win, hist, expr, res):
    hist.insert(0, f"{expr} = {res}")
    win["-HIST-"].update(hist[:10])


def calcular(expr):
    if not expr or expr[-1] in OPS or expr[-1] == ".":
        raise ValueError("Expressão inválida")
    try:
        res = eval(expr)
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero")
    except Exception:
        raise ValueError("Expressão inválida")
    if isinstance(res, float):
        res = round(res, 8)
        if res.is_integer():
            res = int(res)
    return str(res)


def main():
    win = sg.Window("Calculadora - INE5201", criar_layout())
    expr, hist, erro = "", [], False

    while True:
        ev, _ = win.read()
        if ev == sg.WIN_CLOSED:
            break
        if ev == "C":
            expr, erro = "", False
            atualizar_display(win, "0")
        elif ev == "-CHIST-":
            hist.clear()
            win["-HIST-"].update(hist)
        elif ev == "←":
            expr = "" if erro else expr[:-1]
            erro = False
            atualizar_display(win, expr or "0")
        elif ev in "0123456789" and (erro or len(expr) < MAX_CHARS):
            expr = ev if (erro or expr == "0") else expr + ev
            erro = False
            atualizar_display(win, expr)
        elif ev == "." and (erro or len(expr) < MAX_CHARS):
            if erro or not expr or expr[-1] in OPS:
                expr, erro = ("0." if erro else expr + "0."), False
            elif "." not in expr.split("+")[-1].split("-")[-1].split("*")[-1].split("/")[-1]:
                expr += "."
            atualizar_display(win, expr)
        elif ev in OPS and not erro:
            if not expr and ev == "-":
                expr = "-"
            elif expr and expr[-1] in OPS and expr != "-":
                expr = expr[:-1] + ev
            elif expr and expr[-1] != "." and len(expr) < MAX_CHARS:
                expr += ev
            atualizar_display(win, expr or "0")
        elif ev == "=" and expr and not erro:
            try:
                res = calcular(expr)
                adicionar_ao_historico(win, hist, expr, res)
                atualizar_display(win, res)
                expr = res
            except (ZeroDivisionError, ValueError) as e:
                tratar_erro(win, str(e))
                expr, erro = "", True

    win.close()


if __name__ == "__main__":
    main()