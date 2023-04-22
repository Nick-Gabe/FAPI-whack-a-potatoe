import pyautogui
import keyboard

running, isHolding = False, False
startStopKey = "f8"

print("Starting WhackaMoler@1.0.0")
print(f"{startStopKey} - Start / Stop")
print("-" * 20)
print("🟩 Running" if running else "🛑 Stopped")

while True:
    if keyboard.is_pressed(startStopKey) == True:
        if isHolding == False:
            isHolding = True
            print ("\033[A                             \033[A")
            print("🛑 Stopped" if running else "🟩 Running")
            running = not running
    else:
        isHolding = False

    if running:
        location = pyautogui.locateOnScreen(
            image="img/eye.png",
            confidence=0.8,
            region=[350,280,620,570]
        )

        if location:
            pyautogui.click(location)