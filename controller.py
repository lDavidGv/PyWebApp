import web
from models import RegisterModel, LoginModel

urls = (
    '/','Home',
    '/register','Register',
    '/postregistration', 'Postregistration',
    '/login', 'Login',
    '/check-login' 'CheckLogin'
)
render = web.template.render("views/templates", base = "MainLayout")
app = web.application(urls,globals())

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
            return correct
        return "error"

if __name__ == "__main__":
    app.run()