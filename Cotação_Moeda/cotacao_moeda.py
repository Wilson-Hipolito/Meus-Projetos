"""Script Para acompanhar a cotação das moedas."""
import requests
from tkinter import *


def pegar_cotações():
    requisicao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotação_btc = requisicao_dic["BTCBRL"]["bid"]

    texto = f'''
    Dólar = {cotacao_dolar}
    Euro = {cotacao_euro}
    Bitcoin = {cotação_btc}'''

    texto_cotacoes['text'] = texto

janela = Tk()
janela.title("Cotação Atual Das Moedas")

texto_orientacoes = Label(janela, text="Clique no botão para ver as cotações das moedas.")
texto_orientacoes.grid(column=0, row=0, padx=20, pady=20)

botao = Button(janela, text="Clique Aqui", command=pegar_cotações)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
