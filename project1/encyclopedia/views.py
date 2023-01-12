from django.shortcuts import render
# importing markdown to convert markdown to html
from markdown2 import Markdown


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def htmlconverter(title):
    mycode = util.get_entry(title)
    # copy pasted code from github which cs50 provided
    markdowner = Markdown()
    if mycode == None:
        return None
    else:
        return markdowner.convert(mycode)
        # if file exists then convert to html else return none
    markdowner.convert("*boo!*")


def entry(request, title):
    # function which calls the entries given in file
    # if entries match then return none
    htmlcode = htmlconverter(title)
    if htmlcode == None:
        return render(request, "encyclopedia/error.html", {
            "info": "This entry doesn't exist"
            #  error page indicating that their requested page was not found.
            # making an error information assuming we didnt write entry names
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "code": htmlcode
        })
        # if we did write entry names then go to destination


# import libraryeach encyclopedia entry markdown should be converted
# to html for this use markdown library and
# use function to convert it to html 