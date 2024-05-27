import json
import os
import customtkinter
from datetime import datetime

# Classe Ovelha
class Ovelha:
    def __init__(self, id_ovelha, idade, sexo, peso, raca, finalidade, vacinas=None, tratamentos=None, doencas=None, observacoes=None):
        self.id_ovelha = id_ovelha
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.raca = raca
        self.finalidade = finalidade
        self.vacinas = vacinas if vacinas is not None else []
        self.tratamentos = tratamentos if tratamentos is not None else []
        self.doencas = doencas if doencas is not None else []
        self.observacoes = observacoes if observacoes is not None else []

    def vacinacao(self, vacina, data):
        self.vacinas.append({"vacina": vacina, "data": data})

    def tratamento(self, tratamento, data):
        self.tratamentos.append({"tratamento": tratamento, "data": data})

    def doenca(self, doenca, data):
        self.doencas.append({"doenca": doenca, "data": data})

    def definir_finalidade(self, finalidade):
        self.finalidade = finalidade

    def observacao(self, observacao, data):
        self.observacoes.append({"observacao": observacao, "data": data})

    def to_dict(self):
        return {
            "id_ovelha": self.id_ovelha,
            "idade": self.idade,
            "sexo": self.sexo,
            "peso": self.peso,
            "raca": self.raca,
            "finalidade": self.finalidade,
            "vacinas": self.vacinas,
            "tratamentos": self.tratamentos,
            "doencas": self.doencas,
            "observacoes": self.observacoes
        }

# Função para salvar ovelhas em arquivo JSON
def salvar_ovelhas(ovelhas):
    with open("ovelhas.json", "w") as arquivo:
        json.dump([ovelha.to_dict() for ovelha in ovelhas], arquivo)

# Função para carregar ovelhas de arquivo JSON
def carregar_ovelhas():
    if os.path.exists("ovelhas.json"):
        with open("ovelhas.json", "r") as arquivo:
            return [Ovelha(**data) for data in json.load(arquivo)]
    return []

# Classe Sistema para gerenciar ovelhas
class Sistema:
    def __init__(self):
        self.ovelhas = carregar_ovelhas()

    def adicionar_ovelha(self, ovelha):
        self.ovelhas.append(ovelha)
        salvar_ovelhas(self.ovelhas)

    def exibir_menu(self):
        app = customtkinter.CTk()
        app.geometry("900x600")
        app.title("Sistema de Gerenciamento")

        # Função para adicionar ovelha do menu ao arquivo.json
        def adicionar_ovelha():
            id_ovelha = entry_id.get()
            idade = entry_idade.get()
            sexo = entry_sexo.get()
            peso = entry_peso.get()
            raca = entry_raca.get()
            finalidade = entry_finalidade.get()

            try:
                id_ovelha = int(id_ovelha)
                idade = int(idade)
                peso = int(peso)
            except ValueError:
                customtkinter.CTkMessageBox.show_error(title="Erro", message="ID, Idade e Peso devem ser números inteiros.")
                return

            nova_ovelha = Ovelha(id_ovelha, idade, sexo, peso, raca, finalidade)
            self.adicionar_ovelha(nova_ovelha)
            app.quit()

        # Componentes da interface
        label_id = customtkinter.CTkLabel(app, text="ID da Ovelha")
        label_id.pack(pady=5)
        entry_id = customtkinter.CTkEntry(app)
        entry_id.pack(pady=5)

        label_idade = customtkinter.CTkLabel(app, text="Idade (meses)")
        label_idade.pack(pady=5)
        entry_idade = customtkinter.CTkEntry(app)
        entry_idade.pack(pady=5)

        label_sexo = customtkinter.CTkLabel(app, text="Sexo")
        label_sexo.pack(pady=5)
        entry_sexo = customtkinter.CTkEntry(app)
        entry_sexo.pack(pady=5)

        label_peso = customtkinter.CTkLabel(app, text="Peso (kg)")
        label_peso.pack(pady=5)
        entry_peso = customtkinter.CTkEntry(app)
        entry_peso.pack(pady=5)

        label_raca = customtkinter.CTkLabel(app, text="Raça")
        label_raca.pack(pady=5)
        entry_raca = customtkinter.CTkEntry(app)
        entry_raca.pack(pady=5)

        label_finalidade = customtkinter.CTkLabel(app, text="Finalidade")
        label_finalidade.pack(pady=5)
        entry_finalidade = customtkinter.CTkEntry(app)
        entry_finalidade.pack(pady=5)

        botao_salvar = customtkinter.CTkButton(app, text="Salvar", command=adicionar_ovelha)
        botao_salvar.pack(pady=10)

        botao_sair = customtkinter.CTkButton(app, text="Sair", command=app.quit)
        botao_sair.pack(pady=10)

        app.mainloop()

if __name__ == "__main__":
    sistema = Sistema()
    sistema.exibir_menu()
