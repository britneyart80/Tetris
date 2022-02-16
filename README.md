# TETRIS
###### started on 3/26/2020

<hr>
A game of tetris powered by python and the pygame library. <br>
This was my first time programming in python and I wanted to take on learning it in a fun way. <br>
This implementation utilizes the MVC structure and OOD principles.

Have fun!

### Technologies Used
- Python
- pygame library

### Architecture
To start the process, I started thinking about how I wanted to structure my code. I determined that the best way to do that was applying MVC principles we learned in class.

Models would be used for components of the game. I had 3 models:
- the gameboard
- a tetrominoe
- the scoreboard/sidebar on the GUI

The View would have one responsibility only, and that is the create the GUI based on the state of the model given.

The Controller pieces the model and view together. Upon user key inputs, the controller calls the appropriate updates to the model, and passes it to the view. This way we are able to decouple the three components, making it easy to update any functionality needed.

### Code Strategy
I started first with defining my models.

A gameboard: An array of array of numbers.

A tetromino: An array of array of numbers

eg 

```
[
  [0, 0, 0, 0],
  [1, 1, 1, 1],
  [0, 0, 0, 0],
  [0, 0, 0, 0]
]

```
represents a horizontal straight tetromino.


A sidebar: simply generates and keeps 3 tetrominoes up next.

### To Play

`git clone` the repo in your python IDE and make sure pygame is installed.
run the main program and have fun!

#### Controls:

- arrow keys : move the tetromino
- F : store a tetromino
- space: hard place
- A : rotate left
- D : rotate right
- Esc : pause

<i> Things left to do:</i>

<i>Implement rounds of gameplay</i>
