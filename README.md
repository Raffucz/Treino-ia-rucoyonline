# 🤖 IA Rucoy

> Sistema de Inteligência Artificial e Visão Computacional desenvolvido para automação, captura de tela e tomada de decisões baseada em aprendizado por reforço (PPO) voltado para o ambiente de jogo **Rucoy Online**.

---

## 📌 Sumário
- [Sobre o Projeto](#-sobre-o-projeto)
- [Estrutura do Repositório](#-estrutura-do-repositório)
- [Arquitetura e Módulos](#-arquitetura-e-módulos)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Como Utilizar](#-como-utilizar)
- [Contribuição](#-contribuição)
- [Aviso Legal](#-aviso-legal)

---

## 📖 Sobre o Projeto

O **IA Rucoy** une técnicas de **Visão Computacional** e **Aprendizado por Reforço (Reinforcement Learning)** com o algoritmo *Proximal Policy Optimization (PPO)*. O objetivo do sistema é analisar o estado da tela do jogo em tempo real, interpretar o cenário através dos módulos lógicos e interagir de forma autônoma aplicando ações de controle de mouse.

---

## 🗂️ Estrutura do Repositório

```text
ia_rucoy/
├── ambiente_regrasrucoy.py  # Ambiente compatível com Gym/PettingZoo (recompensas e regras)
├── assistir.py              # Script de inferência para visualização do agente treinado
├── cerebro.py               # Arquitetura da rede neural e lógica de decisão
├── coletor.py               # Captura de tela e pipeline de coleta de dados visuais
├── mouse.py                 # Biblioteca de controle de hardware (simulação de cliques e mouse)
├── ppo_iarules.zip          # Pesos do modelo treinado (PPO)
└── images/                  # Banco de imagens para testes, templates e referências visuais
    ├── rucoytela_1.png
    ├── rucoytela_2.png
    ├── rucoy_recorte_1.png
    └── rucoy_recorte_2.png
🛠️ Arquitetura e MódulosMóduloDescrição Principalambiente_regrasrucoy.pyDefine o ecossistema do jogo em formato de ambiente de RL, calculando recompensas positivas/negativas com base nas regras estabelecidas.cerebro.pyCentraliza a construção da rede neural e a política de tomada de ação do agente.coletor.pyResponsável por monitorar e recortar frames da tela do jogo em tempo de execução para alimentar as observações da IA.mouse.pyConverte as saídas numéricas do modelo de IA em ações físicas de movimento e cliques do mouse.assistir.pyCarrega o arquivo binário do modelo (ppo_iarules.zip) para rodar sessões de demonstração ou testes práticos.⚙️ Pré-requisitosCertifique-se de possuir os seguintes itens instalados no seu sistema:Python (versão 3.8 ou superior recomendada)Pip (gerenciador de pacotes do Python)📥 Instalação e ConfiguraçãoSiga os passos abaixo para configurar o projeto localmente:Clone o repositório:Bashgit clone [https://github.com/Raffucz/Treino-ia-rucoyonline.git](https://github.com/Raffucz/Treino-ia-rucoyonline.git)
cd Treino-ia-rucoyonline
Crie e ative um ambiente virtual:Bashpython -m venv venv

# No Windows:
venv\Scripts\activate

# No Linux / macOS:
source venv/bin/activate
Instale as dependências necessárias:Bashpip install stable-baselines3 gymnasium opencv-python pyautogui pynput
🎮 Como Utilizar1. Assistir à IA em Execução (Modo Inferência)Para carregar o modelo treinado (ppo_iarules.zip) e observar o agente interagindo com o ambiente:Bashpython assistir.py
2. Executar a Coleta de Dados / MonitoramentoCaso precise coletar capturas de tela e dados brutos de referência do ambiente:Bashpython coletor.py
🤝 ContribuiçãoContribuições, melhorias na arquitetura de recompensa ou otimizações no modelo são sempre bem-vindas!Faça um Fork do projeto.   Crie uma branch para sua funcionalidade (git checkout -b feature/nova-funcionalidade).   Faça o Commit das suas alterações (git commit -m 'Adiciona nova funcionalidade').   Faça o Push para a Branch (git push origin feature/nova-funcionalidade).Abra um Pull Request.⚠️ Aviso LegalEste projeto foi desenvolvido estritamente para fins educacionais, acadêmicos e de pesquisa em aprendizado por reforço e visão computacional. O autor não se responsabiliza pelo uso indevido de ferramentas de automação em softwares de terceiros.