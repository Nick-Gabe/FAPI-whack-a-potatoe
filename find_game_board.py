import pyautogui

gameBoardLocation = pyautogui.locateOnScreen(
            image="img/game_board.png",
            confidence=0.8,
            grayscale=True
        )
print ("Game Board Location:")
print (gameBoardLocation)

pyautogui.screenshot(
    imageFilename="img/region_test.png",
    region=gameBoardLocation
)
