# Jogo do NIM

## Descrição

O **Jogo do NIM** é um jogo de estratégia simples onde dois jogadores (ou um jogador contra o computador) competem para retirar pedras de uma pilha. O objetivo do jogo é evitar ser o jogador que retira a última pedra. O jogo continua até que todas as pedras sejam retiradas.

## Regras do Jogo

- O jogo começa com uma quantidade inicial de pedras (definida pelo jogador).
- Em cada turno, um jogador pode retirar entre 1 e um número máximo de pedras (definido no início do jogo).
- O jogo alterna entre os jogadores, começando pelo Jogador 1.
- O jogador que retirar a última pedra perde o jogo.

### Opções de Jogo
1. **Modo Jogador vs Jogador**: Dois jogadores se alternam para retirar pedras até que alguém perca.
2. **Modo Jogador vs Computador**: O jogador se alterna com a máquina, que usa uma estratégia para tentar ganhar o máximo possível.

## Como Jogar

1. O número de pedras iniciais e o número máximo de pedras que podem ser retiradas por vez são definidos no início do jogo.
2. O jogo pode ser jogado entre dois jogadores humanos (Jogador 1 e Jogador 2) ou entre um jogador e o computador.
3. Em cada rodada, o jogador da vez escolhe quantas pedras quer retirar (de 1 até o número máximo definido).
4. A máquina (caso esteja jogando contra o computador) irá tentar usar uma estratégia para forçar o jogador a retirar a última pedra.

## Estratégia do Computador

O computador tenta sempre deixar o jogador em uma posição onde ele precise retirar a última pedra. A lógica por trás dessa estratégia é a seguinte:

1. O computador sempre tenta deixar o número de pedras restantes igual a 1 no próximo turno do jogador.
2. Se o número de pedras restantes for múltiplo de `(max_retirada + 1)`, o computador retira a menor quantidade possível de pedras.
3. Caso contrário, o computador calculará a quantidade ideal de pedras a ser retirada para deixar o jogador com 1 pedra restante, o que garante a vitória ao computador.

## Lógica do Jogo

1. **Início do Jogo**: O número de pedras e o número máximo de pedras que podem ser retiradas por vez são definidos pelo jogador.
2. **Turnos**: O jogo alterna entre os jogadores ou entre o jogador e a máquina, de acordo com o modo selecionado.
3. **Jogada do Jogador**: O jogador escolhe quantas pedras deseja retirar. O sistema verifica se a jogada é válida (ou seja, se o número de pedras retiradas está dentro do limite e se ainda há pedras suficientes).
4. **Jogada da Máquina**: Se o modo de jogo for Jogador vs Computador, a máquina faz sua jogada com base na estratégia descrita anteriormente.
5. **Verificação de Vitória**: A cada turno, o sistema verifica se o número de pedras restantes é 0. O jogador que retirar a última pedra perde o jogo.
6. **Finalização**: O jogo é encerrado quando uma vitória é determinada (quando o jogador ou a máquina retira a última pedra).

## Como Rodar o Jogo

### Requisitos

- Python 3.x ou superior instalado.

### Passos para Executar

1. Clone este repositório para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/jogo-nim.git

2. Navegue até o diretório do repositório: 

    ```bash
    cd jogo-nim

3. Execute o código Python: 

    ```bash
    python jogo_nim.py

4. Siga as instruções na tela para definir o número de pedras e o tipo de jogo (Jogador vs Jogador ou Jogador vc Computador.)

## Exemplo de execução

Bem-vindo ao jogo do NIM
Digite o número de pedras: 10
Digite o número máximo de pedras que podem ser retiradas por vez: 2
Você quer jogar contra o (1) Jogador ou (2) Computador? (Digite 1 ou 2) 2
Numeros de pedras restantes: 10
VEZ DO JOGADOR 1!
Quantas pedras você deseja retirar: (1 a 2) 2
Numeros de pedras restantes: 8
VEZ DO COMPUTADOR!
O computador retirou: 1
Numeros de pedras restantes: 7
VEZ DO JOGADOR 1!
Quantas pedras você deseja retirar: (1 a 2) 2
...

Estrutura do Código
O código está organizado da seguinte maneira:

1. Classe JogoNim:
    Responsável por gerenciar o estado do jogo (número de pedras, turno, etc.).
    Contém os métodos para exibir o status do jogo, fazer jogadas (tanto para o jogador quanto para a máquina), verificar a vitória e alternar os turnos.

2. Função iniciar_jogo:
    Ponto de entrada do programa. Permite ao usuário configurar o número de pedras, o número máximo de pedras retiradas por vez e escolher o tipo de jogo (jogador vs jogador ou jogador vs computador).

3. Métodos:
    exibir_status: Exibe a quantidade de pedras restantes e o turno atual.
    jogada_jogador: Processa a jogada do jogador, verificando se a jogada é válida.
    jogada_maquina: Realiza a jogada da máquina, utilizando a estratégia de deixar o jogador com 1 pedra restante.
    verifica_vitoria: Verifica se o jogo terminou, ou seja, se o número de pedras restantes é 0.
    alterar_turno: Alterna entre os turnos dos jogadores.
    jogar: Método principal do jogo, que executa a lógica de alternância de turnos, jogadas e verificação de vitória.

### Licença

    Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.