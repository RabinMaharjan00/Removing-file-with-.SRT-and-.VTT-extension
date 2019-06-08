# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:11:49 2019

@author: Rabin maharjan
"""

import os
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("--src","--source",dest="paths", help="Removing file with extension .SRT and .VTT")
    (options,arguments)=parser.parse_args()
    if not options.paths:
        parser.error("[-] Please specify source, use --help for more info.")
    return options
    

def Source_folder(folder_path):
    for folderName,subfolders,filename in os.walk(folder_path):
        try:
            for file in filename:
                if file.endswith('.vtt') or file.endswith('.srt') :
                    os.remove(os.path.join(folderName,file))
            
        
        except :
            print("Error during deleting",file)
            
            
            
options = get_arguments()
Source_folder(options.paths)

        
        