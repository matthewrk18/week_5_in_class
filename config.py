import os

basedir = os.path.abspath(os.path.dirname(__file__))



# gives flask access to relative filepathregardless of OS.
# alllows outside files/folders to be imported as well
# can consider this a 'roadmap' we're giving flask for our operating system

class Config:
    """
    Sets configuration variables for our Flask app here
    Eventually will use hidden variable items - but for now, we'll leave them exposed in config
    """
    SECRET_KEY = "You will never guess..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Decreases unnecessary output in terminal