import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

def MostrarArvore():
  plt.subplots(figsize=(14, 8))
  Tela = plt.get_current_fig_manager()
  Tela.window.attributes('-zoomed', True)
 
  plt.suptitle('Árvore Ramificada Principal:')
  plt.title('• As cores representam níveis, sendo cinza-escuro, S, a raiz.\n' + 
    '• Se ficar ruim a vizualização, feche e abra novamente.')

  vDe = ['S', 'S', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'NP', 'DetM', 'DetM', 'DetM',
    'DetF', 'DetF', 'DetF', 'NF', 'NF', 'NF', 'NF', 'NM', 'NM', 'NM', 'NM',
    'VP', 'VP', 'V', 'V', 'V', 'V']

  vPara = ['NP', 'VP', 'DetM', 'NM', 'DetF', 'NF', 'ele', 'ela', 'você' ,'Marcos', 'Cláudia', 'tu' , 'José', 'Maria', 'Hemerson', 'um', 'o', 'meu',
    'uma', 'a', 'minha', 'girafa', 'mesa', 'calça', 'carne', 'carro', 'rato', 'casaco', 'sofa',
    'V', 'NP', 'pegou', 'jogou', 'pulou', 'comeu']

  vRelacoes = pd.DataFrame({'De': vDe, 'Para': vPara })

  vCategorias = pd.DataFrame({'ID':['S', 'NP', 'VP', 'DetM', 'DetF', 'NF', 'NM', 'V'], 
    'Nivel':['Raiz','Nivel1', 'Nivel1', 'Nivel2', 'Nivel2', 'Nivel2', 'Nivel2', 'Nivel3']})

  G = nx.from_pandas_edgelist(vRelacoes, 'De', 'Para', create_using = nx.Graph())

  # Configurar Categorias
  vCategorias = vCategorias.set_index('ID')
  vCategorias = vCategorias.reindex(G.nodes())

  vCategorias['Nivel'] = pd.Categorical(vCategorias['Nivel'])

  # Configurando o Tamanho 
  vTamanho = [2500 if entry == 'Raiz' else 1750 if entry == 'Nivel1' else 1350 if entry == 'Nivel2' else 1000 for entry in vCategorias.Nivel]

  # Configurar gráfico
  nx.draw(G, with_labels=True, node_color = vCategorias['Nivel'].cat.codes, cmap = plt.cm.Dark2, 
    node_size = vTamanho, font_size = 9, font_weight = "bold", width = 0.75)

  Tela.show()
        