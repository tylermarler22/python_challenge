from tkinter import *
from tkinter import filedialog, messagebox
import ipSearch
import ipLocation
import ipFilter
root = Tk()

def browse():
    fileName = filedialog.askopenfilename()
    pathLabel.config(text=fileName)
def search():
    fileName = pathLabel.cget("text")
    if fileName == "":
        messagebox.showerror("Cannot Search File", "Please enter a valid file directory")
        pathLabel.config(text = fileName)
    elif fileName.endswith('.txt'):
        ipListText.config(state=NORMAL)
        ipListText.delete(1.0,INSERT)
        if checkV.get() == 0:
            ipList = ipSearch.search(fileName)
            ipListText.insert(INSERT, "\n".join(ipList))
        else:
            ipList = ipSearch.search(fileName)
            ipLocations = ipLocation.locateIp(ipList)
            ipListText.insert(INSERT, '\n'.join([' | '.join([str(item) for item in ip]) for ip in ipLocations]))

        ipListText.config(state = DISABLED)

def filter():
    ipListText.config(state=NORMAL)
    ipListText.delete(1.0, INSERT)
    fileName = pathLabel.cget("text")
    countryName = countryEntry.get()
    cityName = cityEntry.get()
    stateName = stateEntry.get()
    ipName = ipEntry.get()
    if countryName or cityName or stateName:
        result = ipFilter.filterIP((ipLocation.locateIp(ipSearch.search(fileName))),countryName,stateName,cityName)
        ipListText.insert(INSERT, '\n'.join([' | '.join([str(item) for item in ip]) for ip in result]))
    elif ipName:
        result = ipFilter.filterLocation((ipLocation.locateIp(ipSearch.search(fileName))),ipName)
        ipListText.insert(INSERT, '\n'.join([' | '.join([str(item) for item in ip]) for ip in result]))
    else:
        messagebox.showerror("Cannot filter results", "Please enter a search credential")
    ipListText.config(state=DISABLED)

#File Browse Widgets
browseButton = Button(root, text="Browse", command=browse)
browseButton.grid(row = 0, column = 2, sticky = E)
fileLabel = Label(root,text = "Find file:")
fileLabel.grid(row = 0,column = 0, sticky = W)
pathLabel = Label(root)
pathLabel.grid(row = 0, column = 1, sticky = W)


#Ip searching widgets
findButton = Button(root, text="Find file IPs", command = search)
findButton.grid(row = 1,column = 2, sticky = E)

#Ip Location Widgets
checkV = IntVar()
ipListText = Text(root, height =5, width = 110, bg = 'white', state = DISABLED)
ipListText.grid(row = 1, column = 0, columnspan = 2)
ipListScrollBar = Scrollbar(root, orient=VERTICAL, command = ipListText.yview)
ipListScrollBar.grid(row = 1, column = 2, sticky = 'nsw')
ipListText['yscrollcommand'] = ipListScrollBar.set
findLocationCheck = Checkbutton(root, text = "Display GeoLocations", variable = checkV)
findLocationCheck.grid( row = 2, column = 2, sticky = 'w')

#Ip filtering widgets
countryEntry = Entry(root)
countryEntry.grid( row = 3 , column = 1, sticky = W)
stateEntry = Entry(root)
stateEntry.grid(row = 3 , column = 3, sticky = W)
cityEntry = Entry(root)
cityEntry.grid(row = 4 , column = 1, sticky = W)
ipEntry = Entry(root)
ipEntry.grid(row = 4 , column = 3, sticky = W)
countryLabel = Label(root, text= "Filter By Country:").grid(row = 3, column  =0, sticky = W)
stateLabel = Label(root, text= "Filter By State:").grid(row = 3, column  =2, sticky = W)
cityLabel = Label(root, text= "Filter By City:").grid(row = 4, column  =0, sticky = W)
ipLabel = Label(root, text= "Filter By IP:").grid(row = 4, column  =2, sticky = W)
filterButton = Button(root, text = "Filter", command = filter)
filterButton.grid (row = 3, rowspan = 2, column = 4, sticky = E)






root.mainloop()