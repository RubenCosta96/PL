from lexer import ArithLexer
from grammar import parse
from eval import Evaluator


if __name__ == "__main__":
    input_string = """
ESCREVER(365 * 2); -- 730
ESCREVER("Ola Mundo"); -- Olá, Mundo!
curso = "ESI";
ESCREVER("Olá, "<> curso); -- Olá, ESI
    """
    
    ast = parse(input_string)
    evaluator = Evaluator()
    evaluator.eval(ast)

