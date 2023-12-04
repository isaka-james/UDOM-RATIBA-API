# Udom Ratiba API

[Full Documentation Here](https://udom-ratiba-api.vercel.app/)

## Overview
Udom Ratiba API is a custom-made Flask application hosted on Vercel. It functions as a robust API, facilitating the extraction of schedule information from the University of Dodoma (Udom) Ratiba portal through web scraping. Developers are encouraged to leverage this API to seamlessly integrate Udom's schedule data into their applications and programs.

## Table of Contents
- [API Base URL](#api-base-url)
- [API Endpoints](#api-endpoints)
  - [Get Categories](#1-get-categories)
  - [Get Options](#2-get-options)
  - [Get Programs](#3-get-programs)
  - [Get Schedule Table](#4-get-schedule-table)
- [Usage Example](#usage-example)
- [How to Use](#how-to-use)
- [Error Handling](#error-handling)
- [Server Settings](#server-settings)
- [Author](#author)
- [License](#license)

## API Base URL
[https://udom-ratiba-api.vercel.app/](https://udom-ratiba-api.vercel.app/)

## API Endpoints

### 1. Get Categories
- **Endpoint**: `/get/category`
- **Method**: GET ( https://udom-ratiba-api.vercel.app/get/category )
- **Description**: You can check the type of the timetable available, When you fetch most of the time you will find that it only says *Teaching*, this is because there are two category *Teaching* and *Examination*, since the examination season is not yet nearer then you will find only  the *Teaching timetable type*.
  
- The sample output of the request

```python
{
  "code": 200,
  "data": {
    "1": "Teaching"
  },
  "status": "success"
}
```

### 2. Get Options
- **Endpoint**: `/get/option`
- **Method**: GET ( https://udom-ratiba-api.vercel.app/get/option )
- **Description**: Here you can see that you want your timetable can be categorized by either *coarse*,*programme*,*venue* and so on.. , Disclaimer: now we only support fetching by *programme*, hope we can provide with more categories.
- Sample output
```python
{
  "code": 200,
  "data": {
    "course": "By Course ",
    "instructor": "By Instructor",
    "programme": "By Programme ",
    "room": "By Venue "
  },
  "status": "success"
}

```


### 3. Get Programs
- **Endpoint**: `/get/programme`
- **Method**: GET ( https://udom-ratiba-api.vercel.app/get/programme )
- **Description**: This is very important, here you can see all the programmes with the appropiate code of each programme, It is **crutual** to know the code of the programme you want to fetch, because with that code you can fetch the timetable in the following steps..
  
- sample output
```python
{
  "code": 200,
  "data": {
    "9763": "BAENGLISH3 - CHSS",
    "9764": "BATI3 - CHSS",
    "9765": "BAARCA1 - CHSS",
    "9766": "BACHT1 - CHSS",
    ...
    ...
    ....
    "10096": "N4 - SNPH & SMD",
    "10097": "MSCAC&FIN(EV)2 - CoBE",
    "10098": "HIS2 - SNPH & SMD",
    "10325": "MDPS1 - CHSS"
  },
  "status": "success"
}
```


### 4. Get Schedule Table
- **Endpoint**: `/api`
- **Method**: POST/GET
- **Form Data**:
  - `option`: Option value
  - `programme`: Program value
- **Description**: Retrieve a schedule table based on the selected option and program.

## Usage Example
Developers can interact with the API using the following endpoints:
- To get categories: [https://udom-ratiba-api.vercel.app/get/category](https://udom-ratiba-api.vercel.app/get/category)
- To get options: [https://udom-ratiba-api.vercel.app/get/option](https://udom-ratiba-api.vercel.app/get/option)
- To get programs: [https://udom-ratiba-api.vercel.app/get/programme](https://udom-ratiba-api.vercel.app/get/programme)
- To get a schedule table: [https://udom-ratiba-api.vercel.app/api](https://udom-ratiba-api.vercel.app/api) (POST request with 'option' and 'programme' form data)

## How to Use
Developers can integrate this API into their applications to access Udom Ratiba schedule data for various purposes, including but not limited to:
- Building schedule management applications
- Creating academic tools and resources
- Developing customized schedule widgets for websites

## Error Handling
The application employs a robust error-handling mechanism, providing a structured JSON response with status and code for any encountered errors during API interactions.

## Server Settings
The application is effortlessly hosted on Vercel, eliminating the need for a separate server setup. Developers can seamlessly access and utilize the API without the hassle of intricate server configurations.

## Author
This project is developed and maintained by **masterplan**. For inquiries or collaboration opportunities, feel free to contact [Whatsapp](wa.me/255673182989).

## License
This project is licensed under the [MIT License](LICENSE). Feel free to explore and adapt the codebase to meet your specific requirements.
