# Movie Data Reporting API
This API provides utilizes the Movies Data Set, which contains metadata for movies dating back to the late 1800s! 

For more details: https://www.kaggle.com/rounakbanik/the-movies-dataset. 



You can grab the following details:

* The budget for a production company by year
* The revenue for a production company by year
* The most popular movie genre by year

# Tutorial
## Installation
The API consists of two Docker containers: i) the _db_ container, which is a Postgres instance to house & persist data, and ii) the _api_ container, which is a Flask app that grabs data from the _db_ container.

To get the API up and running, we need to first install Docker (if you don't have it installed already). Then, we need to build the Docker containers. Finally, we need to seed the data in the _db_ container.

1. Install Docker
    * f