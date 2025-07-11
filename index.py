import pyautogui
import random
import time

# --- Configuration ---
# How often to check if the mouse has moved (in seconds)
CHECK_INTERVAL = 5

# How long to wait before moving the mouse (in seconds) if no user activity is detected
INACTIVITY_THRESHOLD = 30 # 5 minutes (5 * 60 seconds)

# Duration for the mouse movement (makes it smoother)
MOVE_DURATION = 1.0 # 1 second

# --- Initialization ---
last_mouse_x, last_mouse_y = pyautogui.position()
last_user_move_time = time.time() # Tracks the last time the user moved the mouse
screen_width, screen_height = pyautogui.size()

print('Anti Desk Time script started. Monitoring mouse activity...')
print(f'Will move mouse if inactive for {INACTIVITY_THRESHOLD} seconds.')
print('Press Ctrl-C to stop the script.')

try:
    while True:
        current_mouse_x, current_mouse_y = pyautogui.position()
        current_time = time.time()

        # Check if the user has moved the mouse
        if current_mouse_x != last_mouse_x or current_mouse_y != last_mouse_y:
            last_user_move_time = current_time # Update the last user move time
            last_mouse_x = current_mouse_x
            last_mouse_y = current_mouse_y
            # Optional: print a message when user moves mouse
            # print(f"User moved mouse at {time.ctime(current_time)}")

        # Check if enough time has passed without user activity
        time_since_last_user_move = current_time - last_user_move_time

        if time_since_last_user_move >= INACTIVITY_THRESHOLD:
            # Generate random coordinates within the screen boundaries
            target_x = random.randint(0, screen_width - 1)
            target_y = random.randint(0, screen_height - 1)

            print(f"[{time.ctime(current_time)}] Inactivity detected! Moving mouse to ({target_x}, {target_y})...")
            
            # Move the mouse to the random target
            pyautogui.moveTo(target_x, target_y, duration=MOVE_DURATION)

            # After moving, update last_user_move_time to current_time
            # This prevents it from immediately moving again right after its own move
            last_user_move_time = time.time()
            last_mouse_x, last_mouse_y = pyautogui.position() # Update position after our move
            print("Mouse moved. Resetting inactivity timer.")

        # Wait for the next check interval
        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print('\nAnti Desk Time script stopped.')
    print(f"Last user activity detected at: {time.ctime(last_user_move_time)}")