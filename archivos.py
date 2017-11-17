from pip._vendor.distlib.database import _Cache


class LectorArchivos:

    def creaArchivos(self):
        file = open("nombre.csv","r")

        html =""
        for i in file:
            html += "<p>" + i + "</p>"

        file.close()

        return html