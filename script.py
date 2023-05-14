import pyautogui
import keyboard

running, isHolding = False, False
startStopKey = "f8"
exitScriptKey = "f10"

print("Starting WhackaMoler@1.0.1")
print(f"{startStopKey} - Start / Stop")
print(f"{exitScriptKey} - Exit Script")
print("-" * 20)
print("Running" if running else "Stopped")

while True:
    if keyboard.is_pressed(startStopKey) == True:
        if isHolding == False:
            isHolding = True
            
            gameBoardLocation = pyautogui.locateOnScreen(
                image="img/game_board.png",
                confidence=0.8,
                grayscale=True
            )

            if gameBoardLocation == None:
                print("-" * 20)
                print ("Couldn't find game board, stopping...")
                running = False
        
            else:
                print("-" * 20)
                print("Stopped" if running else "Running")

                running = not running

                if running == True:
                    print ("Game Board Location:")
                    print (gameBoardLocation)
    else:
        isHolding = False

    if keyboard.is_pressed(exitScriptKey) == True:
        print("-" * 20)
        print("Exiting Script...")
        break

    if running:
        location = pyautogui.locateOnScreen(
            image="img/eye.png",
            confidence=0.8,
            region=gameBoardLocation,
            grayscale=True
        )

        if location:
            pyautogui.click(location)
