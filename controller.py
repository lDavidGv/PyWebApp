import web
from models import RegisterModel, LoginModel, Posts

urls = (
    '/','Home',
    '/register','Register',
    '/postregistration', 'Postregistration',
    '/login', 'Login',
    '/logout', 'Logout',
    '/check-login', 'CheckLogin',
    '/post-activity', 'PostActivity'
)
web.config.debug = False
app = web.application(urls,globals())
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer ={'user': None})
session_data = session.initializer
render = web.template.render("views/templates", base = "MainLayout", globals={'session': session_data, 'current_user': session_data["user"]})

#classes routes

class Home:
    def GET(self):
        return render.Home()
class Register:
    def GET(self):
        return render.register()
class Login:
    def GET(self):
        return render.login()
class Postregistration:
    def POST(self):
        data = web.input()
        reg_module=RegisterModel.RegistrationModel()
        reg_module.inset_user(data)
class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        correct = login.cu(data)

        if correct:
            session_data["user"]=correct
            return correct
        return "error"
class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']

        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"

class Logout:
    def GET(self):
        session['user'] = None
        session_data['user'] = None
        session.kill()
        return "success"

if __name__ == "__main__":
    app.run()