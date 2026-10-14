import time
import pyautogui

# Medida de segurança caso o mouse fuja do controle
pyautogui.FAILSAFE = True

print("Prepare-se! O mouse vai marcar a região do jogo para você testar.")
time.sleep(2)

# --- AJUSTE ESTES 4 NÚMEROS CONFORME O SEU NOX ---
# x_inicial, y_inicial, largura, altura
x = 50
y = 20
largura = 1250
altura = 700

print(f"Testando a região: X={x}, Y={y}, Largura={largura}, Altura={altura}")

# 1. Vai para o canto Superior Esquerdo
print("Movendo para o Canto Superior Esquerdo...")
pyautogui.moveTo(x, y, duration=1)
time.sleep(1)

# 2. Vai para o canto Superior Direito
print("Movendo para o Canto Superior Direito...")
pyautogui.moveTo(x + largura, y, duration=1)
time.sleep(1)

# 3. Vai para o canto Inferior Direito
print("Movendo para o Canto Inferior Direito...")
pyautogui.moveTo(x + largura, y + altura, duration=1)
time.sleep(1)

# 4. Vai para o canto Inferior Esquerdo
print("Movendo para o Canto Inferior Esquerdo...")
pyautogui.moveTo(x, y + altura, duration=1)
time.sleep(1)

print("Teste de contorno concluído! Se o mouse desenhou exatamente em volta da tela do Rucoy, os números estão perfeitos.")