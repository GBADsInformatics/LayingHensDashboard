
# GBADS Laying Hens Dashboard

This dashboard was created ontop of the [GBADS Dashboard Template](https://github.com/GBADsInformatics/Dashboard_Template) by [@Amardeep](https://github.com/amardeep-1) and [@Nitin](https://github.com/Nitin501)

## Running in Docker
1. `docker run -d -p 80:8051 -v /local/path/to/.env:/app/.env gbadsinformatics/layinghens-dash` \
  This exposes the dashboard on port `80` of your machine, you can change this number to any port you desire. \
  Do not change `8051` in the port argument. \
  Change `/local/path/to/.env` to the full path of the .env you're using.

## Installation
1. `git clone https://github.com/GBADsInformatics/LayingHens_Dashboard`
2. `cd dash`
3. `pip3 install -r requirements.txt`
4. Contact [@WilliamFitzjohn](https://github.com/WilliamFitzjohn) to add a .env file

## Running the App
1. `cd dash`
2. `python3 wsgi.py`

## Author
- [@WilliamFitzjohn](https://github.com/WilliamFitzjohn)
