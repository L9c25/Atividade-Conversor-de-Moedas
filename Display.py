from tkinter import *

root = Tk()
moedas = ['BRL', 'EUR', 'USD', 'ARS', 'GBP', 'CAD', 'CHF', 'JPY', 'AUD', 'CNY']

# Taxas de câmbio com a BRL Sendo a Principal
taxas_cambio = {
    'BRL': 1.0,    # Real brasileiro
    'EUR': 0.18,   # Euro
    'USD': 0.20,   # Dólar americano
    'ARS': 34.00,  # Peso argentino
    'GBP': 0.15,   # Libra esterlina
    'CAD': 0.27,   # Dólar canadense
    'CHF': 0.18,   # Franco suíço
    'JPY': 28.00,  # Iene japonês
    'AUD': 0.30,   # Dólar australiano
    'CNY': 1.40    # Yuan chinês

    #! VERIFICAR A VERACIDADE DAS INFORMAÇOES DO CAMBIO !
}

class Funcs:
    #Funçao que converte o valor da entry para BRL e apos isso converte no cambio desejado.
    def Converter(moeda_origen, moeda_destino, val):
        if moeda_origen == moeda_destino:
            return f'{val:,.2f}'
        # Converte o valor para BRL primeiro
        val_em_brl = val / taxas_cambio[moeda_origen]
        # Converte de BRL para a moeda de destino
        result = val_em_brl * taxas_cambio[moeda_destino]
        return f'{result:,.2f}'

    # Funçao para tranformar o valor da entry em float e caso for um valor valido a jogar para ser convertida.
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
        self.frame()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title('Conversor de Moedas')
        self.root.configure(bg="#484848")
        self.root.geometry('300x200')
        self.root.resizable(True, True)
        self.root.maxsize(width=400, height=180)
        self.root.minsize(width=250, height=135)
    # BACK GROUND
    def frame(self):
        self.frame_1 = Frame(self.root, bg="#484848")
        self.frame_1.place(relwidth=1, relheight=1)

    def botoes(self):
        # Criar a entry do valor
        self.ty_valor = Entry(self.frame_1, bg='#808b96',font=('verdana', 9, 'bold'), fg='white')
        self.ty_valor.place(relx=0.35, y=20, relwidth=0.5, height=25)

        # Drop Down Button 1
        self.TipVar = StringVar(self.frame_1)
        self.Tipv = moedas
        self.TipVar.set('BRL')
        self.popmenu = OptionMenu(self.frame_1, self.TipVar, *self.Tipv)
        # EDITA A APARENCIA DO BUTTON DORPDOWN       
        self.popmenu.config(bg='#808b96', fg='white', activebackground="white", activeforeground="#808b96",  font=('Helvetica', 10, 'bold'))
        # EDITAR A CAIXA DE SLEÇOES
        self.menu = self.popmenu['menu']
        self.menu.config(bg="#808b96", fg="white", activebackground="white", activeforeground="#808b96")
        # POSICIONA O DROPDOWN
        self.popmenu.place(relx=0.1, y=20, relwidth=0.22, height=25)
        

        # Drop Down Button 2
        self.TipVar2 = StringVar(self.frame_1)
        self.Tipv2 = moedas
        self.TipVar2.set('USD')
        self.popmenu2 = OptionMenu(self.frame_1, self.TipVar2, *self.Tipv2)
        self.popmenu2.config(bg='#808b96', fg='white', activebackground="white", activeforeground="#808b96",  font=('Helvetica', 10, 'bold'))
        self.menu2 = self.popmenu2['menu']
        self.menu2.config(bg="#808b96", fg="white", activebackground="white", activeforeground="#808b96")
        self.popmenu2.place(relx=0.1, y=60, relwidth=0.22, height=25)

        # Criando o label do resultado
        self.result = Label(self.frame_1, font=('verdana', 9, 'bold'), fg='white', bg="#808b96", justify="left", anchor="nw")
        self.result.place(relx=0.35, y=60, relwidth=0.5, height=25)

        # Criar o botao Converter
        self.converter = Button(self.frame_1, text='Converter', bd=3, activebackground="#F0F8FF",
                                font=('verdana', 10, 'bold'), command=self.Vfloat)
        self.converter.place(relx=0.35, y=100, relwidth=0.3, height=30)


App()
