import os


# connect to remote machine
def ensure_dir(file_path):
    """
    Directory - ensure that directory if it exists
    """
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

# disconnect from a remote machine
