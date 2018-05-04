osi = True
try: import os
except ImportError: osi = False
class HMOD_ERROR(SyntaxError): None
class HMOD():
    def PERCENTAGE(full_number, percentage): return float(float(full_number) * float(float(percentage) * 0.01))
    def PI(): return 3.14159265358797
    def DELETE_CHARACTER(string, char_no):
        new = ''
        for _ in range(len(string)):
            if _ != char_no: new = str(new) + string[_]
        return new
    def ADD(string, addon): return (str(string) + str(addon))
    def DELETE_ALL_TYPE(string, character):
        if len(character) != 1: raise HMOD_ERROR('Character length must be <1>.')
        else:
            new = ''
            for _ in string:
                if str(_) != str(character): new = HMOD.ADD(new, _)
            return new
    def OPEN_HTML(html_text, docname):
        doc = open((str(docname) + '.html'), 'w')
        doc.write(html_text)
        doc.close()
    def WRTIE_TXT_DOC(contents, docname):
        doc = open((str(docname) + '.txt'), 'w')
        doc.write(contents)
        doc.close()
    def GET_CONTENTS(docname):
        doc = open(docname, 'r')
        c = (doc.read())
        doc.close()
        return c
    def CDIRP(additional_path):
        global osi
        if osi == True: return (str(os.getcwd()) + str(additional_path))
        else: raise HMOD_ERROR('Could not import "OS" module.')
    
