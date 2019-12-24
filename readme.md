# Python and MySQL RDBMS Repo

Welcome! This repo contains basic CRUD functions along with some data manipulation tools to extract equity data from MySQL
using Python. This repo will be the central hub for learning how to manipulate equity data using code instead of cumbersome
MS Excel. 

The genesis behind this initiative was to re-invent data storage and visualization now that our enterprise has hit a key
personal milestone: 35 million data points. 

![Hooray GIF!](https://media2.giphy.com/media/MTclfCr4tVgis/giphy.gif)

For a smaller buy-side RIA, this is a big deal! Our data spans 19 years and grows every month!

## Here's why I'm now using code!

* 180,000kb file sizes are pretty hard to manipulate and open in memory along with multiple other apps
* In order to grab only certain fields you need from a larger dataset, you HAVE to read into the entire sheet
    * (This is like 'SELECT * FROM foo' when you only want one field, it makes no sense to display all data if not desired)
* And speaking of that last point, you can't grab data without rendering it to the screen in Excel! Annoying!

### Why Python?

In my limited experience I've coded in JavaScript, C, HTML-CSS (both non-logical) and Python.
All of these languages but one have a major drawback, to beginners the code looks like an alien language. Python
is written in what looks like the english language. This means you can start creating faster!!!

![Python scripting demo](https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiu5ZKDo83mAhWKhOAKHdMFDF0QjRx6BAgBEAQ&url=https%3A%2F%2Fgiphy.com%2Fexplore%2Fpythons&psig=AOvVaw26oIzXV9nw4I_scSjUt233&ust=1577242115881406)

## About ECS & Our Data

At EquityCompass, our data enterprise houses equity market data that aggreagates monthly as-of, as-reported stock data. 
We tagrget coverage of the Russell 3000 and the S&P 500. Our data is updated as-of the last day of the month and includes
obsolete securities. We currently aggregate data on 206 unique fields for each security, less eight fields which are identifiers.

Fields include price, 52wk hi and lo, valuation fields, relative strength fields, sector data and proprietary metrics. We currently do not
publish our data, nor do we have plans to sell our data via an API.