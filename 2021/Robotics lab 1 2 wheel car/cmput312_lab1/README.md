Eniac the Differential Drive Robot
----------------------------------
LAB 1: Differential Drive Vehicle
10%
For this lab you will need to do the following:


1) Build a differential drive vehicle & get familiar with ev3dev environment
    Using your EV3 Lego Kit construct a differential drive vehicle. 
Take photos of all design iterations and include in your report.
    Read/run sample codes and understand how they work 
(make sure that appropriate sensors/motors are connected). 


2) Error data collection & analysis
    Write a program to collect the following data:

    Design two ways of measuring the error when your robot is moving in straight line. 
    At least one of them must use input from some sensors. Compare the two methods. What do you find? 
    (Have to redo with power input...)
    Design two ways of measuring the error when the robot is rotating. 
    At least one of them must use input from some sensors. 
    Compare the two methods. What do you find? 
    (haven't yet made it do a full theoretical 360 but will use gyro and tape to check)

    How does error accumulate in rotation and linear movements of your robot, as a function of the
power applied to the robot motors? Add your answers to the report. 
Use these methods to collect data in parts 3 & 4. 


3) Perform the following shape movements
    Write a program that receives as input one of the following four shapes and performs the desired movement:

        Move the robot in a rectangle
        Move the robot in a lemniscate
        Move the robot in a straight line (optional)
        Move the robot in a circle (optional)

    Add a pen or pencil to your robot in such a way that you can draw the above shapes 
    (line, rectangle, circle, figure-eight) when placing the robot over a sheet of paper. 
    Draw each shape at least 3 times. What can be concluded and why? 
    State your answer in the report and provide an error analysis of your results. 
    Include photos of each drawn shape in the report. 


4) Implement a dead reckoning position controller on your robot
    Write a program that receives as input a 3x3 array. 
    The first two columns are the left and right motor power respectively, 
    the last column is the time during which the power is apply to the motors. 
    Your program has to read each row in sequence and for each row the robot has to apply power 
    to the motors according to columns 1 and 2 and maintain this value for duration stated in column 3.

Example input:

                        int[][] command = {
                            { 80, 60, 2},
                            { 60, 60, 1},
                            {-50, 60, 4}
                        };
                        

    row1: During the 1st 2 seconds motor one and motor two are powered with 80% and 60% of their max 				capacity
    row2: During the 3rd second motor one and two are powered with 60% and 60% of their max capacity
    row3: During seconds 4 and 5 motors one and two are powered with -50% and 60% of their max capacity 		(the minus means change in rotation direction) 

After it is done executing all three rows the robot has to transmit its location and orientation 
to the PC and/or show it in the display. Make sure you add some lego blocks structure to be 
able to align your robot with the (0,0) coordinate reference frame. 
Describe your implementation in detail in your report. 
Run the program at least 3 times (on the above input), 
collect data (draw the trajectory on paper) and include an 
error analysis in your report with photos.

5) Convert your differential drive vehicle into a Braitenberg vehicle
    Using light detecting sensors, implement the following behaviours in 
reaction to a light source on your robot:

        Cowardice  --> run from light source
        Aggression --> speed up toward light source
        Love (optional) --> make circles around the light source
        Curiosity (optional) --> slowly aproach light and lightly tap it, reverse and repeat

    Include videos of your robot demonstrating each behaviour in your report. 

6) Final project planning
    Open the final project planning Google document shared with you and answer the question for lab 1. 
If you do not have access to the document, please speak with the TA. 

Demo:

        Points 3, 4 and 5. 

What to hand in:

A tarfile electronically on eClass. The tarfile has to contain your implementations and 
any data you either measured or generated. Download the sample file structure to use as a template.
