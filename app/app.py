import pathlib
import textwrap
import os
import google.generativeai as genai

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

from flask import Flask
app = Flask(__name__)

@app.route('/ask/<question>', methods=['GET', 'POST'])
def hello():

	return ask_gemini(question))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)



def ask_gemini(req):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(req)
    return response.candidates[0].content.parts[0].text
    



