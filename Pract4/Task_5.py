class HTML:
    tag = '<body>\n'
    code = ''

    def p(self, phrase):
        self.code += '<p>'+phrase+'</p>\n'

    def __enter__(self):
        self.code += self.tag

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.code += '</'+self.tag[1:]

    def get_code(self):
        return self.code


html = HTML()
with html:
    with html:
        html.p('First String')
        html.p('Second String')
    with html:
        html.p('Second String')
print(html.get_code())
