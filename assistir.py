import time
import keyboard
from stable_baselines3 import PPO
from ambiente_regrasrucoy import iarules # Correção do import

print("Carregando o cérebro da IA...")
modelo = PPO.load("ppo_iarules.zip") 
ambiente = iarules()

print("Iniciando em 3 segundos. Posicione o Nox na tela!")
time.sleep(3)

obs, _ = ambiente.reset()

while True:
    if keyboard.is_pressed('q'):
        print("Teste encerrado pelo usuário!")
        break

    acao, _ = modelo.predict(obs, deterministic=True)
    obs, recompensa, terminated, truncated, _ = ambiente.step(acao)
    
    if terminated or truncated:
        print("Episódio acabou! Reiniciando...")
        obs, _ = ambiente.reset()