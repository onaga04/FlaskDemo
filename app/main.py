import os
import cgi, cgitb 
import random

form = cgi.FieldStorage() 


from flask import Flask, request, redirect, render_template, session, url_for, g, jsonify

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/', methods=['GET','POST'])
def randomizer():
  list1 = []
  # if request.method == 'POST':
  #   text_box_value = request.form['myTextarea']
  # if form.getlist('myTextarea'):
  string1 = ""
  blank = " "
  noblank = ""
  textarea = []
  if 'text_box' in request.args:
     textarea1 = request.args.get('text_box')
     textarea2 = textarea1.split('\n')
     for word in textarea2:
       if word not in blank:
          textarea.append(word)
     # remove empty elements or ones with only spaces
     #for word in textarea: 
     #    list1.append(word)
     random.shuffle(textarea)
     string1 = '\n'.join(textarea)
  if 'json' in request.args:
      return jsonify(textarea)
 # def calculate():
 #   t = {'a': 0, 'b': 0, 'c': 0}   # josh
 #   if request.method == 'POST':
 #     t['a'] = request.form['a']
 #     t['b'] = request.form['b']
 #   elif 'a' in request.args:
 #     t['a'] = request.args.get('a')
 #     t['b'] = request.args.get('b')
 #   t['c'] = int(t['a']) * int(t['b'])
 
 
 
  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)
  if 'times' not in session:
    session['times'] = 0
  session['times'] += 1
    
  return render_template('index.html', string1 = string1, times = session['times']) # Send t to the template

@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('randomizer'))  # Calculate is the fn name above!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!