class Evaluator:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def eval(self, node):
        node_type = node[0]
        if node_type == 'program':
            return self.eval_program(node)
        elif node_type == 'assign':
            return self.eval_assign(node)
        elif node_type == 'write':
            return self.eval_write(node)
        elif node_type == 'func_def':
            return self.eval_func_def(node)
        elif node_type == 'func_call':
            return self.eval_func_call(node)
        elif node_type == 'binop':
            return self.eval_binop(node)
        elif node_type == 'concat':
            return self.eval_concat(node)
        elif node_type == 'num':
            return node[1]
        elif node_type == 'var':
            return self.variables[node[1]]
        elif node_type == 'str':
            return node[1]
        else:
            raise ValueError(f"Unknown node type: {node_type}")

    def eval_program(self, node):
        for stmt in node[1]:
            self.eval(stmt)

    def eval_assign(self, node):
        var_name = node[1]
        value = self.eval(node[2])
        self.variables[var_name] = value

    def eval_write(self, node):
        if isinstance(node[1], str):
            print(node[1])
        else:
            value = self.eval(node[1])
            print(value)

    def eval_func_def(self, node):
        func_name = node[1]
        params = node[2]
        body = node[3]
        self.functions[func_name] = (params, body)

    def eval_func_call(self, node):
        func_name = node[1]
        args = [self.eval(arg) for arg in node[2]]
        params, body = self.functions[func_name]
        local_vars = self.variables.copy()
        self.variables.update(zip(params, args))
        result = self.eval(body)
        self.variables = local_vars
        return result

    def eval_binop(self, node):
        op = node[1]
        left = self.eval(node[2])
        right = self.eval(node[3])
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left / right
        else:
            raise ValueError(f"Unknown operator: {op}")

    def eval_concat(self, node):
        left = self.eval(node[1])
        right = self.eval(node[2])
        return str(left) + str(right)
