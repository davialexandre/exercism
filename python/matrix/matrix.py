class Matrix:
    def __init__(self, matrix_string):
        self._rows = []

        for line in matrix_string.splitlines():
            items = [int(i) for i in line.split()]
            self._rows.append(items)

    def row(self, index):
        return self._rows[index - 1]

    def column(self, index):
        column = []

        for row in self._rows:
            column.append(row[index - 1])

        return column
