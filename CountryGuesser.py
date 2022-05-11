import subprocess
from time import sleep

# THIS IS A FIRST TIME DEPENDANCIES INSTALLATION

autocorrect_check = subprocess.run(["pip", "show", "--quiet", "autocorrect"])
geopy_check = subprocess.run(["pip", "show", "--quiet", "geopy"])
countryinfo_check = subprocess.run(["pip", "show", "--quiet", "countryinfo"])

if autocorrect_check.returncode or geopy_check.returncode or countryinfo_check.returncode != 0:
    subprocess.call("cls", shell=True)
    print("Certain dependancies not found, installing in 3 seconds")
    sleep(3)
    subprocess.call("cls", shell=True)
    print("Installing autocorrect")
    subprocess.run(["pip", "install", "autocorrect"])
    print("Installing geopy")
    subprocess.run(["pip", "install", "geopy"])
    subprocess.call("cls", shell=True)
    print("Installing countryinfo")
    subprocess.run(["pip", "install", "countryinfo"])
    subprocess.call("cls", shell=True)
    print("Please restart the script! Closing in 30 seconds...")
    sleep(30)
    exit()

countries = {
"Afghanistan": "AF", 
"Albania": "AL", 
"Algeria": "DZ", 
"Andorra": "AD", 
"Angola": "AO", 
"Argentina": "AR", 
"Armenia": "AM", 
"Australia": "AU", 
"Austria": "AT", 
"Azerbaijan": "AZ", 
"Bahamas": "BS", 
"Bahrain": "BH", 
"Bangladesh": "BD", 
"Belarus": "BY", 
"Belgium": "BE", 
"Bermuda": "BM", 
"Bhutan": "BT", 
"Bolivia": "BO", 
"Bosnia And Herzegovina": "BA", 
"Botswana": "BW", 
"Brazil": "BR", 
"Bulgaria": "BG", 
"Burkina Faso": "BF", 
"Burundi": "BI", 
"Cambodia": "KH", 
"Cameroon": "CM", 
"Canada": "CA", 
"Chad": "TD", 
"Chile": "CL", 
"China": "CN", 
"Colombia": "CO", 
"Comoros": "KM", 
"Congo": "CG", 
"Costa Rica": "CR", 
"Croatia": "HR", 
"Cuba": "CU", 
"Cyprus": "CY", 
"Czech Republic": "CZ", 
"Denmark": "DK", 
"Dominica": "DM", 
"Dominican Republic": "DO", 
"Ecuador": "EC", 
"Egypt": "EG", 
"El Salvador": "SV", 
"Estonia": "EE", 
"Ethiopia": "ET", 
"Fiji": "FJ", 
"Finland": "FI", 
"France": "FR", 
"Gambia": "GM", 
"Georgia": "GE", 
"Germany": "DE", 
"Ghana": "GH", 
"Gibraltar": "GI", 
"Greece": "GR", 
"Greenland": "GL", 
"Grenada": "GD", 
"Guatemala": "GT",  
"Guinea": "GN", 
"Guyana": "GY", 
"Haiti": "HT", 
"Honduras": "HN", 
"Hong Kong": "HK", 
"Hungary": "HU", 
"Iceland": "IS", 
"India": "IN", 
"Indonesia": "ID", 
"Iran": "IR", 
"Iraq": "IQ", 
"Ireland": "IE", 
"Israel": "IL", 
"Italy": "IT", 
"Jamaica": "JM", 
"Japan": "JP", 
"Jordan": "JO", 
"Kazakhstan": "KZ", 
"Kenya": "KE", 
"Kiribati": "KI", 
"Korea": "KR", 
"Kuwait": "KW", 
"Kyrgyzstan": "KG", 
"Latvia": "LV", 
"Lebanon": "LB", 
"Lesotho": "LS", 
"Liberia": "LR", 
"Liechtenstein": "LI", 
"Lithuania": "LT", 
"Luxembourg": "LU", 
"Macedonia": "MK", 
"Madagascar": "MG", 
"Malaysia": "MY", 
"Maldives": "MV", 
"Malta": "MT", 
"Mexico": "MX", 
"Moldova": "MD", 
"Monaco": "MC", 
"Mongolia": "MN", 
"Montenegro": "ME",
"Morocco": "MA", 
"Mozambique": "MZ", 
"Myanmar": "MM", 
"Namibia": "NA", 
"Nepal": "NP", 
"Netherlands": "NL", 
"New Zealand": "NZ", 
"Nicaragua": "NI", 
"Niger": "NE", 
"Nigeria": "NG", 
"Norway": "NO", 
"Oman": "OM", 
"Pakistan": "PK", 
"Palestine": "PS", 
"Panama": "PA", 
"Papua New Guinea": "PG", 
"Paraguay": "PY", 
"Peru": "PE", 
"Philippines": "PH", 
"Poland": "PL", 
"Portugal": "PT", 
"Puerto Rico": "PR", 
"Qatar": "QA", 
"Romania": "RO", 
"Russia": "RU", 
"San Marino": "SM", 
"Saudi Arabia": "SA", 
"Senegal": "SN", 
"Serbia": "RS", 
"Sierra Leone": "SL", 
"Singapore": "SG", 
"Slovakia": "SK", 
"Slovenia": "SI", 
"Solomon Islands": "SB", 
"Somalia": "SO", 
"South Africa": "ZA", 
"Spain": "ES", 
"Sri Lanka": "LK", 
"Sudan": "SD", 
"Sweden": "SE", 
"Switzerland": "CH", 
"Syria": "SY", 
"Taiwan": "TW", 
"Tajikistan": "TJ", 
"Tanzania": "TZ", 
"Thailand": "TH", 
"Tunisia": "TN", 
"Turkey": "TR", 
"Turkmenistan": "TM", 
"Uganda": "UG", 
"Ukraine": "UA", 
"United Arab Emirates": "AE", 
"United Kingdom": "GB", 
"United States": "US", 
"Uruguay": "UY", 
"Uzbekistan": "UZ", 
"Venezuela": "VE", 
"Vietnam": "VN", 
"Vatican": "VA", 
"Yemen": "YE", 
"Zambia": "ZM", 
"Zimbabwe": "ZW"}

