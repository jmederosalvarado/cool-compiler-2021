from coolpyler.visitors.cool.type_collector import TypeCollectorVisitor


class Visitor:
    def __init__(self, errors=None):
        self.visitors = [TypeCollectorVisitor(errors)]

    def visit(self, ast):
        for visitor in self.visitors:
            ast = visitor.visit(ast)
        return ast