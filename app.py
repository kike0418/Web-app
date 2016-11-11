import web
import json


render = web.template.render('views/')
urls = ('/index(.*)', 'index', '/mapa', 'mapa')

class index:
    def GET(self, data):
        data = []
        with open('data200.json', 'r') as file:
            temp = json.load(file)
            data = temp['results']
        return render.index(data)

class mapa:
    def GET(self): 
        ubi = []
        with open('data200.json', 'r') as file:
            temp_data = json.load(file)
            ubi = temp_data['results']
        return render.mapa(ubi)        
         
if __name__ == '__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()  