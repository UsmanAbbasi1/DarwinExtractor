# DarwinExtractor
This project extracts data from Darwin Info product API and displays the result on terminal for now.
The logic is separated ina way that processing and formatting of data is separated from each other so it is very maintainable and easy to change the output format.
To run the extractor API, replace your access_token [here](https://github.com/UsmanAbbasi1/DarwinExtractor/blob/2e8db6e21993f1859c00e5991ae67e5a965d7dd2/darwin_extractor/config.py#L8) to make sure you get access to the API.


## How to run the script
1: Create virtual env
> python3 -m venv darwin_env

2: Activate virtual env
> source darwin_env/bin/activate

3: Set proper python path.

Change directory from terminal to root darwin_extractor (which is Github repository's root folder)
> cd darwin_extractor

> export PYTHONPATH=.

3: Install requirements/dependencies
> pip install -r requirements.txt
 
4: Create .env file to load environment variables i.e. ACCESS_TOKEN

Duplicate the file called [.env.example](https://github.com/UsmanAbbasi1/DarwinExtractor/blob/main/.env.example) and rename it to .env

Assign your Darwin access token value to variable ACCESS_TOKEN in .env file.

Notice that without this, your code will return authentication error.

5: Run the darwin extractor script: 
> python darwin_extractor/main.py 

6: Run test case
>  python -m unittest discover tests/



## Choice of DataStructure
It is very important to have a layer between external APIs and internal business logic.
I have used pydantic model to store the response from Darwin API. This pydantic model is our internal application model.
So if anything chage, we will only need to adjust the model and not our internal business logic. Because business logic is not directly using the Darwin's API
response format. Instead it is using out intermediary data structure called [DarwinPurchaseResponse](https://github.com/UsmanAbbasi1/DarwinExtractor/blob/2e8db6e21993f1859c00e5991ae67e5a965d7dd2/darwin_extractor/models.py#L5)

## Coding Approach
I have kept in mind the separation of concern. Models, Client class, extraction and formatting of data, everything is 
very cleanly separated in separate files/classes. This makes the code extendable, maintainable and scalable.


Example of output data:
response from darwin 'DAH': product_name='DAH.5.24' dc='5.18' os='4.82' cs='1.57' mc='9.89' rplus='1.31' ra='9.87' ex='10.0' pf='0.87' score='48.51' rminus='3.21' rs='7.16' sc='4.54' la='7.85' cp='4.54'

## Testing
I also have written a test case to test the code. Though, on production level code, I would have more test coverage than 
I have in this task.
