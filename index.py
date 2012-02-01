import web

urls = ("/.*", "hello",
        "/(.*)/", 'redirect')
app = web.application(urls,globals())

class hello:
    def GET(self):
        return 'hello world'

class redirect:
    def GET(self,path):
        web.seeother('/', path)
    
if __name__ == "__main__":
    app.run()
