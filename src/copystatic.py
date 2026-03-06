import shutil
import os

#Use recursion to walk through directory, build source paths and destination paths and copy over
def copy_recursive(source, destination):
    for filepath in os.listdir(source):
        source_path = os.path.join(source, filepath)
        destination_path = os.path.join(destination, filepath)
        
        # Skip hidden files and Windows NTFS Alternative Data Streams
        if filepath.startswith("."):
            continue
        
        if os.path.isfile(source_path):
            print(f"Copying {source_path} to {destination_path}")
            shutil.copy(source_path, destination_path)

        else:
            os.mkdir(destination_path)
            print(f"Creating directory {destination_path}")
            copy_recursive(source_path, destination_path)


#Cleanup destination filepath, create new destination, use recursion copy_recursive to transfer files into new location
def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    
    os.mkdir(destination)
    
    copy_recursive(source, destination)
    
    
    
    
            