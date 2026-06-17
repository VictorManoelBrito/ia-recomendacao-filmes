from tkinter import *
from tkinter import messagebox
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Variáveis globais
X = []
y = []
encoder = LabelEncoder()
modelo = None

# Função para adicionar dados de treinamento
def adicionar_dados():
    try:
        idade = int(entry_idade.get())
        filmes = int(entry_filmes.get())
        companhia = combo_companhia.get().lower()
        genero = combo_genero.get().lower()

        companhia_cod = 0 if companhia == "sozinho" else 1

        X.append([idade, filmes, companhia_cod])
        y.append(genero)

        lbl_status.config(text=f"Pessoa adicionada! Total: {len(X)}")

        entry_idade.delete(0, END)
        entry_filmes.delete(0, END)

    except:
        messagebox.showerror("Erro", "Preencha os campos corretamente!")

# Função para treinar a IA
def treinar():
    global modelo

    if len(X) < 3:
        messagebox.showwarning("Aviso", "Cadastre pelo menos 3 pessoas!")
        return

    y_codificado = encoder.fit_transform(y)

    modelo = DecisionTreeClassifier()
    modelo.fit(X, y_codificado)

    messagebox.showinfo("Sucesso", "IA treinada com sucesso!")

# Função para prever
def prever():
    global modelo

    if modelo is None:
        messagebox.showwarning("Aviso", "Treine a IA primeiro!")
        return

    try:
        idade = int(entry_teste_idade.get())
        filmes = int(entry_teste_filmes.get())
        companhia = combo_teste_companhia.get().lower()

        companhia_cod = 0 if companhia == "sozinho" else 1

        previsao_cod = modelo.predict([[idade, filmes, companhia_cod]])[0]
        previsao = encoder.inverse_transform([previsao_cod])[0]

        lbl_resultado.config(
            text=f"Gênero previsto: {previsao}"
        )

    except:
        messagebox.showerror("Erro", "Preencha os dados corretamente!")

# Janela principal
janela = Tk()
janela.title("Sistema de Recomendação de Filmes")
janela.geometry("500x500")

# Cadastro
Label(janela, text="DADOS DE TREINAMENTO").pack()

Label(janela, text="Idade").pack()
entry_idade = Entry(janela)
entry_idade.pack()

Label(janela, text="Filmes por semana").pack()
entry_filmes = Entry(janela)
entry_filmes.pack()

Label(janela, text="Companhia").pack()
combo_companhia = StringVar(value="sozinho")
OptionMenu(janela, combo_companhia, "sozinho", "acompanhado").pack()

Label(janela, text="Gênero favorito").pack()
combo_genero = StringVar(value="ação")
OptionMenu(janela, combo_genero, "ação", "comédia", "drama").pack()

Button(janela, text="Adicionar Pessoa", command=adicionar_dados).pack(pady=10)

Button(janela, text="Treinar IA", command=treinar).pack()

lbl_status = Label(janela, text="")
lbl_status.pack()

# Teste
Label(janela, text="\nTESTAR IA").pack()

Label(janela, text="Idade").pack()
entry_teste_idade = Entry(janela)
entry_teste_idade.pack()

Label(janela, text="Filmes por semana").pack()
entry_teste_filmes = Entry(janela)
entry_teste_filmes.pack()

Label(janela, text="Companhia").pack()
combo_teste_companhia = StringVar(value="sozinho")
OptionMenu(janela, combo_teste_companhia,
           "sozinho", "acompanhado").pack()

Button(janela, text="Prever Gênero", command=prever).pack(pady=10)

lbl_resultado = Label(janela, text="", font=("Arial", 12, "bold"))
lbl_resultado.pack()

janela.mainloop()