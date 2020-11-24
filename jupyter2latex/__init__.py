"""
Eduardo P. Titello - 2020 - github.com/dutitello
"""

from IPython.display import display

def df2table(df, caption='', label=''):
    # Everything must be strings
    label = str(label)
    caption = str(caption)

    # Generate df as latex table
    latexdf = df.to_latex()
    latex = r'''
    \begin{table}[h!]
    \centering
    \caption{''' + caption + '''}
    {''' + latexdf + '''}
    \label{''' + label + '''}
    \end{table}
    '''

    # Generate df as html table
    htmldf = df.to_html()
    html = f'''
    <div name='{label}' align='center'>
    {caption}<br>
    {htmldf}
    </div>'''

    # Markdown format 
    md = caption + '\n\n' + df.to_markdown() + '\n\n<br>\n\n'

    # Now do the magic!
    # Use IPython display to print diferent formats
    display({'text/latex': latex, 'text/html': html, 'text/markdown': md}, raw=True)




class latexfigure:
    """

     AINDA NÃO FUNCIONA!

    A class to enumerate latex figures
    """
    def __init__(self, caption='', label=''):
        # Everything must be strings
        self.label = str(label)
        self.caption = str(caption)

        # Open latex figure tags 
        # Since latex uses {} i couldn't use .format ...
        latex = r'\begin{figure}[h!] \centering \caption{' + self.caption + '}'
        
        # HTML tags
        html = f'<div name=\"{self.label}\" align=\"center\">{self.caption}<br>'

        # Now do the magic!
        # Use IPython display to print diferent formats
        display({'text/latex': latex, 'text/html': html}, raw=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Close latex figure tags 
        latex = r' \label{' + self.label + '}\end{figure}'
        html = '</div>'
        display({'text/latex': latex, 'text/html': html}, raw=True)