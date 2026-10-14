import time
import pyautogui
import keyboard

print("Posicione o mouse sobre o Nox e prepare o jogo...")
print("Pressione a tecla 'c' para tirar o print recortado ou 'ESC' para sair.")

contador = 1

x_inicial = 50
y_inicial = 20
largura = 1250
altura = 700    
regiao_do_jogo = (x_inicial, y_inicial, largura, altura)
while True:
    if keyboard.is_pressed('c'):
        # -------------------------------------------------------------
        # ATENÇÃO AQUI: 
        # x, y = Ponto onde começa o canto superior esquerdo da tela do jogo
        # largura, altura = O tamanho da área que vamos fotografar
        # Como sua tela é 1360x760, ajustamos para capturar o miolo do Nox.
        # (Você pode ajustar esses 4 números se o print sair cortado errado)
        # -------------------------------------------------------------
        
        
        print_tela = pyautogui.screenshot(region=regiao_do_jogo)
        
        # Redimensiona para 100x100 pixels (exatamente o tamanho que a IA lê)
        print_processado = print_tela.resize((100, 100))
        
        nome_arquivo = f"rucoy_recorte_{contador}.png"
        print_processado.save(nome_arquivo)
        print(f"Print recortado e redimensionado salvo: {nome_arquivo}")
        
        contador += 1
        time.sleep(0.5)
        
    if keyboard.is_pressed('esc'):
        print("Encerrando coletor.")
        break