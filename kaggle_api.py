# run my imports
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

# Set Kaggle creds
os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

# download the dataset from kaggle