# habitat_tools
Tools to interact with the Habitat API

**Methods Available**
add_reading(temperature=None, humidity=None)
Takes a temperature and humidty float
Returns reading

get_reading
Returns the current reading

filter_readings(period=None, unit=None, date_from=None, date_to=None)
Takes period string (minutes, days, hours), an integer unit of time or isoformat dates
Returns a list of readings

get_config
Returns the current config

set_config(data=None)
Takes a dictionary of config fields and vlaues to be updated
Returns a config

new_config
Returns a new config from defaults
