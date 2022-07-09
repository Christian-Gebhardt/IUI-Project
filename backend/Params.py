"""
Static constants for the project
"""

import os

RUNNING_IN_CLOUD=os.environ.get("RUNNING_IN_CLOUD")

# Youtube
YT_API_KEY=os.environ.get("YT_API_KEY")
YT_REGION='DE'

# Database
DB_SERVER = os.getenv('MONGO_URI')
DB_LIMIT=100

# ML
PATH_TO_STATIC_MODEL=os.environ.get("PATH_TO_STATIC_MODEL")
PATH_TO_DYNAMIC_MODEL=os.environ.get("PATH_TO_DYNAMIC_MODEL")
NUM_OF_TRAINING_SAMPLES=50
NUM_OF_FEEDBACKS_UNTIL_RETRAIN=3