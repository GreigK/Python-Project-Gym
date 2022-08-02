# Python-Project-Gym

CodeClan_Gym_App

How to Run:

• Clone the repository
• Create a database with the following name : gym_manager
    • Use the following command in terminal : createdb gym-manager
• Populate the database using the following command : psql -d gym_manager -f db/gym_manager.sql
    • May be required to drop the database twice to ensure it has populated
• Run the console file : python3 console.py
• Run flask : flask run
    • Check the terminal to ensure which port has been used for the localhost
    
    
Gym
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP
The app should allow the gym to create and edit Members
The app should allow the gym to create and edit Classes
The app should allow the gym to book members on specific classes
The app should show a list of all upcoming classes
The app should show all members that are booked in for a particular class
Inspired By
Glofox, Pike13

Possible Extensions
Classes could have a maximum capacity, and users can only be added while there is space remaining.
The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings. 

The project technologies:

HTML / CSS
Python
Flask
PostgreSQL and the psycopg
