class A:
    def __init__(self):
        pass
    def __dict__(self):
        try:
            return self._get_current_object().__dict__
        except RuntimeError:
            raise AttributeError('__dict__')
        

a = A()
a['a'] = "12"

from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'YouWillNeverGuess'

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    print("sfdfd")
    session['user'] = user
    return 'User value set to: ' + session['user']
@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

@app.route('/login')
def do_login():
    session['logged_in']=True
    
    return 'You are now not logged in.'
if __name__ == '__main__':
    app.run(debug=True)


