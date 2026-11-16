# Calculadora com Interface Gráfica

Projeto desenvolvido para a **Tarefa 02** da disciplina de Introdução à Ciência da Computação com Python (UFSC).

## Funcionalidades Implementadas
- **Interface Gráfica (`FreeSimpleGUI`):** Layout estilo calculadora física com visor bloqueado para edição direta, botões numéricos (`0-9`), decimais (`.`), operações básicas (`+`, `-`, `*`, `/`), igual (`=`), limpar (`C`) e apagar último caractere (`←`).
- **Histórico de Cálculos:** Painel lateral que armazena os últimos cálculos realizados (suportando mais de 5 registros recentes) com botão dedicado para limpar o histórico.
- **Tratamento de Erros e Validações:**
  - Divisão por zero exibe `"Erro: Divisão por zero"`.
  - Expressões incompletas ou inválidas exibem `"Erro: Expressão inválida"`.
  - Prevenção contra múltiplos operadores consecutivos e múltiplos pontos decimais no mesmo número.
  - Controle de limite de caracteres no display (*display overflow*).

## Como Executar
1. Certifique-se de ter o Python 3 instalado.
2. Instale a dependência:
   pip install FreeSimpleGUI

Durante o desenvolvimento no VS Code, o GitHub Copilot foi utilizado como ferramenta de apoio nas seguintes funções:

criar_layout: Sugestão da estrutura de colunas e estilização dos botões para alinhar o teclado numérico ao lado da sg.Listbox do histórico.

validar_ponto: Auxílio na lógica de percorrer a string da expressão de trás para frente até encontrar um operador para impedir dois pontos decimais no mesmo operando.

calcular: Refinamento do tratamento de exceções (ZeroDivisionError e ValueError) e formatação de números inteiros/decimais arredondados para evitar imprecisões de ponto flutuante.