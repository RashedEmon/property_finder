#Property Finder

User can search property by location, price range and ordered by price.<br>

#Technoloy used in this project:<br>

1. Python<br>
2. Django<br>
3. PostgreSQL<br>

#Database Schema:<br>
Property(id,title,description,price,location) -> Relation[many to one with Location, one to many with Image]<br>
Location(id,name) -> Relation[one to many with Property] <br>
Label(id,title) -> Relation[one to many with Image] <br>
Image(id,image,type,property) -> Relation[many to one with Label, many to one with Property]<br>

#How to Install and Run the Application: <br>

1. Create virtual environment<br>
   <code>python3 -m virtualenv directory_name</code><br>
2. Change directory to directory_name<br>
   <code>cd directory_name</code><br>
3. Clone the repository<br>
   <code>git clone https://github.com/RashedEmon/property_finder.git</code><br>
4. Change directory to project root<br>
   <code>cd propery_finder</code><br>
5. Install dependencies.<br>
   <code> pip install -r requirements.txt</code><br>
6. Create a config.py file in project core and create database config according to django convention.<br>
7. Run the application.<br>
   <code>python3 manage.py runserver</code><br>
