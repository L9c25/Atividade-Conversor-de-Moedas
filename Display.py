from tkinter import *
from PIL import Image, ImageTk
import requests


# Array com todas as moedas que vamos utilizar // Array que armazena as cotações
moedas = ['BRL', 'USD', 'EUR', 'ARS', 'GBP', 'CAD', 'CHF', 'JPY', 'AUD', 'CNY']
cot = []

# Fazendo a requisiçao de todas as moedas
req = requests.get(f"https://economia.awesomeapi.com.br/json/last/BRL-EUR,BRL-USD,BRL-ARS,BRL-GBP,BRL-CAD,BRL-CHF,BRL-JPY,BRL-AUD,BRL-CNY")

for moeda in moedas:
	if moeda != 'BRL':
		cotacao = (req.json()[('BRL' + moeda)]['bid'])
		cotacao = round(float(cotacao), 2)
		cot.append(cotacao)

#? Taxas de câmbio com a BRL Sendo a Principal
taxas_cambio = {
    'BRL': 1.0,    #? Real brasileiro
    'USD': cot[0], #? Dólar americano
    'EUR': cot[1], #? Euro
    'ARS': cot[2], #? Peso argentino
    'GBP': cot[3], #? Libra esterlina
    'CAD': cot[4], #? Dólar canadense
    'CHF': cot[5], #? Franco suíço
    'JPY': cot[6], #? Iene japonês
    'AUD': cot[7], #? Dólar australiano
    'CNY': cot[8]  #? Yuan chinês
}

root = Tk()

class Funcs:
    #* Funçao que converte o valor da entry para BRL e apos isso converte no cambio desejado.
    def Converter(moeda_origen, moeda_destino, val):
        if moeda_origen == moeda_destino:
            return f'{val:,.2f}'
        #* Converte o valor para BRL primeiro
        val_em_brl = val / taxas_cambio[moeda_origen]
        #* Converte de BRL para a moeda de destino
        result = val_em_brl * taxas_cambio[moeda_destino]
        return f'{result:,.2f}'

    #* Funçao para tranformar o valor da entry em float e caso for um valor valido a jogar para ser convertida.
    def Vfloat(self):
        val = str(self.ty_valor.get()).replace(',', '.').replace(' ', '')
        try:
            val = float(val)
        except (ValueError, TypeError):
            self.ty_valor.delete(0, END)
            self.result.configure(text='Erro: Valor invalido.')
        else:
            self.selecao1 = self.TipVar.get()
            self.selecao2 = self.TipVar2.get()
            convertido = Funcs.Converter(self.selecao1, self.selecao2, val)
            self.result.configure(text=f'{convertido}')


class App(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.background()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title('Conversor de Moedas')
        self.root.geometry('300x180')
        self.root.resizable(False, False)

    def background(self):
        # Carregar e redimensionar a imagem com Pillow
        self.img_original = Image.open("bg.png")
        self.img_resized = self.img_original.resize((1000, 280), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img_resized)
        
        self.Background = Label(self.root, image=self.img)
        self.Background.place(x=0, y=0, relwidth=1, relheight=1)

    def botoes(self):
        #* Criar a entry do valor
        self.ty_valor = Entry(self.root, bg='#fff8d7',font=('verdana', 9, 'bold'), fg='black')
        self.ty_valor.place(relx=0.35, y=20, relwidth=0.5, height=25)


        #* Drop Down Button 1
        self.TipVar = StringVar(self.root)
        self.Tipv = moedas
        self.TipVar.set('BRL')
        self.popmenu = OptionMenu(self.root, self.TipVar, *self.Tipv)
        #* EDITA A APARENCIA DO BUTTON DORPDOWN       
        self.popmenu.config(bg='#ffcd69', fg='black', activebackground="#efbd59", activeforeground="black",  font=('Helvetica', 10, 'bold'))
        #* EDITAR A CAIXA DE SLEÇOES
        self.menu = self.popmenu['menu']
        self.menu.config(bg="#ffcd69", fg="black", activebackground="#ffffff", activeforeground="black")
        #* POSICIONA O MENU DE SELEÇÃO
        self.popmenu.place(relx=0.1, y=20, relwidth=0.22, height=25)
        

        #* Drop Down Button 2
        self.TipVar2 = StringVar(self.root)
        self.Tipv2 = moedas
        self.TipVar2.set('USD')
        #* EDITA A APARENCIA DO BUTTON DORPDOWN       
        self.popmenu2 = OptionMenu(self.root, self.TipVar2, *self.Tipv2)
        self.popmenu2.config(bg='#ffcd69', fg='black', activebackground="#efbd59", activeforeground="black",  font=('Helvetica', 10, 'bold'))
        self.menu2 = self.popmenu2['menu']
        #* EDITAR CAIXA DE SELEÇÃO
        self.menu2.config(bg="#ffcd69", fg="black", activebackground="#ffffff", activeforeground="black")
        #* POSICIONA O MENU DE SELEÇÃO
        self.popmenu2.place(relx=0.1, y=60, relwidth=0.22, height=25)



        #* Criando o label do resultado
        self.result = Label(self.root, font=('verdana', 9, 'bold'), fg='black', bg="#fff8d7", justify="left", anchor="nw")
        self.result.place(relx=0.35, y=60, relwidth=0.5, height=25)

        #* Criar o botao Converter
        self.converter = Button(self.root, text='Converter',bg="#fff8d7", bd=3, activebackground="#fff0a6",
                                font=('verdana', 10, 'bold'), command=self.Vfloat)
        self.converter.place(relx=0.35, y=100, relwidth=0.3, height=30)


App()
