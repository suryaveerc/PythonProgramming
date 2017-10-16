from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
from DBcm import UserDatabase
from threading import Thread
from time import sleep
app = Flask(__name__)
app.config['dbconfig'] = {'host': '192.168.99.100', 'user':'vsearch', 'password':'vsearch', 'database':'vsearchlogDB','port':'32768'}

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to the search4letters webpage')

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'

#@app.route('/')
#def hello() -> '302':
    #return redirect('/entry')

@app.route('/viewlog')
def view_the_log() -> 'html':
    
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    
    _SQL = """ select Phrase, Letters, Remote_addr, ser_agent, Results from log"""
    with UserDatabase(app.config['dbconfig']) as cursor:
        content = cursor.execute(_SQL)
    #log = open('vsearch.txt','r') 
    #with open('vsearch.txt') as log:
        #for line in log:
            #log_list.append([])
            #for item in line.split('|'):
                #log_list[-1].append(escape(item))
            #print(log_list)   
        return render_template('viewlog.html', the_title='View Log', the_row_titles = titles, the_data = content)


@app.route('/search4', methods= ['POST'])
def do_search() -> 'html':
    
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        _SQL = """ insert into log (phrase, letters, ip, browser_string, results) values(%s,%s,%s,%s,%s)"""
        sleep(15)
        with UserDatabase(app.config['dbconfig']) as cursor:
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res, ))    
        """
        with open('vsearch.txt','a') as logFile:
            #print(req.form,file=logFile, end='|')
            #print(req.remote_addr,file=logFile, end='|')
            #print(req.user_agent,file=logFile, end='|')
            #print(res,file=logFile)
            
            print(req.form, req.remote_addr, req.user_agent, res, file=logFile, sep='|')
         """       
    
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    
    #log_request(request,results)
    """
    The log_request thread will fail as the do_search functions completes instantaneously.
    The log_request method does not have access to the passed parameters as they are garbage collected.
    Flask provides a decorator @copy_current_request_context which keeps the context available to the metods in thread.
    However, this requires the method to be defined inside the calling method.
    """
    
    
    logThread = Thread(target=log_request, args  = (request,results))
    logThread.start()
    return render_template('results.html',
                           the_title='Here are your results:', 
                           the_phrase=phrase, 
                           the_letters=letters, 
                           the_results=results) 



#Run the function if the module is run directly. If imported from other modules __name__ returns vsearch4web (modulename) and the if check fails.
if __name__ == '__main__':
    app.run(debug=True)
