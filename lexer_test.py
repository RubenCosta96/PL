from lexer import ArithLexer

exemplos = [ 
	"""FUNCAO fib( 0 ),: 0 ;
FUNCAO fib( 1 ),: 0 ;
FUNCAO fib( n ):
a = fib(n-1);
b = fib(n-2);
a + b;
FIM
fib5 = fib(5);"""]

for frase in exemplos:
	print(f"----------------------")
	print(f"frase: '{frase}'")
	al = ArithLexer()
	al.build()
	al.input(frase)
	print('tokens: ',end="")
	while True:
		tk = al.token() 
		if not tk: 
			break
		print(tk,end="")
	print()	

