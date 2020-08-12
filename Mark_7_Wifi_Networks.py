import subprocess
import tkinter
from tkinter import*
root=Tk()
root.geometry("500x500")
root.title("WI-FI-NETWORKS")
def ShowWifi():
    results=subprocess.check_output(["netsh","wlan","show","profiles"]).decode("utf-8").split("\n")
    results=[i.split(":")[1][1:-1] for i in results if "All User Profile" in i]
    for i in results:
        results1=subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8').split("\n")
        results1=[b.split(":")[1][1:-1] for b in results1 if "Key Content" in b]
        try:
             ssids=str(i)+str(results1)
             Label1=Label(root,padx=50,pady=90,font=('Algerian',16),text=ssids)
             Label1.grid(row=1,columnspan=1)
        except IndexError:
            label2=Label(root,padx=50,pady=90,font=('Algerian',16))
            label2.grid(row=1,columnspan=1)

    
   

Show_button=Button(root,text="Show Networks",command=ShowWifi,font=('Algerian',16))
Show_button.grid(row=0,columnspan=2,padx=90,pady=30)
root.mainloop()