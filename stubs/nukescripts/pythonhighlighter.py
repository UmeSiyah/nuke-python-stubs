import re

import PySide2


class PythonHighlighter(PySide2.QtGui.QSyntaxHighlighter):
    def __init__(self, doc, parent=None):
        super(PythonHighlighter, self).__init__(parent)

        self.setDocument(doc)

        self._rules = []

        self._keywords = PySide2.QtGui.QTextCharFormat()
        self._keywords.setForeground(PySide2.QtGui.QColor(236, 119, 180))
        self._keywords.setFontWeight(PySide2.QtGui.QFont.Bold)
        self._rules.append(
            {
                'pattern': '\\b(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)\\b',
                'format': self._keywords
            }
        )

        # String Literals
        self._strings = PySide2.QtGui.QTextCharFormat()
        self._strings.setForeground(PySide2.QtGui.QColor(240, 137, 143))
        self._rules.append(
            {
                'pattern': '"([^"\\\\]|\\\\.)*"',
                'format': self._strings
            }
        )

        self._stringsSingle = PySide2.QtGui.QTextCharFormat()
        self._stringsSingle.setForeground(PySide2.QtGui.QColor(240, 137, 143))
        self._rules.append(
            {
                'pattern': "'([^'\\\\]|\\\\.)*'",
                'format': self._stringsSingle
            }
        )

        # Comments
        self._comment = PySide2.QtGui.QTextCharFormat()
        self._comment.setForeground(PySide2.QtGui.QColor(145, 220, 147))
        self._rules.append(
            {
                'pattern': '#[^\n]*',
                'format': self._comment
            }
        )

    def highlightBlock(self, text):
        text = str(text)
        for rule in self._rules:
            expression = rule['pattern']

            if len(text) > 0:
                results = re.finditer(expression, text)

                # Loop through all results
                for result in results:
                    index = result.start()
                    length = result.end() - result.start()
                    self.setFormat(index, length, rule['format'])
