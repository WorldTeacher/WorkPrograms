from PyQt6 import QtWidgets, uic

class Settings(QtWidgets.QMainWindow):
    def __init__(self):
        super(Settings, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('settings.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.save_button=self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Save)
        self.cancel_button=self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel)

        self.save_button.clicked.connect(self.save_settings)
        self.cancel_button.clicked.connect(self.cancel_settings)
    
    def save_settings(self):
        #save settings
        print("save")

    def cancel_settings(self):
        #cancel settings
        print("cancel")