from random import choice
import geopy.distance
from geopy import Nominatim
from time import sleep
import autocorrect as ac
from countryinfo import CountryInfo

def get_real_country_and_code():
    """Get the final country"""
    # globals
    global final_country, final_country_code, real_coords
    real_country_name = list(countries.keys())
    final_country = choice(real_country_name)
    final_country_code = list(countries.values())[list(countries.keys()).index(final_country)]

    # Get lat lon
    app  = Nominatim(user_agent="aslopas")
    location = app.geocode(final_country).raw
    real_latitude = location["lat"]
    real_longitude = location["lon"]
    real_coords = f"{real_latitude}, {real_longitude}"
get_real_country_and_code()


def auto_correct(guess):
    autocorrect = ac.Speller("en")
    guess_corrected = autocorrect(guess)
    return guess_corrected


def guess_country(guess):
    if guess in countries:
        return guess
    else:
        did_you_mean = input(f"""Did you mean {auto_correct(guess)}?\n(Yes/No)\n-->""").lower()
        if did_you_mean.startswith("y"):
            guess = auto_correct(guess)
            if guess in countries:
                return guess
        else:
            print("This country doesn't exist or you wrote it incorrectly, try again.")
            sleep(3)
            pass
        
def get_distance(guess):
    app  = Nominatim(user_agent="aslopas")
    location = app.geocode(guess_country(guess)).raw
    guess_latitude = location["lat"]
    guess_longitude = location["lon"]
    guess_coords = f"{guess_latitude}, {guess_longitude}"

    global distance
    distance = int(geopy.distance.distance(real_coords, guess_coords).km)
    if distance == 0:
        return "the real country, good job!"
    else:
        return f"{distance}km away from the real country."

print(f"""CountryGuesser
  ____  _   _ ___ __  __ ___ ____  
 / ___|| | | |_ _|  \/  |_ _/ ___| 
 \___ \| |_| || || |\/| || |\___ \ 
  ___) |  _  || || |  | || | ___) |
 |____/|_| |_|___|_|  |_|___|____/ 

https://github.com/Shinigamiixd

The country distances are calculated from the centres of the countries.
Please type only real countries and not random words.
WARNING: Some of the countries hints are not exact and may be off by a lot, because of old data.""")

#print(final_country, final_country_code)
#print(real_coords)

languages = CountryInfo(final_country).languages()
languages_two = (','.join(languages))

currencies = CountryInfo(final_country).currencies()
currencies_two = (','.join(currencies))

borders = CountryInfo(final_country).borders()
borders_two = (','.join(borders))

# GUESS 1
for i in range(1):
    guess = input(str("""\nGuess the country.\n\n-->""")).title()
    print(f"{guess} is {get_distance(guess)}")
    if distance == 0:
        print("Please restart the game to play again.")
        sleep(30)
        exit()
    else:
        print(f"This country - {languages_two}")

    # GUESS 2
    for i in range(1):
        guess = input(str("""\n-->""")).title()
        print(f"{guess} is {get_distance(guess)}")
        if distance == 0:
            print("Please restart the game to play again.")
            sleep(30)
            exit()
        else:
            print(f"The population of the real country is - {CountryInfo(final_country).population():,} people. (may be wrong by -500k to -1mil)")

    # GUESS 3
    for i in range(1):
        guess = input(str("""\n-->""")).title()
        print(f"{guess} is {get_distance(guess)}")
        if distance == 0:
            print("Please restart the game to play again.")
            sleep(30)
            exit()
        else:
            print(f"The country\'s currect currency is - {currencies_two}.")

    # GUESS 4
    for i in range(1):
        guess = input(str("""\n-->""")).title()
        print(f"{guess} is {get_distance(guess)}")
        if distance == 0:
            print("Please restart the game to play again.")
            sleep(30)
            exit()
        else:
            print(f"The capital of the real country is - {CountryInfo(final_country).capital()}")

    # GUESS 5
    for i in range(1):
        guess = input(str("""\n-->""")).title()
        print(f"{guess} is {get_distance(guess)}")
        if distance == 0:
            print("Please restart the game to play again.")
            sleep(30)
            exit()
        else:
            print(f"The real country's alpha2 code is - {final_country_code}")
            print(f"The real country's first 3 letters are - {final_country[:3]}")
            print(f"The real country borders these countries - {borders_two}")

    for i in range(1):
        guess = input(str("""\n-->""")).title()
        print(f"{guess} is {get_distance(guess)}")
        if distance == 0:
            print("Please restart the game to play again.")
            sleep(30)
            exit()
        else:
            print(f"You lose! The real country was {final_country}")
            sleep(30)



# USEFUL LINKS:
# https://janakiev.com/blog/gps-points-distance-python/
# https://www.thepythoncode.com/article/get-geolocation-in-python

# TODO:
# 1 auto imports
# 2 draw the country in ASCII
# 3 add hints

# DONE:
# 1 autocorrect the guess

# imports:
# countryinfo