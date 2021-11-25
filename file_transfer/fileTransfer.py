import shutil
import os
import time
import datetime

import fileTransfer_main
import fileTransfer_gui



def transfer(self):
    #   Set where the source of the files are
        #'/Users/Tien/Desktop/file_transfer/Folder_A/'
    source = self.txt_bar1.get()

    #   Set the destination path to folder B
        #'/Users/Tien/Desktop/file_transfer/Folder_B/'
    destination = self.txt_bar2.get()
    files = os.listdir(source)


    for i in files:
        
        #   Get the times created and modified and having it displayed in a specific format
        #ti_c = os.path.getctime(source+i)
        #c_ti = time.ctime(ti_c)
        #m_ti = time.ctime(ti_m)
        
        #   Grabs the time of each individual file
        ti_m = os.path.getmtime(source+'/{}'.format(i))

        #   Get last modified date and today's date
        dateModified = datetime.datetime.fromtimestamp(ti_m)
        todaysDate = datetime.datetime.today()
        #    Will check to see if modified within last 24 hours
        modified24h = dateModified + datetime.timedelta(days=1)

        #   If modified, will move the files to destination folder
        if modified24h > todaysDate:
        #   Displays information of file
        #print("The file '{}' was created at '{}' and was last modified at '{}'".format(i, c_ti, m_ti))
    
        #   We are saying move the files represented by 'i' to their new destination
            shutil.move(source+'/{}'.format(i), destination)
