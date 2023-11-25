# Documentação do Código

## Perceptron Class

A classe `Perceptron` implementa um perceptron simples, que pode ser treinado para aprender a lógica de portas lógicas simples (AND, OR, NAND) e uma solução alternativa para a porta XOR.

### Métodos

#### `__init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5)`

Método de inicialização que configura os parâmetros do perceptron.

- `learning_rate`: Taxa de aprendizado para ajuste dos pesos.
- `n_iterations`: Número de iterações durante o treinamento.
- `threshold`: Limiar de ativação para a função degrau.

#### `activation_function(self, x)`

Função de ativação (função degrau) que retorna 1 se `x` for maior ou igual ao limiar e 0 caso contrário.

#### `predict(self, inputs)`

Realiza uma previsão usando o perceptron.

- `inputs`: Vetor de entradas.

Retorna a saída prevista após a aplicação da função de ativação.

#### `train(self, X, y)`

Treina o perceptron ajustando os pesos e o viés para minimizar o erro de previsão.

- `X`: Matriz de entradas.
- `y`: Vetor de saídas desejadas.

## Função Choice_model()

A função `choice_model()` solicita ao usuário a escolha de uma porta lógica (AND, OR, XOR, NAND) e retorna o nome do modelo escolhido.

Retorna:
- `model`: Nome do modelo escolhido.

## Função Main()

A função `main()` é a função principal do programa que conduz a execução.

- Solicita ao usuário a escolha do modelo de porta lógica.
- Define as entradas e saídas desejadas com base no modelo escolhido.
- Treina o perceptron.
- Testa o perceptron e, no caso do modelo XOR, explica a solução alternativa usando dois perceptrons treinados para representar NAND e AND.

### Execução do Programa

O programa é executado chamando a função `main()` se o script for executado diretamente.

```python
if __name__ == "__main__":
    main()
```

# Solução da Porta XOR usando Dois Perceptrons

A solução da porta XOR usando dois perceptrons envolve uma abordagem conhecida como **Rede Neural de duas camadas**. A lógica da porta XOR não é linearmente separável, o que significa que não é possível traçar uma única linha (ou plano) para separar claramente as instâncias positivas das instâncias negativas no espaço de entrada.

## Perceptron NAND

- Este perceptron é treinado para representar a lógica da porta NAND.
- A saída deste perceptron é 1 apenas quando ambas as entradas são 0, e 0 caso contrário.
- Ele fornece uma representação complementar da lógica AND.

## Perceptron AND

- Este perceptron é treinado para representar a lógica da porta AND.
- A saída deste perceptron é 1 apenas quando ambas as entradas são 1, e 0 caso contrário.
- Ele fornece uma representação da parte "positiva" da lógica XOR.

### Combinando os Perceptrons

- A saída do perceptron NAND é usada como entrada para o perceptron AND.
- Assim, quando a lógica NAND retorna 1 (representando a negação da lógica AND), o perceptron AND não é ativado.
- Quando a lógica NAND retorna 0, o perceptron AND é ativado apenas quando ambas as entradas são 1, produzindo assim a saída desejada da porta XOR.

## Execução do Programa

```python
python3 perceptron.py
```

## Link do Vídeo

Link: https://drive.google.com/file/d/1c6vPDMjfHaGYqnHEjAxQGw08s4wAMZjE/view?usp=sharing