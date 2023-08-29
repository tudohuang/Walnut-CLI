from PIL import Image, ImageSequence
import time
import os
import curses
def display_ascii_gif(stdscr, gif_path, width=100, sec=0.1):
    # Initialize curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(1))

    # Load GIF
    try:
        gif = Image.open(gif_path)
    except Exception as e:
        raise ValueError(f"Failed to open image at {gif_path}: {e}")

    last_ascii_art = None
    
    # Loop through GIF frames
    for ii in range(20):
        for index, frame in enumerate(ImageSequence.Iterator(gif)):
            if (index + 1) % 2 != 0:
                try:
                    gray_frame = frame.convert("L")
                except Exception as e:
                    raise ValueError(f"Failed to convert frame to grayscale: {e}")

                # Create ASCII art
                ascii_art = ""
                img_width, img_height = gray_frame.size
                ratio = img_height / img_width / 1.65
                height = int(width * ratio)
                gray_frame = gray_frame.resize((width, height))
                pixels = gray_frame.getdata()
                grayscale_characters = "@%#*+=-:.  "
                
                for pixel_value in pixels:
                    ascii_art += grayscale_characters[pixel_value // 25]
                
                ascii_art_len = len(ascii_art)
                ascii_img = ""
                
                for i in range(0, ascii_art_len, width):
                    ascii_img += ascii_art[i:i+width] + "\n"
                
                # Display ASCII art
                if ascii_img != last_ascii_art:
                    stdscr.clear()
                    stdscr.addstr(0, 0, ascii_img)
                    stdscr.refresh()
                    last_ascii_art = ascii_img
                
                time.sleep(sec)
def display(gif_path,width):
    curses.wrapper(display_ascii_gif, gif_path, int(width))