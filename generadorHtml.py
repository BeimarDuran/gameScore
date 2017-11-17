class GeneradorHTML:
    def creaHeader(self):
        return "<head> </head>"

    def createList(self, listaDeCosas):
        list = "<ol>"

        for i in listaDeCosas:
            list += "<li>" + str(i) + "</li>"

        list += "</ol>"

        return list