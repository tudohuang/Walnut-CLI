import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import pyfiglet
import webbrowser
import time
import threading
import sys
from colorama import init, Fore
import random
import qrcode
from PIL import Image, ImageSequence
from tqdm import tqdm
import wget, tarfile
import os
import zipfile
import rarfile



    


init()
count = 0
unzip = False
with open("C:\\Gdrive_tudo\\code\\Browser\\ascii_art.txt", 'r') as f:
    ascii_art = f.read()

with open("C:\\Gdrive_tudo\\code\\Browser\\新文字文件.txt", 'r') as f:
    cool1 = f.read()

# Checks if the four digit number doesn't have repeating digits or zero


def starting():
    for iii in range(0,101,10):
        sys.stdout.write(Fore.GREEN + f'\rWalnut@terminal:~$ loading | {iii}%' + Fore.RESET)
        time.sleep(0.1)
        sys.stdout.write(Fore.GREEN + f'\rWalnut@terminal:~$ loading / {iii}%' + Fore.RESET)
        time.sleep(0.1)
        sys.stdout.write(Fore.GREEN + f'\rWalnut@terminal:~$ loading - {iii}%' + Fore.RESET)
        time.sleep(0.1)
        sys.stdout.write(Fore.GREEN + f'\rWalnut@terminal:~$ loading \\ {iii}%' + Fore.RESET)
        time.sleep(0.1)
        if iii == 100:
            sys.stdout.write(Fore.GREEN + f'\rWalnut@terminal:~$ loading {iii}%   \n')


def script():
    cool_code_part1 = """
if (typeof emitter.prependListener === 'function') {
    return emitter.prependListener(event, fn);
  } else {
    // This is a hack to make sure that our error handler is attached before any
    // userland ones.  NEVER DO THIS. This is here only because this code needs
    // to continue to work with older versions of Node.js that do not include
    // the prependListener() method. The goal is to eventually remove this hack.
    if (!emitter._events || !emitter._events[event]) emitter.on(event, fn);else if (isArray(emitter._events[event])) emitter._events[event].unshift(fn);else emitter._events[event] = [fn, emitter._events[event]];
  }
}
"""

    type_writer(cool_code_part1, 0.001)

def cool():
    type_writer(cool1, 0.01)

def download_and_extract(url, out_filename):
    try:
        # Download the file
        wget.download(url, out=out_filename)
        print(f"Downloaded {out_filename} successfully.")
        
        # Determine the file type and extract
        if out_filename.endswith('.tar.gz'):
            with tarfile.open(out_filename, 'r:gz') as tar:
                tar.extractall()
                unzip = True
        elif out_filename.endswith('.zip'):
            with zipfile.ZipFile(out_filename, 'r') as zip_ref:
                zip_ref.extractall()
                unzip = True
        elif out_filename.endswith('.rar'):
            with rarfile.RarFile(out_filename, 'r') as rar_ref:
                rar_ref.extractall()
                unzip = True
        else:
            unzip = False
            return "Unsupported file type."

        # Remove the downloaded file
        if unzip == True:
            os.remove(out_filename)
            print(f"Removed {out_filename} successfully.")

        return "Operation completed successfully."
        
    except Exception as e:
        return f"An error occurred: {e}"





