import web

urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        greeting = "Welcome to my Dungeon"
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()
