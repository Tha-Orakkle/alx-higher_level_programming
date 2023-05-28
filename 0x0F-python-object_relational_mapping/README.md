# Python - Object-relational mapping

## Tasks :page_with_curl:

* **0. Get all states**
  * [0-select_states.py](./0-select_states.py): Python script that lists all states in the database `hbtn_0e_0_usa` using MySQLdb.
  * Usage: `./0-select_states.py <mysql username> <mysql password> <database name>`.
  * Results are sorted in ascending order by `states.id`.

* **1. Filter states**
  * [1-filter_states.py](./1-filter_states.py): python scripts that lists all the states with a name that starts with uppercase `N` from the database `hbtn_0e_0_usa`
  * Usage: `./1-filter_states.py <mysql username> <mysql password> <database nam    e>`.
  * Results are sorted in ascending order by `states.id`.

* **2. Filter states by user input**
  * [2-my_filter_states.py](./2-my_filter_states.py): python scripts that lists all the states with a name that matches the argument passed.
  * Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database nam    e>`.
  * Results are sorted in ascending order by `states.id`.

* **3. SQL Injection...**
  * [3-my_safe_filter_states.py](./3-my_safe_filter_states.py): python scripts that lists all the states with a name that matches the argument passed.
  * Usage: `./2-my_filter_states.py <mysql username> <mysql password> <database nam    e>`.
  * The query is safe from MySQL injections
  * Results are sorted in ascending order by `states.id`.

* **4. Cities by states**
  * [4-cities_by_state.py](./4-cities_by_state.py): Python script that uses
  MySQLdb to list all cities from the database `hbtn_0e_4_usa`.
  * Usage: `./4-cities_by_state.py <mysql username> <mysql password>
  <database name>`.
  * Results are ordered by ascending `cities.id`.

* **5. All cities by state**
  * [5-filter_cities.py](./5-filter_cities.py): Python script that uses MySQLdb
  to list all cities of a given state in the database `hbtn_0e_4_usa`.
  * Usage: `./5-filter_cities.py <mysql username> <mysql password>
  <database name>`.
  * Results are sorted by ascending `cities.id`.

