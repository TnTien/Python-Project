import webbrowser
import pageGenerator_func

#   Creates new HTML page called test.html if one does not exist.
#   If it exists, will update the body
def createPage(self, newText):

    #   Opens up text file and will be able to read and write
    f = open('test.html', 'w')

    #   HTML. Text will update base on 'newText'
    message = """<html>
    <body>
        <h1>
        {}
        </h1>
    </body>
</html>""".format(newText)

    #   Writes text to file
    f.write(message)
    #   Saves and closes the opened text file
    f.close()

    #   Will open html file in browser
    webbrowser.open_new('test.html')
    
if __name__ == "__main__":
    pass
