import logging
from flask_appbuilder.basemanager import BaseManager
from flask_babel import lazy_gettext as _


log = logging.getLogger(__name__)

"""
   Create your plugin manager, extend from BaseManager.
   This will let you create your models and register your views
   
"""


class MyAddOnManager(BaseManager):


    def __init__(self, appbuilder):
        """
             Use the constructor to setup any config keys specific for your app. 
        """
        super(MyAddOnManager, self).__init__(appbuilder)
        self.appbuilder.get_app.config.setdefault('MYADDON_KEY', 'SOME VALUE')

    def register_views(self):
        """
            This method is called by AppBuilder when initializing, use it to add you views
        """
        pass

    def pre_process(self):
        pass

    def post_process(self):
        pass

