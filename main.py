import win32gui
import win32api
import win32con
import threading 

import time



HINST = win32api.GetModuleHandle()
HWND = ""
def main():
	args = []

	wc = win32gui.WNDCLASS()
	wc.hInstance = HINST
	wc.lpszClassName = "DougWindow"
	win32gui.RegisterClass(wc)
	#ha = window.Window()
	#ha.set_background_color("F")
	#ha.set_text_color("2")
	HWND = win32gui.CreateWindow(\
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
			None)
	win32gui.ShowWindow(HWND,5)
	
	aThread = threading.Thread(target=i_live)
	aThread.start()
	win32gui.PumpMessages()
	
		



def i_live():
	print("GOTCHA!!")
	input("")

main()


