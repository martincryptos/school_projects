import web
from gothonweb import map

urls = (
  '/game', 'GameEngine',
  '/', 'Index'
)

app = web.application(urls, globals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                    initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

#session = session

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
        #this is used to 'set-up' the session with starting values
        session.room = map.START
        web.seeother("/game")

class GameEngine(object):
    def GET(self):
        if session.room:
            #login.store_score
            return render.show_room(room=session.room, session=None)
        else:
            #login.store_score
            #login.reset_score
            return render.you_died()

    def POST(self):
        form = web.input(action=None, user=None, pass=None)
        #if login.login is None:
        #    login('user', 'pass')
        #else:
        #    pass
        if session.room and form.action:
            session.room = session.room.go(form.action)
            return render.show_room(room=session.room, session=session)
        else:
            web.seeother("/game")

if __name__ == "__main__":
    app.run()
