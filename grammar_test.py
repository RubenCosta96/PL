# Importa a classe ArithGrammar do seu arquivo
from grammar import ArithGrammar
import ply.yacc as yacc


# Cria uma instância da classe ArithGrammar
parser = ArithGrammar()

# Constroi o analisador léxico e sintático
parser.build()

# Expressão aritmética de exemplo
input_text = "3 + (4 * 2)"

# Faz o parsing da expressão e calcula o resultado
resultado = parser.parse(input_text)
print("Resultado:", resultado)