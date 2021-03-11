import pyowm

API = 'c20030b930bac8c3232e1683308885e9'


def observation(city, token=API):
    """Global parameters"""
    owm = pyowm.OWM(token)
    obs = owm.weather_at_place(city)
    return obs


def weather(w):
    """Weather info."""

    print(w.get_reference_time())
    print(w.get_reference_time(timeformat='iso'))
    print(w.get_reference_time(timeformat='date'))
    print(w.get_clouds())
    print(w.get_rain())
    print(w.get_snow())
    print(w.get_wind())
    print(w.get_humidity())
    print(w.get_pressure())
    print(w.get_temperature())
    print(w.get_temperature(unit='celsius'))
    print(w.get_status())
    print(w.get_detailed_status())
    print(w.get_weather_code())
    print(w.get_weather_icon_name())
    print(w.get_weather_icon_url())
    print(w.get_sunrise_time())
    print(w.get_sunset_time('iso'))
    print("\n")


def location(l):
    """Location info."""

    print(l.get_name())
    print(l.get_lon())
    print(l.get_lat())
    print(l.get_ID())
    print("\n")


while True:
    print("Exit enter: 0")
    entered_city = input("Enter you city: ")
    if entered_city != "0":
        # Get weather info
        weather(observation(entered_city).get_weather())
        # Get location info.
        location(observation(entered_city).get_location())
    else:
        print("You are out of the program.")
        break
