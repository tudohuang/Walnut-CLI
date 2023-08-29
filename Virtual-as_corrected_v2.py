import utils
import time
import threading
from colorama import init, Fore
import graph
import serial
import serial.tools.list_ports
import time
import os
import ascc
init()

password = "Walnut"  # 設定的密碼
max_attempts = 3  # 允許的最大嘗試次數
done = 'false'  # 用於動畫的變量
title = "Internet Automatic Search Program"
title_words = title.split(" ")
user_input = ''
query=''

def find_arduino_port():
    ports = list(serial.tools.list_ports.comports())
    for port in ports:
        if "Arduino" in port.description:
            return port.device



# 主函數，執行查詢並顯示結果
# 主程序，需要正確的密碼才能訪問

utils.starting()
attempts = 0
while attempts < max_attempts:
    try:
        password_try = utils.get_password()
        if password_try == password:
            start1 = threading.Thread(utils.script())
            start1.start()
            start = threading.Thread(utils.asciiart())
            start.start()
            utils.print_title("     Welcome-Walnut    ")
            time.sleep(2)

            while query != "!quit" and user_input != "!quit":
                
                user_input = input(Fore.GREEN + f'\rWalnut@terminal:~$' + Fore.RESET)
                # Debugging lines
                
                try:
                    if user_input.startswith('!ascii_gif'):
                        _, gif_path, width  = user_input.split(' ')
                        ascc.display(gif_path,int(width))
                    elif user_input.startswith('!JGPG'):
                        _, path_to_image= user_input.split(' ')
                        result = utils.jpg_to_png(path_to_image, )
                        print(Fore.GREEN + result + Fore.RESET)
                    elif user_input.startswith('!PGJG'):
                        _, path_to_image,  = user_input.split(' ')
                        result = utils.png_to_jpg(path_to_image, )
                        print(Fore.GREEN + result + Fore.RESET)
                    elif user_input.startswith('!Qrcode'):
                        _, url,  = user_input.split(' ')
                        result = utils.generate_qrcode(url, )
                        print(Fore.GREEN + result + Fore.RESET)
                    elif user_input.startswith("!graph"):
                        _, expr = user_input.split(" ", 1)
                        expr = expr.strip("\"")  # Remove quotes if they exist
                        graph.draw_graph(expr)
                    elif user_input.startswith('!Search'):
                        for word in title_words:
                            utils.print_title(word)
                            time.sleep(0.5)
                        utils.main()
                        #print("Debug: Updated query:", query)
                    elif user_input.startswith('!fakehacker'):
                        utils.cool()
                    elif user_input.startswith('!random'):
                        _, max1, r  = user_input.split(' ')
                        graph.random_dis(int(max1),int(r))
                    elif user_input.startswith('!wget'):
                        _, url, out_filename  = user_input.split(' ')
                        utils.download_and_extract(url, out_filename)
                    elif user_input.startswith('!3d'):
                        _, type  = user_input.split(' ')
                        if type == 'curve':
                            graph.tdplt()
                        elif type == 'vector':
                            graph.vector()
                    elif user_input.startswith('!ascii_high'):
                        _, image_path, output_width  = user_input.split(' ')
                        
                        
                        utils.image_to_asciiH(image_path, int(output_width))
                    elif user_input.startswith('!ascii'):
                        _, image_path, output_width  = user_input.split(' ')
                        
                        utils.image_to_ascii(image_path, int(output_width))
                    
                    elif user_input.startswith('!Arduino'):
                        arduino_port = find_arduino_port()
                        if arduino_port is None:
                            print("Arduino not found. Please check your connection.")
                        else:
                            # Initialize serial connection
                            ser = serial.Serial(arduino_port, 9600)

                            # Wait for the Arduino to initialize
                            time.sleep(3)

                            # Use the input provided to the function
                            _,user_inputa = user_input.split(' ')
                            #print(user_inputa)
                            # Send user input to Arduino
                            ser.write((user_inputa + '\n').encode())
                            ser.close()
                    elif user_input.startswith("!help"):
                            prompt = '''
!JGPG path
!PGJG path
!Qrcode url 
!graph expr
!Search query
!fakehacker 
!random range times
!wget url
!3d vector/curve
!ascii_high path width
!ascii_gif path width
!Arduino text
'''
                            utils.type_writer(prompt, 0.01)
                    elif user_input.startswith("!Atk"):
                        _, a, b, guess = user_input.split(' ')
                        while int(a) != 4:  # Convert a to an integer
                            utils.perform_attack(int(a), int(b), guess)
                            user_input = input(Fore.GREEN + f'\rWalnut@terminal-Brue Force Attack:~$' + Fore.RESET)
                            a, b, guess = user_input.split(' ')
                            if int(a) == 4:  # Convert a to an integer
                                break
                            
                    else:
                        print(Fore.RED + "Invalid command." + Fore.RESET)
                except Exception as e:
                    print(Fore.RED + f"An error occurred while processing the command: {e}" + Fore.RESET)
                    
        else:
            attempts += 1
            print("Wrong password! Try again.")
            if attempts == max_attempts:
                print("Max attempts reached. Exiting program.")
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}" + Fore.RESET)
