# LearnYourCountriesAndCapitals
Generate a set of images to teach you countries shape, countries name and capital cities

This program will generate 3 images for each known country
|country_1.png|countour of the country|
|country_2_name.png|countour of the country with country name|
|country_3_capital.png|country with capital city name|

This is useful to use in a slideshow app in order to  progressively display the country, its name and its capital city.

![Country](docs/Sri Lanka_1.png?raw=true)
![Country with name](docs/Sri Lanka_2_name.png?raw=true)
![Country with capital city](docs/Sri Lanka_3_capital.png?raw=true)

# Install
```pip install -r requirements.txt```

# Initiate cards generation
```LearnYourCountriesAndCapitals.py```

Wait ~5 minutes for the almost 800 images to be generated in ```geocards``` directory

# Internal processes
The program uses [Natural Earth](https://www.naturalearthdata.com/) Geo data (like countries borders and cities.
The data are already stored in the ```datas``` directory

The program uses [Stamen](https://stamen.com/) data for terrain design and colors.
The data is downloaded from internet while running.

# Known issues
For country with overseas territories the cards will display all of those, creating a large view with a lot of sea.