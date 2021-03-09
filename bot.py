#!/usr/bin/env python3
from os import system
from time import sleep


try:
   system('clear')
   print("       __  ___           __  _")       
   print("   /  |/  /_  _______/ /_(_)___ ___  _____ ") 
   print("  / /|_/ / / / / ___/ __/ / __ `/ / / / _ \\")
   print(" / /  / / /_/ (__  ) /_/ / /_/ / /_/ /  __/") 
   print("/_/  /_/\__, /____/\__/_/\__, /\__,_/\___/ ") 
   print("       /____/              /_/             ") 
   print(" Coded by: Ph.Phoenix ")
   print("'Dont just learn it, master it.'")
   print(" Facebook: https://www.facebook.com/profile.php?id=100051284011748 \n")

   threads = int(input("threads: "))
   time = int(input("time: "))
   link = input("link: ")

   #change this to open a normal window or private window (remove --private-window)
   browser = f"proxychains firefox --private-window {link}"

   x = 0
   x += 1
   
   print("\n")
   try:
      for x in range(threads):
         system(browser)
         print(f"{x} | {link} ==> success \n")
         sleep(time)
   except KeyboardInterrupt:
      print("Cancelling...")
      sleep(2)
      print("Cancelled \n")

except ValueError:
   print("Please enter a thread (numeric)")

