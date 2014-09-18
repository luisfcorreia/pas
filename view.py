import web
import view, config
from view import render

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.base(view.listing())

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()

[dmarc@dmarc pas]$ cat view.py
import web
#import db
import config

t_globals = dict(
  datestr=web.datestr,
)
render = web.template.render('templates/', cache=config.cache, globals=t_globals)
render._keywords['globals']['render'] = render

def listing():
    #l = db.listing(**k)
    #return render.listing(l)
    return render.listing()
