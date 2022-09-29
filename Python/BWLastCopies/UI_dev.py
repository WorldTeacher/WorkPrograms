from PyQt6 import QtWidgets, uic
import sys, manualsearch, urlsearch, os, json, atexit, search_db


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('Universal_UI.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.check_bwlastcopies_manual.clicked.connect(self.is_pressed)
        self.actionbearbeiten.triggered.connect(self.edit_config)
        self.search_isil.clicked.connect(self.get_data)

    
    def is_pressed(self):
        #check if button self.do_run_bwlastcopies_manual is pressed
        
        author,title,issue=self.get_input()
        
        #result = urlsearch.manualsearch(author,title,pass_issue="3")
        result=manualsearch.search(author,title,issue)
        title=result['title']
        our_issues=result['our_issues']
        our_signature=result['signature']
        our_count=result['our_count']
        all_issues=result['issue_count']

        all_count=result['all_count']
        ppn=result['ppn']
        series=result['series']
        if author=="0": author="ohne Angabe"
        notification_1=f'Die Suche nach Titel:  {title}, Autor: {author} ergab folgendes Ergebnis:'
        notification_manual=f'Lokal: Auflage(n): {our_issues}, Signatur(en): {our_signature}, PPN: {ppn}, Serie: {series}'
        notification_3=f'Gesamt: Anzahl: {all_count}, Auflage(n):\n{all_issues}'
        #print(f'{notification_1}\n{notification_manual}\n{notification_3}')
        # self.result_bwl_manual.setPlainText(f' {notification_1}\n\n{notification_manual}\n\n{notification_3}')
        self.result_bwl_manual.setText(f' {notification_1}\n\n{notification_manual}\n\n{notification_3}')
        
        #display result in loginfo_bwl_manual

    def edit_config(self):
        #start settings.py
        os.system('python settings.py')

    def get_data(self):
        #check if self.isil_input is empty
        isil=self.isil_input.text()
        print(isil)
        try:
            data=search_db.search_database(isil)
            print(data)
            self.organame_line.setText(data['name'])
            self.telnr.setText(data['phone'])
            self.mailto.setText(data['mail'])
            adress_notification=self.adress_notification(data['adress'])
            print(adress_notification)
            self.isil_link_out.setText(data['isil_link'])
            self.adress_out.setText(adress_notification)
        except Exception as e:
            print(e)
            self.isil_input.setText('Fehler')
    def adress_notification(self,adress):
        #check lenght of adress
        street=adress[0]
        city=adress[1]
        zip=adress[2]
        state=adress[3]
        adress_notification=f'{street}\n{zip} {city}\n{state}'
        return adress_notification
    def get_input(self):
        author=self.author_input.text()
        title=self.title_input.text()
        issue=self.pass_issue_input.text()
        #print(f'author: {author}, title: {title}')
        return author,title,issue  

    def get_data_from_settings(self):
        #try to load settings from gui_settings.json, if it is not available, load from settings.json and create gui_settings.json on exit
        try:
            if os.path.isfile('gui-settings.json'):
                with open('gui-settings.json') as f:
                    data = json.load(f)
                self.bib_id_input.setText(data['Bibliotheks-ID'])
                self.sigi_input.setText(data['Sigel'])
                self.ReiheA_BWL.setCurrentIndex(data['Index_ReiheA_BWL'])
                self.tabwidget_auto_manual.setCurrentIndex(data['Index_Automatic_Manual'])
                #self.bib_id_input.setPlainText(data['bibid'])
                #self.sigi_input.setPlainText(data['sigel'])
        except FileNotFoundError:
            print('gui-settings.json does not exist, loading from settings.json')
            try:
                with open('gui-settings.json') as f:
                    data = json.load(f)
                self.bib_id_input.setText(data['Bibliotheks-ID'])
                self.sigi_input.setText(data['Sigel'])
            except FileNotFoundError:
                print('settings.json does not exist, creating new file')
                self.bib_id_input.setText('Bibliotheks-ID')
                self.sigi_input.setText('Sigel')

    def save_data_to_settings(self):
        #save data to settings.json
        bibid=self.bib_id_input.text()
        sigel=self.sigi_input.text()
        tab_bwl_man_auto=self.tabwidget_auto_manual.currentIndex()
        tab_ra_bwlastcopies=self.ReiheA_BWL.currentIndex()
        data = {
            "Bibliotheks-ID": bibid,
            "Sigel": sigel,
            "Index_Automatic_Manual": tab_bwl_man_auto,
            "Index_ReiheA_BWL":tab_ra_bwlastcopies,
            "tbd":0
            }

        with open('gui-settings.json', 'w') as f:
            json.dump(data, f, indent=4)
            print(data)
    
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec())
