from flask import Flask, request, jsonify, render_template
from bs4 import BeautifulSoup
import requests,json,re,random,string
from urllib.parse import quote


app = Flask(__name__)


# THE STATUS OF THE PROJECT
#mode = 'development'
mode = 'production'


# GLOBAL SUPER CHANGABLE VARIABLES
yr = 10
sms = 3356 # current semester





# some useful functions
class usefulUtils:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def random_csrf(length=25):
        characters = string.ascii_letters + string.digits + string.punctuation
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    def remove_first_item(dictionary):
            if dictionary:
                # Create a new dictionary excluding the first item
                new_dict = {key: value for key, value in list(dictionary.items())[1:]}
            else:
                new_dict = {}

            return new_dict

    def clean_schedule(schedule):
        cleaned_schedule = []

        for day_schedule in schedule:
            cleaned_day_schedule = [item for item in day_schedule if item != "" and item != []]
            if cleaned_day_schedule:
                cleaned_schedule.append(cleaned_day_schedule)

        return cleaned_schedule



    def parse_schedule(schedule_data):
        result = []

        for entry in schedule_data:
            # Split the entry into its components
            components = [item.strip() for item in entry.split(';')]

            # Extracting individual details
            time_info = components[0].split(', ')[0].split(' - ')
            start_time, end_time = time_info[0], time_info[1]

            coarse = components[0].split(', ')[1]
            staff = components[1].split(': ')[1]
            students = components[2].split(': ')[1]
            venue = components[3].split(': ')[1]

            if coarse[:3] == "Mon":
                coarse = coarse[6:]
            elif coarse[:3] == "Tue":
                coarse = coarse[7:]
            elif coarse[:3] == "Wed":
                coarse = coarse[9:]
            elif coarse[:3] == "Thu":
                coarse = coarse[8:]
            elif coarse[:3] == "Fri":
                coarse = coarse[6:]
            else:
                pass # fatal error occured


            # Create a dictionary for the entry
            entry_dict = {
                'start_time': start_time,
                'end_time': end_time,
                'coarse': coarse,
                'staff': staff,
                'students': students,
                'venue': venue
            }

            # Append the dictionary to the result list
            result.append(entry_dict)

        return result



    class HTMLParser:
        def __init__(self, html_string):
            self.html_string = html_string
            self.options = {}

        def parse_html(self):
            # the option regex
            pattern = re.compile(r'<option value="([^"]*)">([^<]*)</option>')

            matches = pattern.findall(self.html_string)

            # Populate the options dictionary with matches
            for match in matches:
                value, text = match
                self.options[value] = text

        def get_options(self):
            return self.options
    



class getRatibaFromUdom:
    def __init__(self, semester, year, csrf):
        self.semester, self.year, self.csrf = semester,year,csrf

        # BOGUS USER AGENT ********
        # Specify custom headers
        self.headers = {
            'User-Agent': 'YourCustomUserAgent/1.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://ratiba.udom.ac.tz/',
            'Custom-Header': 'YourCustomValue'
        }

    
    def category(self):
        paramsCategory = {
            '_csrf-backend': f'{self.csrf}',
            'year': f'{self.year}',
            'semester': f'{self.semester}',
            'option': '',
            'type': '',
            'data': ''
        }
        url = f"https://ratiba.udom.ac.tz/index.php/downloads/fetch-categories"
        sampleData = requests.get(url,params = paramsCategory, headers = self.headers)
        sample = sampleData.text
        return sample

    def option(self):
        paramsOption = {
            '_csrf-backend': f'{self.csrf}',
            'year': f'{self.year}',
            'semester': f'{self.semester}',
            'option': '',
            'type': '1',
            'data': ''
        }
        url = f"https://ratiba.udom.ac.tz/index.php/downloads/opt"
        sampleData = requests.get(url,params = paramsOption, headers = self.headers)
        sample = sampleData.text
        return sample


    def programme(self):
        paramsProgramme = {
            '_csrf-backend': f'{self.csrf}',
            'year': f'{self.year}',
            'semester': f'{self.semester}',
            'option': 'programme',
            'type': '1',
            'data': ''
        }
        url = f"https://ratiba.udom.ac.tz/index.php/downloads/data"
        sampleData = requests.get(url,params = paramsProgramme, headers = self.headers)
        sample = sampleData.text
        return sample

    def table(self,option,data):
        paramsTable = {
            '_csrf-backend': f'{self.csrf}',
            'year': f'{self.year}',
            'semester': f'{self.semester}',
            'option': f'{option}',
            'type': '1',
            'data': f'{data}'
        }
        url = f"https://ratiba.udom.ac.tz/index.php/downloads/view"
        sampleData = requests.get(url,params = paramsTable, headers = self.headers)
        

        #sampleData = open('C:/Users/masterplan/Desktop/server/smartTime/api/table.txt','r')
        

        #sample = sampleData 
        sample = sampleData.text
        return sample
        




