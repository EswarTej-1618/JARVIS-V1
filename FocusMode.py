import time 
import datetime
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    current_time = datetime.datetime.now().strftime("%H:%M")
    stop_time = input("Enter the time [e.g., 10:10] 24 hrs format : ")
    
    # 'a' and 'b' for mapping functions more like coordinates
    a = current_time.replace(":",".")
    a = float(a) #convert to float
    b = stop_time.replace(":",".")
    b = float(b)
    
    # calculate stuff
    Focus_Time = b - a
    Focus_Time = round(Focus_Time,3)
    
    host_path = r'C:\Windows\System32\drivers\etc\hosts'
    redirect = '127.0.0.1'
    
    print(current_time)
    time.sleep(2)
    
    # List of websites to block
    website_list = ["www.instagram.com", "instagram.com", "www.youtube.com", "youtube.com", "www.facebook.com", "facebook.com"]
    
    if current_time < stop_time:
        with open(host_path, "r+") as file:
            content = file.read()
            time.sleep(2)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")
                    print("Done, sir.")
                    time.sleep(1)
            print("You are in focus mode, sir! All distractions are blocked!")
    
    # Checking when to exit
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time >= stop_time:
            with open(host_path, "r+") as file:
                content = file.readlines()
                file.seek(0)
                
                for line in content:
                    if not any(website in line for website in website_list):
                        file.write(line)
                
                file.truncate()
                
            print("All websites are unblocked, sir!")
            file = open("TimeNote/focus.txt","a")
            file.write(f",{Focus_Time}") #must write 0 in the focus.txt before starting must should
            file.close()
            break
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
