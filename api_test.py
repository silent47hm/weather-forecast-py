from flask import Flask, render_template_string, request,send_from_directory
import os
import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"53.1,-0.13"}

headers = {
	"x-rapidapi-key": "9dc28790d2mshdb96c2569b20f20p1e3121jsn2806faa392ac",
	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}

app = Flask(__name__,static_folder='uploads')


@app.route('/maaz-weather')
def index():
    ## Get the location query from the URL parameters
    location_query = request.args.get('query', '53.1,-0.13')  # Default to some coordinates

    # API request parameters
    querystring = {"q": location_query}

    # Make the API request
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Extract relevant data from the API response
    location = data.get('location', {}).get('name', 'Unknown')
    temperature = data.get('current', {}).get('temp_c', 'N/A')
    condition = data.get('current', {}).get('condition', {}).get('text', 'Unknown')
    latitude = data.get('location',{}).get('lat', 'N/A')

    # Render the HTML template with the API data

    fname = "index.html"
    html_file = open(fname, 'r', encoding='utf-8')
    source_code = html_file.read() 
    print(source_code)

    # return render_template_string(HTML_TEMPLATE, location=location, temperature=temperature, condition=condition)
    return render_template_string(source_code, location=location, temperature=temperature, condition=condition ,latitude = latitude)


if __name__ == '__main__':
    app.run(debug=True)