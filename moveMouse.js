var robot = require('robotjs')
function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }



function move(){

var twoPI = Math.PI*2.0;
var screenSize = robot.getScreenSize();
var height = (screenSize.height/2)-10;
var width = screenSize.width;

    //Straight line
    
    x = width/4;
    y = height/4;
    robot.moveMouse(x,y);
    console.log("Mouse Position: ", x, y);
    robot.mouseClick("right")
    sleep(1000)
    robot.mouseClick("left")
    
    x = width-width/4;
    y = height-height/4
    console.log("Mouse Position: ", x, y);
    robot.moveMouseSmooth(x,y);
    robot.mouseClick("right")
    robot.moveMouseSmooth(x,y+80)
    robot.moveMouseSmooth(x+20, y+80)
    robot.mouseClick("left")
    console.log("Sleeping, You have mouse control now")
    sleep(5000)
    
}
setInterval(move, 1000);
