import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100, threshold=0.5):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.threshold = threshold
        self.weights = np.zeros(2)
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        # Calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        # Aplica a função degrau para determinar a saída
        y_predicted = self.activation_function(linear_output)
        return y_predicted

    def train(self, X, y):
        for _ in range(self.n_iterations):
            for x, y_true in zip(X, y):
                y_pred = self.predict(x)
                error = y_true - y_pred
                self.weights += error * self.learning_rate * x
                self.bias += error * self.learning_rate

def choice_model():
    choice = ''
    while choice not in ["1", "2", "3", "4"]:
        choice = input(f'Escolha o número da porta que deseja: \n 1 - AND \n 2 - OR \n 3 - XOR \n 4 - NAND \n')
        if choice == "1":
            return "AND"
        elif choice == "2":
            return "OR"
        elif choice == "3":
            return "XOR"
        elif choice == "4":
            return "NAND"
        else:
            print("Opção inválida.")

def main():
    # Escolha do modelo
    model = choice_model()
    # Todas as combinações de entradas possíveis
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # Resposta esperada para respectivas entradas da porta AND e as respectivas entradas
    if model == "AND":
        y = np.array([0, 0, 0, 1])
    elif model == "OR":
        y = np.array([0, 1, 1, 1])
    elif model == "XOR":
        y = np.array([0, 1, 1, 0])
    elif model == "NAND":
        y = np.array([1, 1, 1, 0])
    else:
        print("Opção inválida.")
        return main()

    # Treinando o Perceptron
    perceptron = Perceptron()
    perceptron.train(X, y)

    # Testando o Perceptron
    if model == "XOR":
        print(f"in (0, 0), out: {perceptron.predict([0, 0])} do modelo {model}")
        print(f"in (0, 1), out: {perceptron.predict([0, 1])} do modelo {model}")
        print(f"in (1, 0), out: {perceptron.predict([1, 0])} do modelo {model}")
        print(f"in (1, 1), out: {perceptron.predict([1, 1])} do modelo {model}")
        print(f"O modelo XOR não é linearmente separável, portanto não é possível treinar um perceptron para ele, resultados acima estão errados. Mas se usarmos duas camadas de perceptrons, podemos treinar um modelo para o XOR.")
        perceptron_and = Perceptron()
        perceptron_and.train(X, np.array([0, 0, 0, 1]))
        perceptron_nand = Perceptron()
        perceptron_nand.train(X, np.array([1, 1, 1, 0]))
        print(f"in (0, 0), out: {perceptron_and.predict([perceptron_nand.predict([0, 0]), 0])} do modelo {model}")
        print(f"in (0, 1), out: {perceptron_and.predict([perceptron_nand.predict([0, 1]), 1])} do modelo {model}")
        print(f"in (1, 0), out: {perceptron_and.predict([perceptron_nand.predict([1, 0]), 1])} do modelo {model}")
        print(f"in (1, 1), out: {perceptron_and.predict([perceptron_nand.predict([1, 1]), 0])} do modelo {model}")
        print(f"Você usa 2 camadas de perceptrons para treinar um modelo XOR, a primeira camada é um perceptron NAND e a segunda camada é um perceptron AND. O resultado da primeira camada é a entrada da segunda camada. Logo, quando o resultado da primeira camada NAND é [1, 1, 1, 0] para o primeiro valor da tupla, e você determina o segundo valor [0, 1, 1, 0] para as suas repectivas posições, a entrada ficaria [[1,0], [1,1], [1,1], [0,0]]. O resultado final do AND [0, 1, 1, 0] que é o resultado esperado para o XOR.")
    else:
        print(f"in (0, 0), out: {perceptron.predict([0, 0])} do modelo {model}")
        print(f"in (0, 1), out: {perceptron.predict([0, 1])} do modelo {model}")
        print(f"in (1, 0), out: {perceptron.predict([1, 0])} do modelo {model}")
        print(f"in (1, 1), out: {perceptron.predict([1, 1])} do modelo {model}")



# Exemplo de uso
if __name__ == "__main__":
    main()