from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def checkerboard():
    return render_template("index.html", rows=8, columns=8, color1="blue", color2="yellow")

@app.route('/<int:rows>')
def checkerboardrows(rows):
    return render_template("index.html", rows=rows, columns=8, color1="blue", color2="yellow")

@app.route('/<int:rows>/<int:columns>')
def checkerboardrowscolumns(rows, columns):
    return render_template("index.html", rows=rows, columns=columns, color1="blue", color2="yellow")

@app.route('/<int:rows>/<int:columns>/<color1>/<color2>')
def checkerboardrowscolumnscolors(rows, columns, color1, color2):
    return render_template("index.html", rows=rows, columns=columns, color1=color1, color2=color2)




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.