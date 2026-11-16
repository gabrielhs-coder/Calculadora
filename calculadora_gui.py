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