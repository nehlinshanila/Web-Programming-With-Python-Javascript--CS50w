from django.shortcuts import render
# importing markdown to convert markdown to html
from markdown2 import Markdown
import random
# random for random function
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def htmlconverter(title):
    mycode = util.get_entry(title)
    # copy pasted code from github which cs50 provided for markdown
    markdowner = Markdown()
    if mycode == None:
        return None
    else:
        return markdowner.convert(mycode)
        # if file exists then convert to html else return none
    markdowner.convert("*boo!*")


def getentry(request, title):
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

def getsearch(request):
    if request.method == "POST":
        get_search = request.POST['q']
        # q is what we used to label the variabes
        htmlcode = htmlconverter(get_search)
        if htmlcode is not None:
            return render(request, "encyclopedia/entry.html", {
            "title": get_search,
            "code": htmlcode
        })
        else:
            theentries = util.list_entries()
            recommendation = []
            # recommendation is a list
            for entry in theentries:
                if get_search.lower() in entry.lower():
                    recommendation.append(entry)
                    # check is py is inside of python etc
                return render(request, "encyclopedia/search.html",{
                    "recommendation" : recommendation

                })

# making the new page
def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title = request.POST['title']
        textarea = request.POST['textarea']
        titleexists = util.get_entry(title)
        if titleexists is not None:
            return render(request, "encyclopedia/error.html",{
                "message": "page exists"
                })
        else:
            util.save_entry(title, textarea)
            htmlcode = htmlconverter(title)
            return render(request, "encyclopedia/entry.html",{
                "title":title,
                "textarea": htmlcode
            })
        # if newpage clicked then redirect to it else go to error page

# function for edit page
def editpage(request):
    if request.method == 'POST':
        title = request.POST['entrytitle']
        textarea = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html",{
            "title": title,
            "textarea": textarea
        })

# after editing savepage function will store it and redirect back to entry
def savepage(request):
    if request.method == "POST":
        title = request.POST['title']
        textarea = request.POST['textarea']
        util.save_entry(title, textarea)
        htmlcode = htmlconverter(title)
        return render(request, "encyclopedia/entry.html",{
        "title": title,
        "textarea": htmlcode
    })

    
# randompage while clicking on random will pick any of the entries and view them
def randompage(request):
    theentries = util.list_entries()
    random_entry = random.choice(theentries)
    htmlcode = htmlconverter(random_entry)
    return render(request, "encyclopedia/entry.html",{
        "title": random_entry,
        "textarea": htmlcode
    })

    
# import libraryeach encyclopedia entry markdown should be converted
# to html for this use markdown library and
# use function to convert it to html 