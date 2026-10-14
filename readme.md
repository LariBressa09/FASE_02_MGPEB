# 🚀 MGPEB - Módulo de Gerenciamento de Pouso e Estabilização de Base
### Missão Aurora Siger — Fase 2 (Atividade Integradora / PBL)

Repositório com o protótipo funcional em Python do **MGPEB**, desenvolvido para simular a priorização de aproximação e o controle das etapas críticas de descida na atmosfera de Marte (fase EDL — *Entry, Descent, and Landing*).

---

## 👥 Integrantes da Equipe

* **Aldo Roschel** — RM: 575601
* **Kelven Carlos Luiz de Souza** — RM: 575105
* **Larissa Bressanini Lehn** — RM: 575921
* **Nicole Luiza Mascarenhas Zerbato** — RM: 575981

---

## 🎯 Objetivo do Projeto

O script simula as decisões automatizadas de um sistema embarcado de controle espacial para o pouso de módulos essenciais da colônia marciana (baseado na arquitetura *NASA DRA 5.0*):

1. **Cadastro e Gestão de Módulos:** Organização dos módulos, suas massas, combustíveis e horários de chegada utilizando estruturas de dados lineares (listas).
2. **Algoritmo de Ordenação Clássico (*Bubble Sort*):** Reorganização da fila de descida considerando:
   * **Prioridade Absoluta:** O módulo central **MGPEB** tem precedência obrigatória.
   * **1º Critério:** Data e horário estimado de chegada à órbita marciana.
   * **2º Critério de Desempate:** Relação Massa/Combustível (`massa / combustível`), priorizando módulos em situação mais crítica.
3. **Tomada de Decisão Lógica (Portas Lógicas):** Simulação em tempo real da transição dos sistemas de frenagem (Escudo Térmico, Paraquedas, Retrofoguetes e Trens de Pouso) conforme parâmetros de altitude e velocidade.

---

## 🛠️ Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 3.x
* **Bibliotecas Utilizadas:**
  * `datetime` (nativa): Manipulação e comparação de datas e horários de chegada dos módulos.
  * `numpy`: Operações aritméticas elementares vetorizadas nas listas de massa e combustível.
* **Estruturas de Dados:** Listas lineares paralelas indexadas.
* **Algoritmos:** Ordenação clássica por trocas sucessivas (*Bubble Sort*) com laços aninhados (`for`).
* **Lógica Computacional:** Estruturas condicionais (`if`, `elif`, `else`) que replicam diretamente o circuito digital de portas lógicas (AND, OR, NOT).

---

## 📋 Módulos Cadastrados

| Categoria | Nome do Módulo | Função Principal |
| :--- | :--- | :--- |
| **Infraestrutura Inicial** | **MGPEB & Porto de Pouso** | Estabilização de solo e gerenciamento dos pousos (Prioridade Máxima). |
| **Energia** | Reatores Nucleares / Matriz Solar | Geração contínua de energia elétrica. |
| **Suporte à Vida (ECLSS)** | Módulo ISRU / Suporte à Vida | Produção de oxigênio/água e combustível *in-situ*. |
| **Habitação & Saúde** | Habitacional Blindado | Convivência e blindagem contra radiação cósmica. |
| **Habitação & Saúde** | Médico & Bioclimático | Enfermaria, suporte clínico e isolamento biológico. |
| **Alimentação** | Estufa Agrícola / Biofarm | Produção hidropônica e reciclagem orgânica. |
| **Industrial & Pesquisa** | Processamento de Materiais | Mineração e manufatura por impressão 3D. |
| **Industrial & Pesquisa** | Laboratório Científico | Pesquisas astrobiológicas e manutenção técnica. |

---

## 🛬 Regras de Decisão da Descida (EDL)

A simulação de descida do módulo MGPEB avalia as variáveis de altitude ($h$ em metros) e velocidade ($v$ em $m/s$), traduzindo as seguintes regras lógicas do sistema:

| Faixa de Altitude ($m$) | Faixa de Velocidade ($m/s$) | Ação / Evento de Engenharia |
| :---: | :---: | :--- |
| $11.000 < h \le 125.000$ | $440 < v \le 5.800$ | **Ativação do Escudo Térmico** (Frenagem aerodinâmica hipersônica) |
| $1.800 < h \le 11.000$ | $83 < v \le 440$ | **Acionamento do Paraquedas Supersônico** (Arrasto atmosférico) |
| $h \le 1.800$ | $0{,}75 < v \le 83$ | **Acionamento de Retrofoguetes** (Propulsão ativa terminal) |
| Qualquer altitude | $v \le 0{,}75$ | **Acionamento dos Amortecedores e Trens de Pouso** (Pouso Suave Concluído) |
| *Fora das janelas* | *Fora das janelas* | **Alerta:** Módulo não disponível para iniciar fase de pouso |

---

## ⚙️ Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado. Em seguida, instale a dependência necessária:

```bash
pip install numpy
```

### 2. Execução do Script

Execute o script principal no terminal:

```bash
python trabalho.py
```

### 3. Interação na Fase de Pouso

O programa irá:
1. Exibir a lista ordenada com a prioridade de descida de cada módulo.
2. Iniciar a fase interativa de descida para o **MGPEB**, solicitando via terminal:
   - `DIGITE A ALTITUDE (m):`
   - `DIGITE A VELOCIDADE (m/s):`
3. A cada entrada, o sistema validará os parâmetros de voo e indicará a etapa acionada. O pouso é concluído quando a velocidade for menor ou igual a $0{,}75\text{ m/s}$.