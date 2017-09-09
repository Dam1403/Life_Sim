import win32gui
import win32api
import win32con
import os



HWND = ""
HINST = ""



Black = "0"
Blue = "1"
Green = "2"
Aqua = "3"
Red = "4"
Purple = "5"
Yellow = "6"
White = "7"
Gray = "8"
Light_Blue = "9"
Light_Green = "A"
Light_Aqua = "B"
Light_Red = "C"
Light_Purple = "D"
Light_Yellow = "E"
Bright_White = "F"


class Window():



	def __init__(self):
		self.title = ""
		self.background_color = "0"
		self.text_color = "7"
		args = []
		HINST = win32api.GetModuleHandle()
		win32gui.EnumWindows(set_hwnd,args
		win32gui.CreateWindow(\
			"DougWindow",\
			"GameWindow",\
			win32con.WS_BORDER,\
			0,\
			0,\
			600,\
			600,\
			None,\
			None,\
			HINST,\
			None
			)

	def set_window_name(self,title):
		self.title = title
		win32gui.SetWindowText(HWND,title)

	def set_background_color(self,color):
		self.background_color = color
		os.system("color " + color+self.text_color)

	def set_text_color(self,color):
		self.text_color = color
		os.system("color " + self.background_color+color)


def set_hwnd(hWnd,args):
	title = win32gui.GetWindowText(hWnd)
	global HWND
	

	if "python" in title:
		HWND = hWnd
		
		



