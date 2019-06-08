# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:48:51 2019

@author: Rabin maharjan
"""

import os

path = input("Enter the path of folder: " )

for folderName,subfolders,filename in os.walk(path):
     
     try:
        for file in filename:
            if file.endswith('.vtt') or file.endswith('.srt') :
                os.remove(os.path.join(folderName,file))
            
        
     except :
        print("Error during deleting",file)
        
print("Successfully deleted") 

    
    
        
        
        
