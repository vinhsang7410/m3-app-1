from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
anvil.server.connect()

class Form1(Form1Template):
  
  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def btnSort_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.txtNumbers_QS.text = anvil.server.call(quicksort_string, self.txtnumber)
    pass

  def btnSort_show(self, **event_args):
    """This method is called when the Button is shown on the screen"""
    pass
    
  

  