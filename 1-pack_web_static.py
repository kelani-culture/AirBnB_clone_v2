#!/usr/bin/python3
from fabric.api import local
import os
from datetime import datetime
"""
compress file to tgz
"""

def do_pack():
    """
    A function that compress a file 
    """
    source_folder = 'web_static'
    dest_folder = 'versions'

    if not os.path.isdir(dest_folder):
        os.makedirs(dest_folder)

    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    web_time = f'{source_folder}_{timestamp}.tgz'
    archived_path = os.path.join(dest_folder, web_time)
 
    result = local(f"tar -cvzf {archived_path} {source_folder}")
    if result.fail:
        return None
    
    return archived_path
    
