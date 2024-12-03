import os

# Recursive find function signature
def find(path, filename):
    # List all entries (dirs and files) at the given path
    # There is no guarantee that the dirs will be listed first and then files will be listed last
    entries = os.listdir(path=path)
    # Initialize report as empty array first
    report = []

    # Iterate through all entries (dirs and files)
    for entry in entries:
        # Save the full path of our entry (dir or file) to the variable entryPath
        entryPath = os.path.join(path, entry)

        # If our entry is a dir
        if os.path.isdir(entryPath):
            # Recursive call to the find function
            # Use the results of the call of find functions to EXTEND (not append) our report
            report.extend(find(path=entryPath, filename=filename))
        # Else, if our entry is not a dir but a file
        else:
            # If entry's filename is equal to the filename we are searching
            if entry == filename:
                # APPEND to our report the entry's path
                report.append(entryPath)
                # Since there is no guarantee that the following entries will be files and not dirs, we can not break here.
                # The folling entry might be a dir, and we have to call our recursive find for that dir later
                
    #Return our report as we finish our recursive call
    return report

#""" Driver Code
if __name__ == "__main__":
    # check current working directory
    os.getcwd()
    # possibly have to change current working directory
    # cwdPath = ""
    # os. chdir(cwdPath)
    report = find("testFindFilename-r", "Empty File")
    print(report)
#"""