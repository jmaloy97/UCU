from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)
  
@app.route('/', methods=["GET", "POST"])
def slider():
  if request.method == "POST":
    data = request.get_json()
    print("Light Level: " + data)
    return jsonify(data)
  else:
    return render_template('slider.html')
  

if __name__ == '__main__':
    app.run(debug=True)