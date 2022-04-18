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

<h3>Project Planning & Tracking</h3>
I used a Kanban board to keep track of my progress
<p>
<img src="https://github.com/drodbourne/dalerep/blob/main/Kanban%20Board.drawio.png">
</p>
<h4>Phase 1 - Setting up the virtual environment</h4>

Created a virtual machine and SQL server on Google Could Platform. Allowed permissions for http traffic, flask and Jenkins on the vm. Instantiate an instance and connect to VSCode on my workstation.

<h4>Phase 2 - Design & coding of application</h4>

 Using methods learnt from training to create, read, update & delete data input from a webform by a user. Design database to store data. Coding was done using python.
 The app is designed to allow user to create a fantasy football team & add players.

<h3><u>ERD</u></h3>
Showing the one to many relationshp between team and players.
<p>
<img src="https://raw.githubusercontent.com/drodbourne/dalerep/abdd36170493bf13e8193f90b4d960bf19bdb54d/Database%20diagram.drawio.png">
</p>

<h4>Phase 3 - Front end development </h4>
<table>
    <tr>
    <td>The first page opens to allow a user to enter a team name.</td>
    <td>So let's input a team name and hit add team</td>
    
  </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/Addteam.png">
</p></td>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/AddteamData.png">
</p>
</td>
      </tr>
</table>
<table>
    <tr>
    <td>After adding a team it redrects so we can add players to the team. Let's add some players</td>
    </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/AddPlayers.png">
</p></td>
 </tr>
</table>


<table>
    <tr>
    <td>Every time you add a player it goes to the player list. Here we can add more players, update or delete a player by following the link</td>
    </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/PlayerList2.png">
</p></td>
 </tr>
</table>

<table>
    <tr>
    <td>The player update page.</td>
    <td>The player delete page.</td>
    
  </tr>
  <tr>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/PlayerUpdate.png">
</p></td>
    <td><p>
<img src="https://github.com/drodbourne/dalerep/blob/main/PlayerDelete.png">
</p>
</td>
      </tr>
</table>

<h4>Phase 4 - Testing</h4>

I seem to have hit a bit of a brick wall here. I made a test_app.py file and used pytest procedures. So far as I can tell all the code is correct but I keep getting the error listed below. I think it has something to with the routes. This part will be updated when I figure out exactly what the problem is

<img src="https://github.com/drodbourne/dalerep/blob/main/ProjectTest.png">






<h3>Risk Assesment</h3>
<p>
<img src=https://github.com/drodbourne/QA-Project/blob/main/Risk%20Assesment.drawio.png>
</p>


