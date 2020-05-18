"""
with clause
"""
# with open('test.txt', 'w') as f:
#     f.write('test!')

"""
try-except clause
"""
# f = open('test.txt', 'w')
# try:
#     f.write('test!')
# except:
#     f.close()

"""
Custom object with clause
"""
# class TestClass:
# def __init__(self, name):
#     self.name = name

# def __enter__(self):
#     self.file = open(self.name, 'w')
#     return self.file

# def __exit__(self, exc_type, exc_val, exc_tb):
#     if self.file:
#         self.file.close()


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('\t' * self.level + text)


with Indenter() as indent:
    # indent level = 1
    indent.print('Some')
    with indent:
        # indent level = 2
        indent.print('Thing')
    # indent level = 1
    with indent:
        # indent level= 2
        indent.print('New')
    # indent level = 1
# indent level = 0
