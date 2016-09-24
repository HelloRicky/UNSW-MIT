from tex import latex2pdf

document = """
... \documentclass{article}
... \begin{document}
... Hello, World!
... \end{document}
... """

latex2pdf(document)
