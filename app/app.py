import pathlib
import textwrap
import os
import google.generativeai as genai
import json

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

from flask import Flask, request, jsonify
app = Flask(__name__)


def json_to_string_with_keys(json_data):
    """Converts JSON data into a string with keys and values."""
    if not isinstance(json_data, dict):
        raise ValueError("Input must be a JSON dictionary.")

    items = [f"{key}: {value}" for key, value in json_data.items()]
    return ", ".join(items)



def ask_gemini(req):
    """Takes a String argument to Gemini for prompt tuning."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(req)
    return response.candidates[0].content.parts[0].text

def add_company_tweets_to_json(company, tweets):
	"""Provides a company name and relevant Tweets we are working with to the JSON prompt"""
	with open('./RISE.json', "r") as json_file:
		data = json.load(json_file)
		if "COMPANY" in data:
			data["COMPANY"] = company
		if "INPUT" in data:
			data["INPUT"] = tweets
	return data


	


@app.route('/ask', methods=['POST'])
def ask():
	data = add_company_tweets_to_json(request.get_json()["COMPANY_TWITTER_HANDLE"], request.get_json()["COMPANY_TWEETS"])

	print(data)
	return ask_gemini(json_to_string_with_keys(data))

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
