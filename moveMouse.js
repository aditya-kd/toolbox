var robot = require('robotjs')

function move(){
    
robot.setMouseDelay(2);

var twoPI = Math.PI*2.0;
var screenSize = robot.getScreenSize();
var height = (screenSize.height/2)-10;
var width = screenSize.width;

for(var x=width/4; x<width/2; x++){

    // Sine Wave
    y = (height/4) * Math.sin((twoPI*x)/(width/4))+(height/4);
    robot.moveMouse(x,y)
    robot.mouseClick("right");

    //Straight line
    // x = width/4;
    // y = height/4;
    // console.log("Mouse Position: ", x, y);
    // robot.setMouseDelay(2000);
    // robot.moveMouse(x,y);
    // x = width-width/4;
    // y = height-height/4
    // console.log("Mouse Position: ", x, y);
    // robot.setMouseDelay(2000);
    // robot.moveMouse(x,y);
    // robot.mouseToggle
}
}
setInterval(move, 0);
