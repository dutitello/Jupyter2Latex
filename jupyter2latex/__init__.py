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

    # Now do the magic!
    # Use IPython display to print diferent formats
    display({'text/latex': latex, 'text/html': html}, raw=True)