class jsonMake:
    
    def __init__(self,x,y,z):
        self.x,self.y,self.z = x,y,z
    
    def category(data):
        # ...
        utils_instance = usefulUtils(1, 2, 3)
        parser = utils_instance.HTMLParser(data)

        # Parse the HTML string
        parser.parse_html()

        # Get the options dictionary
        _dict = parser.get_options()

        category = {
            "status":"success",
            "code": 200,
            "data": usefulUtils.remove_first_item(_dict) # the first item is header
        }

        return category # json.dumps(category, indent=2)

    def option(data):
        # ...
        utils_instance = usefulUtils(1, 2, 3)
        parser = utils_instance.HTMLParser(data)

        # Parse the HTML string
        parser.parse_html()

        # Get the options dictionary
        _dict = parser.get_options()

        option = {
            "status":"success",
            "code": 200,
            "data": usefulUtils.remove_first_item(_dict)
        }

        return option # json.dumps(category, indent=2)
    

    def programme(data):
        utils_instance = usefulUtils(1, 2, 3)
        parser = utils_instance.HTMLParser(data)

        # Parse the HTML string
        parser.parse_html()

        # Get the options dictionary
        _dict = parser.get_options()

        programme = {
            "status":"success",
            "code": 200,
            "data": usefulUtils.remove_first_item(_dict)
        }

        return programme # json.dumps(category, indent=2)

    
    def table(data):
        soup = BeautifulSoup(data, 'html.parser')
        h4_content = soup.find('h4').text.strip()
        table = soup.find('table')
        table_data = []

        for row in table.find_all('tr'):
            row_data = [cell.text.strip() for cell in row.find_all('td')]
            table_data.append(row_data)

        # Convert table data to JSON
        table_data = usefulUtils.clean_schedule(table_data)

        time_table = {
            "status":"success",
            "code": 200,
            "title" : h4_content,
            "data": {
                "monday": usefulUtils.parse_schedule(table_data[0][1:]),
                "tuesday": usefulUtils.parse_schedule(table_data[1][1:]),
                "wednesday": usefulUtils.parse_schedule(table_data[2][1:]),
                "thursday": usefulUtils.parse_schedule(table_data[3][1:]),
                "friday": usefulUtils.parse_schedule(table_data[4][1:])
            }
        }
        return time_table



@app.route('/get/<get>')
def preApi(get):
    csrf = quote(usefulUtils.random_csrf())
    
    getRatiba = getRatibaFromUdom(sms,yr,quote(csrf.encode('utf-8')))
    if get == 'category':
        categoryHtml = getRatiba.category()
        responseJson = jsonMake.category(categoryHtml)

    elif get == 'option':
        optionHtml = getRatiba.option()
        responseJson = jsonMake.option(optionHtml)
   

    elif get == 'programme':
        programmeHtml = getRatiba.programme()
        responseJson = jsonMake.programme(programmeHtml)   
    else:
        return "invalid request"

    # finally return the response
    return responseJson



@app.route('/api',methods = ['POST','GET'])
def api():

    if 'option' in request.form and 'programme' in request.form:
        option_which = request.form['option']
        programme = request.form['programme']

        # Check if the values are not empty
        if option_which and programme:
            csrf = quote(usefulUtils.random_csrf())
    
            getRatiba = getRatibaFromUdom(sms,yr,quote(csrf.encode('utf-8')))
            
            tableHtml = getRatiba.table(option_which,programme)
            tableJson = jsonMake.table(tableHtml)
            return tableJson

        else:
            # Either 'username' or 'password' is empty
            return 'the values are empty' # error

    else:
        # 'username' or 'password' is not present in the form data
        return 'false post values not found' # error the values not present



    
        



# Handling about section
@app.route("/")
def home():
    context = {
           'title': 'Udom Ratiba API Documentation',
    }
    return render_template('/index.txt',**context)






                            

#                 ####################
#                 ####################
#                 # SERVER  SETTINGS #
#                 ####################
#                 ####################


# Handling not found err
@app.errorhandler(404)
def page_not_found(error):
	not_found = {
            "status":"failed",
            "code": 400,
        }
	return not_found


# redirecting ensuring securingness through 'https'
@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)


        








# Launching the app
if __name__ == '__main__':
    if mode == 'development':
        app.run(debug=True)
    elif mode == 'production':
        app.run()







# the procedures
# one : get the purpose of the request
# two : get the request headers from the client
# three: get the required data from the server according to request of the client
# four : 
