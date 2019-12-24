# Python and MySQL RDBMS Repo

Welcome! This repo contains basic CRUD functions along with some data manipulation tools to extract equity data from MySQL
using Python. This repo will be the central hub for learning how to manipulate equity data using code instead of cumbersome
MS Excel. 

The genesis behind this initiative was to re-invent data storage and visualization now that our enterprise has hit a key
personal milestone: 35 million data points. 

## Here's why I'm now using code!

* 180,000kb file sizes are pretty hard to manipulate and open in memory along with multiple other apps
* In order to grab only certain fields you need from a larger dataset, you HAVE to read into the entire sheet
    * (This is like 'SELECT * FROM foo' when you only want one field, it makes no sense to display all data if not desired)
* And speaking of that last point, you can't grab data without rendering it to the screen in Excel! Annoying!

### Why Python?

Well, in my limited development experience, I've coded in JavaScript, C, HTML-CSS (non-logical) and Python.
All of these languages but one have a major drawback, to beginners the code looks like an alien language. Python
is written in what looks like the english language. This means you can start creating faster!!!