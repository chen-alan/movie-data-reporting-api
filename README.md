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
    * For the most up-to-date instructions, follow the official Docker install documentation for your OS (https://docs.docker.com/get-docker/)

2. Clone the repository
    * via HTTPS: `git clone https://github.com/chen-alan/movie-data-reporting-api.git`
    * via SSH: `git clone git@github.com:chen-alan/movie-data-reporting-api.git`

3. Build the Docker containers
    * `cd movie-data-reporting-api`
    * `docker compose up -d --build` 
    * Verify the Docker containers are running via `docker ps`
        * You should see two images (_api_ and _postgres_)

4. Seed data into the DB container
    * I've included a dump file of the data as it exists on my machine for simplicity. 
    * Copy the contents of the dump file to the DB container: `cat ./seed_data/backups/postgres_20221010.sql | docker exec -i db psql -U postgres`

5. Test the API connection
    * Try visiting `127.0.0.1:80` a web browser of your choice or run `curl 127.0.0.1:80` from a terminal window to test that the API is properly running.
    * `127.0.0.1:80` should return `Hiya! Wishing you a happy day :)`

# API Endpoints

1. `/revenues/{production_company_id}/{year}`
    * Returns the production company's revenue for the specified year as an integer.
        * example request: `curl 127.0.0.1:80/revenues/11661/1997`
      * example response: `237770259`

2. `/budgets/{production_company_id}/{year}`
    * Returns the production company's budget for the specified year as an integer.
        * example request: `curl 127.0.0.1:80/budgets/11661/1997`
        * example response: `215000000`

3. `/genres/{year}`
    * Returns the most popular genre for the specified year as a JSON object.
        * example request: `curl 127.0.0.1:80/genres/1997`
        * example response: `{"Thriller":53}`

# Running Unit Tests
Unit tests for this application are implemented using Pytest. You can find the source code in the `./tests` directory.

To run unit tests: `docker exec -i api python3 -m pytest`.
