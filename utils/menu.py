from utils.roprodownloader import RoProDownloader
import pyautogui,subprocess
from plyer import notification
import time as t
class RoProPatcherMenu:
    def __init__(self):
        self.browsers = ['Edge', 'Chrome']
        self.downloader = RoProDownloader('https://example.com/ropro.zip', '.')

    def asciindesign(self):
        print("""
██████╗  ██████╗ ██████╗ ██████╗  ██████╗     ██████╗  █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝██████╔╝██║   ██║    ██████╔╝███████║   ██║   ██║     ███████║█████╗  ██████╔╝
██╔══██╗██║   ██║██╔═══╝ ██╔══██╗██║   ██║    ██╔═══╝ ██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║     ██║  ██║╚██████╔╝    ██║     ██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
════════════════════════════════@Codepulze══════════════════════════════════════════════════════════════
                                ═ >[1.0.0]
1. Edge                         ═ >[https://github.com/EvilBytecode]
2. Chrome                       ════════════════════════════════════
              
> [NOTE] If you have any other webbrowser, just open extenstion tabs, and enable developer mode and press option load unpacked
        """)

    def automatesteps(self):
        self.asciindesign()
        inputlol = int(input("Select a browser (enter the number): "))

        if 1 <= inputlol <= len(self.browsers):
            selected_browser = self.browsers[inputlol - 1]
            print(f"You selected: {selected_browser}")

            self.downloader.downnextract()

            if selected_browser == 'Edge':
                subprocess.run(['taskkill', '/f', '/im', 'msedge.exe'])
                msedge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                subprocess.Popen([msedge_path])
                t.sleep(1)
                pyautogui.press('f11')

                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite('edge://extensions')
                pyautogui.press('enter')
                notification_title = "READ ME!"
                notification_text = "Please Enable Developer Mode, and press at top Load Unpacked and choose the ropro folder in current directory, if issues check github"
                notification.notify(title=notification_title,message=notification_text)
                t.sleep(1000)
            elif selected_browser == 'Chrome':
                subprocess.run(['taskkill', '/f', '/im', 'chrome.exe'])
                xhrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                subprocess.Popen([xhrome])
                t.sleep(1)
                pyautogui.press('f11')
                pyautogui.hotkey('ctrl', 't')
                pyautogui.typewrite('chrome://extensions')
                pyautogui.press('enter')
                notification_title = "READ ME!"
                notification_text = "Please Enable Developer Mode, and press at top Load Unpacked and choose the ropro folder in current directory, if issues check github"
                notification.notify(title=notification_title,message=notification_text)
                t.sleep(1000)
            else:
                print("Invalid browser selection.")
        else:
            print("Invalid input. Please select a valid option.")

menu = RoProPatcherMenu()
menu.automatesteps()