def image_to_asciiH(image_path, output_width=100, character_set=None):
    if character_set is None:
        # 使用更多的字符來表示不同的灰度級別
        character_set = "@%#WMN8B@WMmamwoc=;:-,. "
    
    char_len = len(character_set)
    
    # 使用 os.path.join 以避免跨平台問題
    image_path1 = image_path.replace("\\", "/")
    
    img = Image.open(image_path1).convert("L")  # Convert image to grayscale
    width, height = img.size
    ratio = height / width
    output_height = int(output_width * ratio)
    img = img.resize((output_width, output_height))
    
    pixels = img.getdata()
    
    # 使用更多的字符會影響灰度級別的計算
    grayscale_characters = [character_set[pixel * (char_len - 1) // 255] for pixel in pixels]
    grayscale_characters = [grayscale_characters[index: index + output_width] for index in range(0, len(grayscale_characters), output_width)]

    for row in grayscale_characters:
        print("".join(row))

def image_to_ascii(image_path, output_width=100, character_set=None):
    if character_set is None:
        character_set = "@%#*+=-:. "
    
    char_len = len(character_set)
    image_path1 = image_path.replace("\\", "/")
    img = Image.open(image_path1).convert("L")  # Convert image to grayscale
    width, height = img.size
    ratio = height / width
    output_height = int(output_width * ratio)
    img = img.resize((output_width, output_height))
    
    pixels = img.getdata()
    grayscale_characters = [character_set[pixel * (char_len - 1) // 255] for pixel in pixels]
    grayscale_characters = [grayscale_characters[index: index + output_width] for index in range(0, len(grayscale_characters), output_width)]

    for row in grayscale_characters:
        print("".join(row))

def animate():
    global done
    while done == 'false':
        sys.stdout.write(Fore.GREEN + '\rWalnut@terminal:~$ loading |' + Fore.RESET)
        time.sleep(0.1)
        sys.stdout.write(Fore.GREEN + '\rWalnut@terminal:~$ loading /' + Fore.RESET)
        time.sleep(0.1)
        sys.stdout.write(Fore.GREEN + '\rWalnut@terminal:~$ loading -' + Fore.RESET)
        time.sleep(0.1)
        sys.stdout.write(Fore.GREEN + '\rWalnut@terminal:~$ loading \\' + Fore.RESET)
        time.sleep(0.1)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def image_to_ascii(image, width=80):
    ascii_str = ""
    img_width, img_height = image.size
    ratio = img_height / img_width / 1.65
    height = int(width * ratio)
    image = image.resize((width, height))
    pixels = image.getdata()
    grayscale_characters = "@%#*+=-:.  "
    
    for pixel_value in pixels:
        ascii_str += grayscale_characters[pixel_value // 25]
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    
    for i in range(0, ascii_str_len, width):
        ascii_img += ascii_str[i:i+width] + "\n"
        
    return ascii_img

def gif_to_ascii(gif_path, width=100, sec=0, last=20):
    gif = Image.open(gif_path)
    for ii in range(20):
        for frame in ImageSequence.Iterator(gif):
            gray_frame = frame.convert("L")
            ascii_art = image_to_ascii(gray_frame, width=width)
            
            clear_console()
            print(ascii_art)
            time.sleep(sec)

def type_writer(message, delay=0.03):
    colored_message = Fore.GREEN + message + Fore.RESET
    for char in colored_message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def get_password(prompt="Please Enter Password: "):
    type_writer(prompt)
    password = ""
    try:
        if sys.platform == "win32":
            import msvcrt
            while True:
                char = msvcrt.getch().decode('utf-8')
                if char == '\r': # Enter key pressed
                    print()
                    break
                elif char == '\x08': # Backspace key pressed
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
                else:
                    password += char
                    print(Fore.GREEN + '*', end='', flush=True)
        else:
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                import tty
                tty.setraw(sys.stdin.fileno())
                while True:
                    char = sys.stdin.read(1)
                    if char == '\n':
                        print()
                        break
                    elif char == '\x7f': # Backspace key pressed
                        password = password[:-1]
                        print('\b \b', end='', flush=True)
                    else:
                        password += char
                        print('*', end='', flush=True)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except Exception as e:
        print(f"An error occurred: {e}")
    return password



def print_title(word):
    art_title = pyfiglet.figlet_format(word)
    print(Fore.GREEN + art_title + Fore.RESET)

def random_code_scroll():
    lines = ["[INFO] Scanning ports...", "[DEBUG] Trying password...", "[ERROR] Access denied!", "[SUCCESS] Connected!"]
    for _ in range(5):
        print(Fore.GREEN + f"Walnut@terminal:~$ {random.choice(lines)}", 'green')
        time.sleep(0.5)

def search_google(query):
    try:
        url = "https://www.google.com/search?q=" + query
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []
        for g in soup.find_all('a', href=True):
            link = g['href']
            if link.startswith("/url?q="):
                link = link.split("&")[0].replace("/url?q=", "")
                results.append(link)
        return results
    except Exception as e:
        print(f"Error!: {e}")
        return []

def asciiart():
    mask = ascii_art
    print(Fore.GREEN + mask)


def main():
    global done
    done = 'false'
    query = input(Fore.GREEN + "hacker@terminal:~$ Please enter the query string you want to search (or enter '!quit' to exit): " + Fore.RESET)
    if query == "!quit":
        done = 'true'
        return query
    type_writer(Fore.GREEN + f"hacker@terminal:~$ Searching for: {query}\n" + Fore.RESET)
    loading_thread = threading.Thread(target=animate)
    loading_thread.start()
    results = search_google(query)
    done = 'true'
    loading_thread.join()
    if results:
        print(Fore.GREEN + "Results found:" + Fore.RESET)
        for idx, result in enumerate(results, 1):
            print(Fore.GREEN + f"{idx}: {result}" + Fore.RESET)
        selected_indices = input(Fore.GREEN + "Please enter the indices of the results you want to open (e.g. 1,3,5) or 'q' to quit: " + Fore.RESET)
        if selected_indices.lower() == 'q':
            return
        selected_indices = selected_indices.split(',')
        for idx_str in selected_indices:
            idx = int(idx_str)
            if idx > 0 and idx <= len(results):
                result = results[idx - 1]
                decoded_url = unquote(result)
                webbrowser.open(decoded_url, new=2)
                print(Fore.GREEN + f"Opening {decoded_url} ..." + Fore.RESET)
            else:
                print(Fore.GREEN + f"Index {idx} is invalid." + Fore.RESET)
    else:
        print(Fore.GREEN + "No results found" + Fore.RESET)
    return query



# Function to display a hacker-style loading bar
def display_loading_bar(duration):
    for i in tqdm(range(100), desc=f"{Fore.GREEN}Walnut@terminal:~$ loading", ncols=100):
        time.sleep(duration / 100)
    print(Fore.GREEN + "Walnut@terminal:~$ loading \\ 100%" + Fore.RESET)

# Function to convert JPG to PNG with hacker-style loading bar and message
def jpg_to_png(path_to_image, save_path="C:\\Users\\tudo\\Downloads"):
    try:
        img = Image.open(path_to_image)
        display_loading_bar(0.05)
        if save_path is None:
            save_path = path_to_image.rsplit('.', 1)[0] + '.png'
        img.save(save_path, 'PNG')
        return Fore.GREEN + f"Walnut@terminal:~$ Successfully converted {path_to_image} to PNG and saved as {save_path}." + Fore.RESET
    except Exception as e:
        return Fore.RED + f"Walnut@terminal:~$ An error occurred: {e}" + Fore.RESET

# Function to convert PNG to JPG with optional save_path and hacker-style loading bar and message
def png_to_jpg(path_to_image, save_path="C:\\Users\\tudo\\Downloads"):
    try:
        img = Image.open(path_to_image)
        display_loading_bar(0.05)
        if save_path is None:
            save_path = path_to_image.rsplit('.', 1)[0] + '.jpg'
        img = img.convert("RGB")
        img.save(save_path, 'JPEG')
        return Fore.GREEN + f"Walnut@terminal:~$ Successfully converted {path_to_image} to JPG and saved as {save_path}." + Fore.RESET
    except Exception as e:
        return Fore.RED + f"Walnut@terminal:~$ An error occurred: {e}" + Fore.RESET

# Function to generate QR code with hacker-style loading bar and message
def generate_qrcode(url, save_path="C:\\Users\\tudo\\Downloads"):
    global count  # Use the global count variable
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Generate a default save_path if not provided
        if save_path is None:
            save_path = f"QRCode_{count}.png"
        
        display_loading_bar(0.05)
        img.save(save_path)
        count += 1  # Increment the count for next time
        
        return Fore.GREEN + f"Walnut@terminal:~$ Successfully generated QR code for {url} and saved as {save_path}." + Fore.RESET
    except Exception as e:
        return Fore.RED + f"Walnut@terminal:~$ An error occurred: {e}" + Fore.RESET
    
def check(num):
    a, b, c, d = str(num)
    if a in [b, c, d] or b in [a, c, d] or c in [a, b, d] or '0' in [a, b, c, d]:
        return False
    else:
        return True

# Compares two four digit numbers and returns the count of same digits at same and different positions
def compare(num4, guess4):
    count_same_pos = 0
    count_diff_pos = 0
    for i in [0, 1, 2, 3]:
        if num4[i] == guess4[i]:
            count_same_pos += 1
        if num4[i] in guess4:
            count_diff_pos += 1
    count_same_num = count_diff_pos - count_same_pos
    return count_same_pos, count_same_num

# List of all four digit numbers that do not have repeating digits and do not include zero
numbers = [str(i) for i in range(1234, 10000) if check(i)]

def perform_attack(a,b,guess):
    global numbers

    possible_answers = [g4 for g4 in numbers if compare(guess, g4) == (a, b)]

    if len(possible_answers) == 1:
        result = possible_answers[0]
        print(Fore.GREEN + f"The result is {result}. Only one possible answer left!" + Fore.RESET)
    else:
        random.shuffle(possible_answers)
        result = possible_answers[0]
        print(Fore.GREEN + f"The possible result is {result}" + Fore.RESET)

    numbers = possible_answers
