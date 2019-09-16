import query_bios
import bottle
import json
from bottle import route, get, run, template, static_file, post, request, get, jinja2_view
import os
import sys
from functools import partial
from sys import argv
bottle.TEMPLATE_PATH.insert(0, os.getcwd())
print(bottle.TEMPLATE_PATH.insert(0, os.getcwd()))
print(os.getcwd())
path = sys.path[0]
print(path);
view = partial(jinja2_view, template_lookup=['templates'])


@route('/')
def index():
    # print(path)
    return template(path + "/templates/index.html")


@route('/css/<css_file>')
def css(css_file):
    return static_file(css_file, root='css')


@route('/js/<js_file>')
def js(js_file):
    return static_file(js_file, root='js')

@route("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="images")

@route('/interest_input')
@view('book_display.html')
def get_input():
    era = request.GET.dict['eras'][0]
    figure = request.GET.dict['figures'][0]
    region = request.GET.dict['regions'][0]
    db_return = query_bios.find_relevant_bios(era, region, figure)
    for book in db_return:
        with_first_quote = book[9].replace('\x93','"')
        with_both_quotes = with_first_quote.replace('\x94','"')
        with_aposts = with_both_quotes.replace('\x92',"'")
    print(db_return)
    return {"books": db_return, "review": with_aposts}

def main():
    # print(sys.path)
    run(host='localhost', port=8080)


if __name__ == "__main__":
    main()