import logging
from flask.ext.appbuilder.basemanager import BaseManager
from .views import ContactModelView


log = logging.getLogger(__name__)

"""
   Create your plugin manager, extend from BaseManager.
   This will let you create your models and register your views
   
   ex::

       class MyAddOnManager(BaseManager):


"""


class MyAddOnManager(BaseManager):

    contact_view = ContactModelView

    def __init__(self, appbuilder):
        """
             Use the constructor to setup any config keys specific for your app. 
        """
        app.config.setdefault('MYADDON_KEY', 'SOME VALUE')

    def register_views(self):
        """
            This method is called by AppBuilder when initializing, use it to add you views
        """
        self.contact_view = self.appbuilder.add_view(self.contact_view, "List Contacts",
                                                  icon="fa-user", label=_("List Contacts"),
                                                  category="Contacts", category_icon="fa-user",
                                                  category_label=_('Contacts'))

    def pre_process(self):
        fill_gender()

    def fill_gender():
        try:
            self.appbuilder.get_session.add(Gender(name='Male'))
            self.appbuilder.get_session.add(Gender(name='Female'))
            self.appbuilder.get_session.commit()
        except:
            self.appbuilder.get_session.rollback()


    def post_process(self):
        pass

