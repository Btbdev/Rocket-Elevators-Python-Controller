# Description

This code presents a program enabling the efficient movement of elevators in a given building. The code is written in a
way that all the steps from the first push of a button from a user until it's ride to the floor he wants to go will be
automated the to most efficient way !

How does it works ?

First of all, the program will control a column of different elevators. This column is the main controller for of all that is going to happen next and manages many attributes enabling the different operations that will be needed. With the column set, an elevator is going to be selected, or call, and it will be coming with its own attributes, such as its ID, its status, the floor it is currently on and the direction it is heading (or absence of direction). 

The selection of the elevator will be made from the press of a button (just like in real life !!) The user will enter the elevator and press a button to go up or down, depending on the floor he is currently standing. The call of this button will bring some attributes, from ID, to status, floor and direction. This will help the program to choose the best elevator, matching where the user wants to go : its floor request. The code will bring enough attributes for to be able to perform many actions and comparisons to evaluate all the environment attributes in the building, such as :

where is the user when he presses the button
where he wants to go
where are the elevators actually and what are they doing (their status, direction, floor, the weight they carry or are they obstructed)

The code will evaluate these options, giving them some value to set the best elevator available to a specific situation.
The elevator will then move, open its door, take the user if it is not in an overweight situation or obtructed, close its door and bring the user to the floor he wanted to go.

As an example, we see David, standing in front of an elevator column in a given building. OPn this column, 2 elevators are available. David is standing on the 2nd floor and he wants to go the the 6th floor. He presses the call button to go up. 

The two elevators are not at the same place. The left one is standing still at the first floor and the second one is moving from the 10th floor. It is on a mission of its own (it has been called or somebody is in it and is going somewhere). Allready, the code was given enough informations to evaluate the best choice for David. The first elevator, standing idle just one floor from David's request, seems to be better placed than the second elevator, away 9 floors from David. The program will initiate the first elevator to move, since the values derivated from the best elevator evaluation mechanism in place, has choosen this one to take David to its desired floor. 

David enters the elevator, push its floor request button and go where he wants to go !

The end !


#########################################################################################################################



# Rocket-Elevators-Python-Controller
This is the template to use for the python residential controller. You will find the classes that should be used along with some methods described in the requirements. The necessary file to run some tests is also included. 

### Installation

First, depending on your python version, make sure to install the Package Installer for Python (PIP) if needed:

https://pip.pypa.io/en/stable/installing/

Next, install Pytest:

https://docs.pytest.org/en/6.2.x/getting-started.html

### Running the tests

To launch the tests:

`pytest`

With a fully completed project, you should get an output like:

![Screenshot from 2021-06-15 13-13-13](https://user-images.githubusercontent.com/28630658/122095645-a41fa000-cddb-11eb-9322-81a766cce4bb.png)

You can also get more details about each test by adding the `-v` flag: 

`pytest -v` 

which should give something like: 

![Screenshot from 2021-06-15 13-13-33](https://user-images.githubusercontent.com/28630658/122095759-c74a4f80-cddb-11eb-999d-dfe35dbe7d18.png)

The test file can be left in your final project but no scenarios should be present in your code. The grader will run tests similar to the ones provided.

Of course, make sure to edit this Readme file to describe your own project!
