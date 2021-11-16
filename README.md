# [Team 4Gs](https://github.com/B-G101/4Gs)
Runtime link: to be added :)
### [Scrum Board](https://github.com/B-G101/4Gs/projects/1)
### Project Purpose
Description of our project and its purpose
***
### Contributors
|Contributor|Github ID/Profile|Assigned Tasks|Commits|Pair Journal|
|------|---------------------------|-----|--------|------------------|
|Bria|[B-G101](https://github.com/B-G101)|[Tasks](https://github.com/B-G101/4Gs/projects/1?card_filter_query=assignee%3Ab_g101)|[Commits](https://github.com/B-G101/4Gs/commits?author=B-G101)|
|Nadira|[nadirahaddach](https://github.com/nadirahaddach)|[Tasks](https://github.com/B-G101/4Gs/projects/1?card_filter_query=assignee%3Anadira)|[Commits](https://github.com/B-G101/4Gs/commits?author=nadirahaddach)|
|Paige|[paigemccartin](https://github.com/paigemccartin)|[Tasks](https://github.com/B-G101/4Gs/projects/1?card_filter_query=assignee%3Apaige)|[Commits](https://github.com/B-G101/4Gs/commits?author=paigemccartin)|
|Jessie|[parkjessie](https://github.com/parkjessie)|[Tasks](https://github.com/B-G101/4Gs/projects/1?card_filter_query=assignee%3Ajessie)|[Commits](https://github.com/B-G101/4Gs/commits?author=parkjessie)|
***
### Table of Contents
1. [Week 0]()


---
## Week 0: Organize and Design
|Assigned Role|Person Assigned|Tasks for the Week|Commits/Evidence of Completion|
|--------------------------------------------------|----------------------------------------------|----------------------------------------|------------------------------------------------------------|
|Scrum Master|Nadira|
|GitHub Admin|Bria|
|Primary Designer|Paige|
|Deployment Manager|Jessie|
|Operation Officer|Bria|







### Idea
Starter code should be fun and practical.
### Visual thoughts
#### Organize with Bootstrap menu 
#### Add some color and fun through VANTA Visuals (birds, halo, solar, net)
#### Show some practical and fun links (hrefs) like Twitter, Git, Youtube
#### Show project specific links (hrefs) per page

### Implementation progress (August 13th, 2021)
#### Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
#### The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
#### The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
#### WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
#### Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
#### The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
#### The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
#### Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
#### The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
#### A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.

### IDE management (things that happened beyond plan)
#### Recall on ".gitignore" solution to the pains of temporary files.  Start a ".gitignore" and avoid promoting temporary files to Git, for instance IDE xml files.
#### A project needs to establish a "requirements.txt" to keep track of Python packages used by the project.  This help in other IDEs and Deployment.  IntelliJ has menu Tool -> Sync Python Requirements to start file. 
