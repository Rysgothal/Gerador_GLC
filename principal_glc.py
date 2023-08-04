from tkinter import *
from tkinter import messagebox
import classe_glc
import funcoes_glc as Funcoes
import arvore_glc as Plot

# Cria o Formulário/Tela
vFormulario = Tk()

vLargura = 950
vAltura = 560
vLarguraTela = vFormulario.winfo_screenwidth()
vAlturaTela = vFormulario.winfo_screenheight()

X = (vLarguraTela // 2) - (vLargura // 2)
Y = (vAlturaTela // 2) - (vAltura // 2)

vFormulario.geometry('{}x{}+{}+{}'.format(vLargura, vAltura, X, Y))
vFormulario.title("\tGerador de Frases com GLC")

#Instancia a Classe GLC
vGLC = classe_glc.GLC()
Funcoes.CriarDicionarioPadrao(vGLC)

# Criar Funções para compoentes de pJanelaGramatica
def SubstituirEspaco(event):
    if event.char == ' ':
        widget = event.widget
        current_index = widget.index("insert")
        
        if current_index >= 1 and widget.get()[current_index -1] == ' ':
            vNovoTexto = widget.get()[:-1] + ' |'
             
            widget.delete(0, END)
            widget.insert(0, vNovoTexto)

def FecharJanelaNovaGramatica(pNovaGramatica: Toplevel):
    pNovaGramatica.destroy()
    vFormulario.deiconify()

# Salvando Gramatica Nova (Frase)
def SalvarGramatica(pnlNovaGramatica: PanedWindow):
    vGLC.LimparGLC()
    Funcoes.CriarDicionarioBase(vGLC)

    vDicionarios = {
        'edtNomePronome': Funcoes.CriarDicionarioPersonalizadoNP,
        'edtDetF': Funcoes.CriarDicionarioPersonalizadoDetF,
        'edtDetM': Funcoes.CriarDicionarioPersonalizadoDetM,
        'edtSubsF': Funcoes.CriarDicionarioPersonalizadoSF,
        'edtSubsM': Funcoes.CriarDicionarioPersonalizadoSM,
        'edtVerbo':Funcoes.CriarDicionarioPersonalizadoV
    }
    
    for vComponente in pnlNovaGramatica.winfo_children():
        if not isinstance(vComponente, Entry):
            continue 
        
        vNomeComponente = vComponente.winfo_name()
        
        if vNomeComponente in vDicionarios:        
            vPalavras = vComponente.get()
            vCase = vDicionarios[vNomeComponente]
            vCase(vGLC, vPalavras)

def VerificarCamposVazios(pnlNovaGramatica: PanedWindow):
    vReturn = False
    vCamposVazios = []

    for vComponente in pnlNovaGramatica.winfo_children():
        if not isinstance(vComponente, Entry):
            continue 
        
        vTexto = vComponente.get()

        if vTexto.strip() != '':
            continue

        vEdits = {
            'edtNomePronome': 'Nome Pronome',
            'edtDetF': 'Determinante Feminino', 
            'edtDetM': 'Determinante Masculino',
            'edtSubsF': 'Substantivo Feminino',
            'edtSubsM': 'Substantivo Masculino',
            'edtVerbo': 'Verbo'
        }
        
        vNomeComponente = vComponente.winfo_name()
        vNomeComponente = vEdits.get(vNomeComponente, '')
        vCamposVazios.append(vNomeComponente)
        vReturn = True

    if vCamposVazios:  
        vTitulo = 'Campos Vazios'
        vMensagem = 'Os seguintes campos estão vazios:\n\n' + '\n'.join(vCamposVazios)
        messagebox.showinfo(title = vTitulo, message = vMensagem)
    
    return vReturn

def EventoBtnLimparOnClick(tplNovaGramatica: Toplevel):
    for vComponente in tplNovaGramatica.winfo_children():
        if isinstance(vComponente, PanedWindow):
            vPanedWindow = vComponente

    for vObjetos in vPanedWindow.winfo_children():
        if isinstance(vObjetos, Entry):
            vObjetos.delete(0, END) 
        elif isinstance(vObjetos, Text):
            vObjetos.delete('1.0', END)

    # Panel da nova Gramatica Frase, verificando se está visivel
    if vPanedWindow.winfo_name() == 'pnlNovaGramaticaFrase':
        vPanedWindow.nametowidget('edtNomePronome').focus()
    else:
        vPanedWindow.nametowidget('edtSimbolo').focus()

def EventoBtnSalvarOnClick(pnlNovaGramatica: PanedWindow):       
    tplNovaGramativa = vFormulario.nametowidget('tplNovaGramatica')
    
    # Se for o Panel para criar gramática, gerar especificamente a Frase
    if pnlNovaGramatica.winfo_viewable():
        if VerificarCamposVazios(pnlNovaGramatica):     
            pnlNovaGramatica.nametowidget('edtNomePronome').focus()
            return 'break'

        SalvarGramatica(pnlNovaGramatica)
    
    # Se for uma gramatica especifica do usuário
    else:
        pnlGramaticaManual = tplNovaGramativa.nametowidget('pnlGramaticaManual')
        
        if pnlGramaticaManual.nametowidget('txtGramatica').get(1.0, END).strip() == '':
            vMensagem = 'Insira ao menos 1(uma) regra para a Nova Gramática'
            messagebox.showinfo(title = 'Regras Vazias', message = vMensagem)
            return 'break'
    
    tplNovaGramativa.destroy()
    vFormulario.deiconify()        
    lblGramatica = vFormulario.nametowidget('lblGramatica')
    lblGramatica.config(text = vGLC.FGramatica)
        
def EventoBtnResetarOnClick():
    vGLC.LimparGLC()
    Funcoes.CriarDicionarioPadrao(vGLC)
    vFormulario.nametowidget('lblGramatica').configure(text = vGLC.FGramatica)
    vFormulario.nametowidget('lblUmaFrase').configure(text = 'Frase Gerada:')

def EventoBtnAdicionarOnClick(pnlGramaticaManual: PanedWindow):
    edtSimbolo = pnlGramaticaManual.nametowidget('edtSimbolo')
    edtValores = pnlGramaticaManual.nametowidget('edtValores')
    txtGramatica = pnlGramaticaManual.nametowidget('txtGramatica')
    vSimbolo = edtSimbolo.get()
    vValores = edtValores.get()

    if not vSimbolo or not vValores:
        vMensagem = 'Porfavor, insira os 2 campos para inserir a nova regra'
        messagebox.showinfo(title = 'Campos Faltantes', message = vMensagem) 
        return 'break'
        
    if txtGramatica.get(1.0, END).strip() == '':
        vGLC.LimparGLC()
        
    vGLC.AdicionarDicionario(vSimbolo, vValores)
    
    txtGramatica.configure(state = NORMAL)
    txtGramatica.insert(END, '\n' + vSimbolo + ' --> ' + vValores)
    txtGramatica.configure(state = DISABLED)
    
    edtSimbolo.delete(0, END)
    edtValores.delete(0, END)
    edtSimbolo.focus_set()

def AlterarTipoDeGerador(pTopLevel: Toplevel):
    pnlGramaticaManual = PanedWindow(pTopLevel, relief = GROOVE, width = vLargura - 20, 
        height = vAltura - 250, borderwidth = 3, name = 'pnlGramaticaManual')
        
    lblSimbolo = Label(pnlGramaticaManual, text = 'Símbolo:', width = 10, font = 'Arial 18')
    lblValores = Label(pnlGramaticaManual, text = 'Valores:', width = 10, font = 'Arial 18')
    edtSimbolo = Entry(pnlGramaticaManual, width = 8, font = 'Arial 18', name = 'edtSimbolo')
    edtValores = Entry(pnlGramaticaManual, width = 50, font = 'Arial 18', name = 'edtValores')
    btnAdicionar = Button(pnlGramaticaManual, text = 'Adicionar', command = lambda: EventoBtnAdicionarOnClick(pnlGramaticaManual))
    txtGramatica = Text(pnlGramaticaManual, height = 9, width = 108, name = 'txtGramatica')

    pnlGramaticaManual.pack(side = TOP, anchor = N, pady = 20)
    lblSimbolo.place(x = 20, y = 30)
    lblValores.place(x = 20, y = 70)
    edtSimbolo.place(x = 140, y = 30)
    edtValores.place(x = 140, y = 70)
    btnAdicionar.place(x = 820, y = 70)
    txtGramatica.place(x = 30, y = 120)
    
    edtValores.bind('<Key>', SubstituirEspaco)   

def EventoBtnMudarEstiloOnClick(pnlNovaGramatica: PanedWindow):
    vJanelaNovaGramatica = pnlNovaGramatica.winfo_toplevel()

    if pnlNovaGramatica.winfo_viewable():
        pnlNovaGramatica.pack_forget()
        AlterarTipoDeGerador(vJanelaNovaGramatica)
    else:
        pnlNovaGramatica.pack(side = TOP, anchor = N, pady = 20)
        vJanelaNovaGramatica.nametowidget('pnlGramaticaManual').destroy()

# Crição dos eventos
def AbrirJanelaNovaGramatica(pJanelaGramatica: Toplevel):
    vFormulario.withdraw()
    pJanelaGramatica.geometry('{}x{}+{}+{}'.format(vLargura, vAltura - 100, X, Y))
    pJanelaGramatica.resizable(height = FALSE, width = FALSE)
    pJanelaGramatica.protocol("WM_DELETE_WINDOW", lambda: FecharJanelaNovaGramatica(pJanelaGramatica))

    # Criar Compoente de pJanelaGramatica
    pnlNovaGramatica = PanedWindow(pJanelaGramatica, relief = GROOVE, width = vLargura - 20, height = vAltura - 250,
         borderwidth = 3, name = 'pnlNovaGramaticaFrase')
    
    # Nova Gramatica
    lblTitulo = Label(pJanelaGramatica, width = 30, font = 'Arial 18', text = 'Insira sua Gramática:', background = '#8D99AE')
    lblNomePronome = Label(pnlNovaGramatica, width = 18, font = 'Arial 18', text = 'Nome/Pronome:')
    lblDetF = Label(pnlNovaGramatica, width = 19, font = 'Arial 18', text = 'Determinante Feminino:')
    lblDetM = Label(pnlNovaGramatica, width = 20, font = 'Arial 18', text = 'Determinante Masculino:')
    lblSubsM = Label(pnlNovaGramatica, width = 19, font = 'Arial 18', text = 'Substantivo Masculino:')
    lblSubsF = Label(pnlNovaGramatica, width = 18, font = 'Arial 18', text = 'Substantivo Feminino:')
    lblVerbo = Label(pnlNovaGramatica, width = 18, font = 'Arial 18', text = 'Verbo:')
    lblInfo = Label(pJanelaGramatica, width = 90, font = 'Arial 10', text = '• AO INSERIR, SOMENTE APERTE A TECLA [ESPAÇO] X2 (DUAS VEZES) PARA SEPARAR')

    edtNomePronome = Entry(pnlNovaGramatica, font = 'Arial 18', width = 45, name = 'edtNomePronome')
    edtDetF = Entry(pnlNovaGramatica, font = 'Arial 18', width = 45, name = 'edtDetF')
    edtDetM = Entry(pnlNovaGramatica, font = 'Arial 18', width = 45, name = 'edtDetM')
    edtSubsF = Entry(pnlNovaGramatica, font = 'Arial 18', width = 45, name = 'edtSubsF')
    edtSubsM = Entry(pnlNovaGramatica, font = 'Arial 18', width = 45, name = 'edtSubsM')
    edtVerbo = Entry(pnlNovaGramatica, font = 'Arial 18', width = 45, name = 'edtVerbo')
    
    btnSalvar = Button(pJanelaGramatica, text = 'Salvar', width = 20, background = '#7C9EB2',
    fg = 'White', font = 'Arial 15', activebackground = '#7C9EB2', command = lambda: EventoBtnSalvarOnClick(pnlNovaGramatica))
    btnLimpar = Button(pJanelaGramatica, text = 'Limpar', width = 20, background = '#52528C',
    fg = 'White', font = 'Arial 15', activebackground = '#52528C', command = lambda: EventoBtnLimparOnClick(pJanelaGramatica))
    btnMudarEstilo = Button(pJanelaGramatica, text = 'Mudar Estilo', width = 20, background = '#7C9EB2',
    fg = 'White', font = 'Arial 15', activebackground = '#7C9EB2', command = lambda: EventoBtnMudarEstiloOnClick(pnlNovaGramatica))

    # Posição dos Componentes de pJanelaGramatica
    lblTitulo.pack(side = TOP, fill = BOTH)
    pnlNovaGramatica.pack(side = TOP, anchor = N, pady = 20)

    lblNomePronome.place(x = 73, y = 30)
    lblDetF.place(x = 25, y = 70)
    lblDetM.place(x = 15, y = 110)
    lblSubsF.place(x = 42, y = 150)
    lblSubsM.place(x = 35, y = 190)
    lblVerbo.place(x = 125, y = 230)
    lblInfo.place(x = 0, y = 370)

    edtNomePronome.place(x = 300, y = 30)
    edtDetF.place(x = 300, y = 70)
    edtDetM.place(x = 300, y = 110)
    edtSubsF.place(x = 300, y = 150)
    edtSubsM.place(x = 300, y = 190)
    edtVerbo.place(x = 300, y = 230)

    btnSalvar.place(x = 675, y = 395)
    btnLimpar.place(x = 440, y = 395)
    btnMudarEstilo.place(x = 30, y = 395)

    edtNomePronome.bind('<Key>', SubstituirEspaco) 
    edtDetF.bind('<Key>', SubstituirEspaco) 
    edtDetM.bind('<Key>', SubstituirEspaco) 
    edtSubsF.bind('<Key>', SubstituirEspaco) 
    edtSubsM.bind('<Key>', SubstituirEspaco)  
    edtVerbo.bind('<Key>', SubstituirEspaco)   
    
def EventoBtnGerarUmaFraseOnClick():
    lblUmaFrase.configure(text = 'Frase Gerada:\n ' + Funcoes.GerarUmaFrase(vGLC))

def EventoBtnMostrarArvoreOnClick(): 
    vFormulario.withdraw()
    Plot.MostrarArvore()
    vFormulario.deiconify()

def EventoBtnInserirGramaticaOnClick():  
    # Verifica se a janela já foi criada
    vVerificarJanela = hasattr(EventoBtnInserirGramaticaOnClick, 'vJanelaGramatica')

    if (not vVerificarJanela or not EventoBtnInserirGramaticaOnClick.vJanelaGramatica.winfo_exists()):
        # Cria uma nova janela para inserir a gramática
        vJanelaGramatica = Toplevel(vFormulario, name = 'tplNovaGramatica')
        vJanelaGramatica.title("Inserção da Gramática")
        EventoBtnInserirGramaticaOnClick.vJanelaGramatica = vJanelaGramatica
        AbrirJanelaNovaGramatica(vJanelaGramatica)       
    else:
        EventoBtnInserirGramaticaOnClick.vJanelaGramatica.focus_set()

def EventoBtnInformacoesOnClick():
    messagebox.showinfo(title = 'Informações', message = '• Botão Gerar Frase: \n   - Gramática Livre de Contexto (GLC), começa a combinar os blocos seguindo as regras, '
        + 'formando uma nova frase a cada clique.'
        + ' \n \n• Botão Mostrar Árvore: \n   - Mostra a árvore Ramificada Principal, mostrando seus possíveis caminhos percorridos'
        + ' \n \n• Botão Inserir Gramática: \n   - Funcionalidade para o usuário poder testar inserindo sua própria gramática ('
        + 'não garantindo a estrutura das próximas frases geradas)'
        + '\n \n• Botão Resetar: \n   - Retorna na Gramática original do programa e limpa a frase antiga gerada')

# Cria Componentes de vFormulário
pnlCimaBotoes = PanedWindow(vFormulario, relief = RIDGE, width = vLargura - 20, height = 80, borderwidth = 3)
# pnlArvore = PanedWindow(vFormulario, relief = RIDGE, width = vLargura - 20, height = 80, borderwidth = 3)

btnGerarUmaFrase = Button(pnlCimaBotoes, text = 'Gerar Frase', width = 20, background = '#7C9EB2',
    fg = 'White', font = 'Arial 15', activebackground = '#7C9EB2', command = EventoBtnGerarUmaFraseOnClick)

btnMostrarArvore = Button(pnlCimaBotoes, text = 'Mostrar Árvore', width = 20, background = '#52528C',
    fg = 'White', font = 'Arial 15', activebackground = '#52528C', command = EventoBtnMostrarArvoreOnClick)

btnInserirGramatica = Button(pnlCimaBotoes, text = 'Inserir Gramática', width = 20, background = '#372554',
    fg = 'White', font = 'Arial 15', activebackground = '#372554', command = EventoBtnInserirGramaticaOnClick)

btnResetar = Button(vFormulario, text = 'Resetar', width = 5, background = '#F6E8EA', font = 'Arial', command = EventoBtnResetarOnClick)

image = PhotoImage(file = r"Imagens/icon.png")
image = image.subsample(50, 50)

btnInformacoes = Button(vFormulario, width = 50, text = 'Info', image = image, compound = LEFT, font = 'Arial',
    relief = FLAT, command = EventoBtnInformacoesOnClick)

lblUmaFrase = Label(vFormulario, width = 85, font = 'Arial 15', text = 'Frase Gerada: ', name = 'lblUmaFrase')

lblGramatica = Label(vFormulario, width = 75, background = vFormulario.cget('bg'),
     borderwidth = 0, text = vGLC.FGramatica, justify = LEFT, font = 'Courier 15', name = 'lblGramatica')
    

# Posição dos Componentes de vFormulário
pnlCimaBotoes.pack(side = TOP, anchor = N, pady = 15)

btnGerarUmaFrase.pack(fill = BOTH, side = LEFT)
btnInserirGramatica.pack(fill = BOTH, side = RIGHT)
btnMostrarArvore.pack(fill = BOTH, side = TOP)
btnResetar.place(x = 20, y = vAltura - 50)
btnInformacoes.place(x = vLargura - 90, y = vAltura - 50)

lblUmaFrase.place(x = 5, y = 90)
lblGramatica.place(x = 20, y = 230)

vFormulario.resizable(height = FALSE, width = FALSE)
vFormulario.mainloop()