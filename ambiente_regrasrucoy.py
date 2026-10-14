import pyautogui as pg
import keyboard
import time
import gymnasium as gym
from gymnasium import spaces
import numpy as np
import sys
import subprocess

# Variáveis globais para rastreio
x = 0
y = 0

# --- FUNÇÃO MÁGICA: CLIQUE INVISÍVEL VIA ADB ---
# --- FUNÇÃO MÁGICA: CLIQUE INVISÍVEL VIA ADB (ATUALIZADA) ---
def clicar_adb(x_coord, y_coord):
    # O "-s 127.0.0.1:62001" garante que o comando vá direto para o Nox, mesmo que o ADB reinicie
    comando = f"adb -s 127.0.0.1:62001 shell input tap {x_coord} {y_coord}"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    
    if resultado.stderr:
        print(f"❌ ERRO ADB: {resultado.stderr.strip()}")

class iarules(gym.Env):
    def __init__(self):
        super(iarules, self).__init__()
        self.observation_space = spaces.Box(low=0, high=255, shape=(100, 100, 3), dtype=np.uint8)
        self.action_space = spaces.Discrete(4)
        self.passos_presos = 0
        
        # Conecta o terminal ao Nox automaticamente ao iniciar
        print("🔌 Conectando ao emulador Nox em background...")
        subprocess.run("adb connect 127.0.0.1:62001", shell=True, capture_output=True)

    def pegar_observacao(self):
        # A captura continua com pyautogui (não rouba o mouse), apenas deixe o Nox visível na tela
        screenshot = pg.screenshot(region=(50, 20, 1250, 700))
        screenshot2 = screenshot.resize((100, 100))
        return np.array(screenshot2, dtype=np.uint8)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.passos_presos = 0
        
        print("🔄 Fim de Episódio! Resgatando o personagem (clique no minimapa)...")
        
        # Coordenada do minimapa DENTRO do Android (ajuste se necessário)
        # Enviamos dois cliques para garantir que o jogo regista o toque
        clicar_adb(760, 380)
        time.sleep(0.5)
        clicar_adb(760, 380)
        time.sleep(0.5)
        clicar_adb(594, 385)
        time.sleep(0.5)
        clicar_adb(676, 476)
        
        # Pausa de 4 segundos para dar tempo de o personagem caminhar até à área livre
        time.sleep(4)
        
        return self.pegar_observacao(), {}

    def step(self, action):
        if keyboard.is_pressed('f5'):
            print("🚨 Encerrado pelo usuário via F5!")
            raise KeyboardInterrupt  # Simula o Ctrl+C para acionar o salvamento no cerebro.py

        obs_antes = self.pegar_observacao()

        # --- ATENÇÃO NA CALIBRAÇÃO AQUI ---
        # Coordenadas relativas à resolução interna do Android/Nox.
        # Se o seu Nox for 1280x720, o centro do personagem é 640x360.
        centro_x = 640
        centro_y = 360
        distancia = 80 
                
        if action == 0:   clicar_adb(centro_x, centro_y - distancia) # Cima
        elif action == 1: clicar_adb(centro_x, centro_y + distancia) # Baixo
        elif action == 2: clicar_adb(centro_x - distancia, centro_y) # Esquerda
        elif action == 3: clicar_adb(centro_x + distancia, centro_y) # Direita
            
        time.sleep(0.4) # Aumentei um pouquinho a pausa para dar tempo do ADB processar o toque
        
        obs_dps = self.pegar_observacao()
        diff_pixels = np.mean(np.abs(obs_dps.astype(np.int32) - obs_antes.astype(np.int32)))

        print(f"Diferença de pixels: {diff_pixels:.2f}")

        limiar = 4.5
        terminated = False
        truncated = False

        if diff_pixels < limiar:
            global x
            x += 1
            self.passos_presos += 1
            reward = -5.0  
            print(f"Preso! Passos: {self.passos_presos} | Diff: {diff_pixels:.2f}")
            
            if self.passos_presos >= 5:
                global y
                y += 1
                terminated = True 
                reward = -20.0  
                print("💥 Fim de Episódio por inatividade!")
        else:
            self.passos_presos = 0 
            print(f"Andou! | Diff: {diff_pixels:.2f}")
            reward = 50.0  

        print(f"Recompensa obtida: {reward}")
        print(f"x (erros totais): {x}, y (episódios falhos): {y}")
        
        return obs_dps, reward, terminated, truncated, {}