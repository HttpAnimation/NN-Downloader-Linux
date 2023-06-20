import shutil
import os

# Remove directories
shutil.rmtree('./dist', ignore_errors=True)
shutil.rmtree('./build', ignore_errors=True)
shutil.rmtree('./__pycache__', ignore_errors=True)

# Delete file
os.remove('./NN-Downloader.spec')
