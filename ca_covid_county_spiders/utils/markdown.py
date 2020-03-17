import html2text

textGen = html2text.HTML2Text()
textGen.body_width = 0

def markdownIt(html):
    md = textGen.handle(html)
    return md
