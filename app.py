from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return """
    <form action="/froyo_results" method="GET">
        What is your favorite Fro-Yo flavor? <br/>
        <input type="text" name="flavor"><br/>
        What are your favorite Fro-Yo Toppings? <br/>
        <input type="text" name="toppings"> <br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    froyo_flavor = request.args.get('flavor')
    froyo_toppings = request.args.get('toppings')
    return f"You ordered {froyo_flavor} flavored Fro-Yo with toppings {froyo_toppings}!"

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        Enter your favorite color: <br/>
        <input type="text" name="color" /><br/>
        Enter your favorite animal: <br/>
        <input type="text" name="animal" /><br/>
        Enter your favorite city: <br/>
        <input type="text" name="city" /><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    fav_color = request.args.get('color')
    fav_animal = request.args.get('animal')
    fav_city = request.args.get('city')
    return f"Wow, I didn't know {fav_color} {fav_animal}s lived in {fav_city}!"

@app.route('/secret_message', methods=['GET'])
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter your secret message: <br/>
        <input type="text" name="message" /><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    message = request.form.get('message')
    sortedMessage = ''.join(sorted(message))
    return f"Here's your secret message!<br/> {sortedMessage}"

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return """
    <form action="/calculator_results" method="GET">
        Please enter 2 numbers and select an operator.<br/><br/>
        <input type="number" name="operand1">
        <select name="operation">
            <option value="add">+</option>
            <option value="subtract">-</option>
            <option value="multiply">*</option>
            <option value="divide">/</option>
        </select>
        <input type="number" name="operand2">
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    operand1 = request.args.get("operand1")
    operand2 = request.args.get("operand2")
    operation = request.args.get("operation")

    if operation == 'add':
        result = int(operand1) + int(operand2)
    elif operation == 'multiply':
        result = int(operand1) * int(operand2)
    elif operation == 'divide':
        result = int(operand1) / int(operand2)
    elif operation == 'subtract':
        result = int(operand1) - int(operand2)


    return f"You chose to {operation} {operand1} and {operand2}. Your result is: {result}"


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
