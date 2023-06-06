from flask import Flask, request, render_template

app = Flask(__name__)  #creates an instance of the flask class

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return f"You entered: {user_input}"
    else:
        return '''
               <form method="POST">
                   <label for="user_input">Enter some text:</label>
                   <input type="text" id="user_input" name="user_input">
                   <input type="submit" value="Submit">
               </form>
           '''

if __name__ == '__main__': #checks if the file is being run as the main program
    app.run() # starts the Flask application, which will listen for incoming requests and route them to the appropriate functions.
