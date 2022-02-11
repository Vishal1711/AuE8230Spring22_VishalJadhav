# Assignment 2 Turtlesim Basics

In source `src` folder -
  - `launch` folder contain launch files
  - `scipts` folder contains python scripts

## 1. Circle.py:

  - This code controls the turtlebot and moves it in a circular path.
  - It runs the turtlebot with pre-decided linear and angular velocities.
  - The bot stops moving after it completes one circle.
  - To run this program, run the below command in the package (roslaunch):
  
  
    `roslaunch assignment2_turtlesim circle.launch`
    
    
  
![circle](https://user-images.githubusercontent.com/79803663/153536356-50fc6395-dbad-49cb-bae5-291f6962e628.png)

## 2. Square_Open_loop:

  - This code runs the turtlebot in a square of 2x2 units once.
  - Turtle move with 0.2 linear velocity and 0.2 rad/s angular velocity
  - To run this program, run the below command:
  
    `roslaunch assignment2_turtlesim openloop.launch`
    
    
![openloop](https://user-images.githubusercontent.com/79803663/153536575-13d287bb-bf3f-46d1-91c4-aa2954928a5f.png)

3. Square_Closed_loop:

  - This code runs the turtle bot from its starting position to the coordinates (5,5)
  - From here the bot sequentially moves along the following coordinates and completes a 3x3 units square: (8,5); (8,8); (5,8); (5,5)
  - To run this program, run the below command:
  
  `roslaunch assignment2_turtlesim openloop.launch`
  
  
  ![closeloop](https://user-images.githubusercontent.com/79803663/153536697-61be1985-7b56-4e7d-87f7-2bd477eac4d2.png)
