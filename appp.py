import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index(object):
    def GET(self):
        great_thing = "I am optional", "As am I", "so are you"
        return render.foo(great_thing = great_thing)

if __name__ == "__main__":
    app.run()
