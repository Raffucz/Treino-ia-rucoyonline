from stable_baselines3 import PPO
from ambiente_regrasrucoy import iarules
import time

time.sleep(0.5)
print("Preparando ambiente...")
env = iarules()
time.sleep(2)

print("Carregando o cérebro evoluído e co tinuando treinamento...")
# Carrega o modelo anterior
model = PPO.load("ppo_iarules", env=env) 

# --- INÍCIO DO BLOCO DE TREINO SEGURO ---
try:
    print("🚀 Treino iniciado! (Pressione F5 no jogo ou Ctrl+C no terminal para parar e salvar)")
    # Coloquei 20.000 para ela ficar ainda mais inteligente!
    model.learn(total_timesteps=20000) 
    
except KeyboardInterrupt:
    # Se você apertar F5 ou Ctrl+C, o código foge do erro e cai direto aqui
    print("\n🚨 Treino interrompido manualmente pelo usuário!")
    
finally:
    # O 'finally' garante que o modelo será salvo independentemente de como o treino parou
    print("💾 Salvando todo o conhecimento adquirido até agora...")
    model.save("ppo_iarules_v2")
    print("✅ Conhecimento salvo com sucesso (ppo_iarules_v2.zip)! Pode fechar a janela.")
# --- FIM DO BLOCO DE TREINO SEGURO ---