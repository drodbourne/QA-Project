# QA-Project

<h3>By Dale Rodbourne</h3>

<h3><u>Objective</u></h3>

To create a CRUD application with a one to many database table relationship. Utilising the support tools,
methodologies and technologies that encapsulate all core modules
covered during training listed below.

* Project Management
* Python Fundamentals
* Python Testing
* Git
* Basic Linux
* Python Web Development
* Continuous Integration
* Cloud Fundamentals
* Databases

<h3>User Story</h3>
A user story can help to develop the project by providing guidance on what the user wants from the app. It also gives an idea
of how the app should look and work to meet the requirements of the user. My user is a football coach who manages several youth
teams of various ages. They would like the app to allow assigning players to a team according to their age. Based on this brief I 
propose to make an app that will do the following.

* Create teams & players and allow a player to be associated with a team
* Read a list of teams and a list of players
* Update teams & players
* Delete players from a team or delete a team  


<h3>Project Planning & Tracking</h3>
I used Trello to keep track of my progress. 
<p>
<img src="https://github.com/drodbourne/dalerep/blob/main/Trello.png">
</p>
<h3><u>ERD</u></h3>
Showing the one to many relationshp between team and players.
<p>
<img src="https://raw.githubusercontent.com/drodbourne/dalerep/abdd36170493bf13e8193f90b4d960bf19bdb54d/Database%20diagram.drawio.png">
</p>

<h4>Phase 1 - Setting up the virtual environment</h4>

Created a virtual machine and SQL server on Google Could Platform. Allowed permissions for http traffic, flask and Jenkins on the vm. Instantiate an instance and connect to VSCode on my workstation.

<h4>Phase 2 - Design & coding of application</h4>

 Using methods learnt from training to create, read, update & delete data input from a webform by a user. Design database to store data. Coding was done using python.
 The app is designed to assign a player to a team based on their age as requested by the user.



<h4>Phase 3 - Front end development </h4>
<table>
    <tr>
    <td>The app opens on the home page from here we start by entering a team name so lets click the create new team button </td>
    </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/HomePage.png">
</p></td>
 </tr>
</table>
<table>
    <tr>
    <td>Enter the name of a team and click add team </td>
    </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/TeamAdd.png">
</p></td>
 </tr>
</table>
<table>
    <tr>
    <td>Clicking the view team list will show us all the teams in the database. The teams can be updated or deleted from here </td>
    </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/TeamList.png">
</p></td>
 </tr>
</table>

<table>
    <tr>
    <td>Clicking the create new player will allow a new player to be associated with a team </td>
    </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/PlayersAdd.png">
</p></td>
 </tr>
</table>


<table>
    <tr>
    <td>Clicking the players list will show us all the players in the database. The players can be updated or deleted from here </td>
    </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/ListPlayers.png">
</p></td>
 </tr>
</table>

<h4>Phase 4 - Testing</h4>

I made a class to test create, read, update and delete functionality for both the team and players. When I first started the test

<img src="https://github.com/drodbourne/dalerep/blob/main/Pytest.png">






<h3>Risk Assesment</h3>
As this is a basic app the risk are quite low. But when going into a real project the assesments below should be taken into consideration.
<p>
<img src=https://github.com/drodbourne/QA-Project/blob/main/Risk%20Assesment.drawio.png>
</p>

<h4>Problems & Challenges</h4>
The biggest problem and greatest challenge for me was as my pc has no sound I had to follow the course using teams on my mobile. It has not been easy trying to keep
up with the lessons. I could not share my screen when I was having a problem. I also started the project with the intent of using a cloud SQL database but I did not realise it would use so much of the free credit so I had to resort using sqllite to finish the project. 
