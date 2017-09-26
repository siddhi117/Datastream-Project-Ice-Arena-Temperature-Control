from bottle import route, run, template, static_file
import get_stream

@route("/")
def home():
    return template("home.tpl")

@route("/map")
def example_map():
    data = get_stream.get_stream_data()
    #print (data)
    return template("ice_arena_map.tpl", data=data)

@route('/chart')
def get_chart():
    weather_data, ice_arena_data = get_stream.get_chart_data()
    return template("weather_chart.tpl", rows=weather_data, fields=ice_arena_data)

@route("/static/<filename:path>")
def static(filename):
    return static_file(filename, root="./Static")

run(host='localhost', port=8080, debug=True, reloader = True)