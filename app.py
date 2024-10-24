import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def draw_box(ax, text, xy, width=1.5, height=0.5, fontsize=9):
    # Função para desenhar caixas de texto
    boxstyle = 'round,pad=0.3'
    ax.add_patch(FancyBboxPatch(xy, width, height, boxstyle=boxstyle, edgecolor='black', facecolor='white'))
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha='center', va='center', fontsize=fontsize)

def draw_arrow(ax, start, end):
    # Função para desenhar setas entre as caixas
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle='->', lw=1.5))

def draw_hierarchy():
    fig, ax = plt.subplots(figsize=(10, 8))  # Tamanho do gráfico ajustado
    ax.set_xlim(0, 10)  # Reduzi a largura
    ax.set_ylim(-12, 3)  # A altura também foi ajustada
    
    # Desenhando caixas e texto da hierarquia
    draw_box(ax, 'Faculdade', (4, 1), width=2, height=0.7, fontsize=10)
    draw_box(ax, 'Objetos Abstratos', (1, -1), width=2.5, height=0.6)
    draw_box(ax, 'Eventos Generalizados', (7, -1), width=2.5, height=0.6)
    
    # Subcategorias de Objetos Abstratos
    draw_box(ax, 'Cursos', (0, -3), width=2, height=0.5)
    draw_box(ax, 'Disciplinas', (3, -3), width=2, height=0.5)
    draw_box(ax, 'Professores', (6, -3), width=2, height=0.5)
    
    draw_box(ax, 'Direito', (0, -5), width=1.5)
    draw_box(ax, 'ADM', (0, -6), width=1.5)
    draw_box(ax, 'Eng. Software', (0, -7), width=1.5)
    
    draw_box(ax, 'Dir. Civil', (3, -5), width=1.5)
    draw_box(ax, 'Finanças', (3, -6), width=1.5)
    draw_box(ax, 'Algoritmos', (3, -7), width=1.5)
    
    draw_box(ax, 'Carlos', (6, -5), width=1.5)
    draw_box(ax, 'Ana', (6, -6), width=1.5)
    draw_box(ax, 'Laura', (6, -7), width=1.5)
    
    # Subcategorias de Eventos Generalizados
    draw_box(ax, 'Intervalos', (8, -3), width=1.5, height=0.5)
    draw_box(ax, 'Locais', (10, -3), width=1.5, height=0.5)
    draw_box(ax, 'Objetos', (12, -3), width=1.5, height=0.5)
    draw_box(ax, 'Processos', (10, -6), width=1.5, height=0.5)
    
    draw_box(ax, 'Horários', (8, -5), width=1.5)
    draw_box(ax, 'Semestres', (8, -6), width=1.5)
    
    draw_box(ax, 'Salas', (10, -5), width=1.5)
    draw_box(ax, 'Laboratórios', (10, -6), width=1.5)
    draw_box(ax, 'Biblioteca', (10, -7), width=1.5)
    
    draw_box(ax, 'Cadeiras', (12, -5), width=1.5)
    draw_box(ax, 'Mesa', (12, -6), width=1.5)
    draw_box(ax, 'Quadro', (12, -7), width=1.5)
    
    draw_box(ax, 'Aulas', (10, -8), width=1.5)
    draw_box(ax, 'Provas', (10, -9), width=1.5)
    draw_box(ax, 'Congressos', (10, -10), width=1.5)
    
    # Desenhando setas para a hierarquia
    draw_arrow(ax, (5, 0.5), (2, -0.5))  # Faculdade -> Objetos Abstratos
    draw_arrow(ax, (5, 0.5), (8, -0.5))  # Faculdade -> Eventos Generalizados
    
    # Setas para os subníveis de Objetos Abstratos
    draw_arrow(ax, (2.25, -2), (0.75, -2.8))  # Objetos Abstratos -> Cursos
    draw_arrow(ax, (2.25, -2), (3.75, -2.8))  # Objetos Abstratos -> Disciplinas
    draw_arrow(ax, (2.25, -2), (6.75, -2.8))  # Objetos Abstratos -> Professores
    
    draw_arrow(ax, (0.75, -4.5), (0.75, -4.8))  # Cursos -> Direito
    draw_arrow(ax, (0.75, -5.8), (0.75, -5.8))  # Cursos -> ADM
    draw_arrow(ax, (0.75, -6.8), (0.75, -6.8))  # Cursos -> Eng. Software
    
    draw_arrow(ax, (3.75, -4.5), (3.75, -4.8))  # Disciplinas -> Dir. Civil
    draw_arrow(ax, (3.75, -5.8), (3.75, -5.8))  # Disciplinas -> Finanças
    draw_arrow(ax, (3.75, -6.8), (3.75, -6.8))  # Disciplinas -> Algoritmos
    
    draw_arrow(ax, (6.75, -4.5), (6.75, -4.8))  # Professores -> Carlos
    draw_arrow(ax, (6.75, -5.8), (6.75, -5.8))  # Professores -> Ana
    draw_arrow(ax, (6.75, -6.8), (6.75, -6.8))  # Professores -> Laura
    
    # Setas para os subníveis de Eventos Generalizados
    draw_arrow(ax, (8.75, -2), (8.75, -2.8))  # Eventos Generalizados -> Intervalos
    draw_arrow(ax, (8.75, -2), (10.75, -2.8))  # Eventos Generalizados -> Locais
    draw_arrow(ax, (8.75, -2), (12.75, -2.8))  # Eventos Generalizados -> Objetos
    draw_arrow(ax, (10.75, -4.5), (10.75, -5.3))  # Eventos Generalizados -> Processos
    
    draw_arrow(ax, (8.75, -4.5), (8.75, -4.8))  # Intervalos -> Horários
    draw_arrow(ax, (8.75, -5.8), (8.75, -5.8))  # Intervalos -> Semestres
    
    draw_arrow(ax, (10.75, -4.5), (10.75, -4.8))  # Locais -> Salas
    draw_arrow(ax, (10.75, -5.8), (10.75, -5.8))  # Locais -> Laboratórios
    draw_arrow(ax, (10.75, -6.8), (10.75, -6.8))  # Locais -> Biblioteca
    
    draw_arrow(ax, (12.75, -4.5), (12.75, -4.8))  # Objetos -> Cadeiras
    draw_arrow(ax, (12.75, -5.8), (12.75, -5.8))  # Objetos -> Mesa
    draw_arrow(ax, (12.75, -6.8), (12.75, -6.8))  # Objetos -> Quadro
    
    draw_arrow(ax, (10.75, -8), (10.75, -8.8))  # Processos -> Aulas
    draw_arrow(ax, (10.75, -9.3), (10.75, -9.3))  # Processos -> Provas
    draw_arrow(ax, (10.75, -10.3), (10.75, -10.3))  # Processos -> Congressos
    
    ax.axis('off')  # Esconde os eixos
    plt.show()

# Chama a função para desenhar o gráfico
draw_hierarchy()
