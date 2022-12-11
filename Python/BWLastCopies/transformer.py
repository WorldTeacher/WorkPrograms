
class IssueData:
    def __init__(self, issue, count, libraries):
        self.issue = issue
        self.count = count
        self.libraries = libraries
        
    def get_issue(self):
        return self.issue
    
    def get_count(self):
        return self.count
    
    def get_libraries(self):
        return self.libraries

class CreateNotification:
    def __init__(self) -> None:
        """
        _summary_
        """
        pass

    def create_notification(self, message: list, iterate: bool = False) -> str:
        """
        Create a notification based on a list

        It is hard-coded to work with the BWLastCopies project.

        Args:
            message (list): A list with relevant data for each issue.

        Returns:
            notification : the notification to be sent.
        """
        notification_length = len(message)
        issues = []
        counts = []
        libraries = []
        for i in range(notification_length):
            issues.append(message[i]['issue'])
            counts.append(message[i]['count'])
            libraries.append(message[i]['libraries'])
        notilist = []
        spaces = "       "  # a string of spaces to align the notification
        for issue, count, library in zip(issues, counts, libraries):
            library_string = ", ".join(library)
            # library_string=library_string.replace(",",", ")
            template = f'{issue}: {count} | Bibliotheken: {library_string} \n'
            notilist.append(template)
        print(notilist)
        notification = ''.join(notilist)
        # print(notification)
        return notification

    def adress_notification(self, adress: dict) -> str:
        """
        Take a dictionary with the adress data and return a string with the adress.



        Args:
            - adress (dict): The adress data.

        Returns:
            - adress_str (str): The adress as a string.
        """
        # check lenght of adress
        street = adress[0]
        city = adress[1]
        zip = adress[2]
        state = adress[3]
        adress_notification = f'{street}\n{zip} {city}\n{state}'
        return adress_notification
    def create_notification_iterated(self,notification)->str:
        notification_iterated=[]
        #enumerate over the list
        for index,i in enumerate(notification):
            curr_dict=notification[index]
            if index+1>:
                next_dict=notification[index+1]
            else:
                next_dict=notification[index]
            if curr_dict['issue']==next_dict['issue']:
                print(curr_dict['issue'],next_dict['issue'])
                
        # for i,index in enumerate(notification):
            
                
        return notification_iterated

if __name__ == '__main__':
    currlist=[{'issue': '16., aktualisierte und überarbeitete Auflage', 'count': 17, 'libraries': ['DE-Fn1', 'DE-Shm2', 'DE-104', 'DE-Ki95', 'DE-93', 'DE-Ofb1', 'DE-Kon4', 'DE-Ilm1', 'DE-944', 'DE-18', 'DE-Hed2', 'DE-Wim2', 'DE-89', 'DE-Brg3', 'DE-289', 'DE-31', 'DE-Mit1']}, {'issue': '16., aktualisierte und überarbeitete Auflage', 'count': 57, 'libraries': ['DE-839', 'DE-840', 'DE-Mh35', 'DE-Stg258', 'DE-916', 'DE-Ga20', 'DE-197', 'DE-Rav1', 'DE-Bn3', 'DE-520', 'DE-953', 'DE-960', 'DE-56', 'DE-Ilm1', 'DE-944', 'DE-Hed2', 'DE-Fn1-VS', 'DE-551', 'DE-90', 'DE-Wis1', 'DE-Zi4', 'DE-27', 'DE-1041', 'DE-L229', 'DE-Rt2', 'DE-1845', 'DE-18-302', 'DE-958', 'DE-840-3', 'DE-1926', 'DE-21', 'DE-Fn1-TUT', 'DE-46', 'DE-478', 'DE-Rav1-a', 'DE-841', 'DE-L189', 'DE-16', 'DE-31', 'DE-517']}, {'issue': '15., aktualisierte und überarbeitete Auflage', 'count': 5, 'libraries': ['DE-839', 'DE-897', 'DE-897-1', 'DE-Wim2', 'DE-L189']}, {'issue': '15., aktualisierte und überarbeitete Auflage', 'count': 11, 'libraries': ['DE-1033', 'DE-Fn1', 'DE-839', 'DE-897', 'DE-Fl3', 'DE-916', 'DE-Kon4', 'DE-897-1', 'DE-84', 'DE-289', 'DE-31']}, {'issue': '15., aktualisierte und überarbeitete Auflage', 'count': 73, 'libraries': ['DE-991a', 'DE-840', 'DE-Mh35', 'DE-916', 'DE-18', 'DE-Wim2', 'DE-Sra5', 'DE-84', 'DE-197', 'DE-Rav1', 'DE-Sa16', 'DE-Fn1', 'DE-1033', 'DE-520', 'DE-953', 'DE-960', 'DE-56', 'DE-Ilm1', 'DE-115', 'DE-944', 'DE-Fn1-VS', 'DE-90', 'DE-Kt1', 'DE-93', 'DE-27', 'DE-14', 'DE-Frei129', 'DE-Shm2', 'DE-Kon4', 'DE-Rt2', 'DE-18-302', 'DE-958', 'DE-840-3', 'DE-715', 'DE-21', 'DE-988', 'DE-959', 'DE-546', 'DE-46', 'DE-28', 'DE-L189', 'DE-89', 'DE-943', 'DE-31', 'DE-Stg259']}, {'issue': '14., aktualisierte und überarbeitete Auflage', 'count': 1, 'libraries': ['DE-18']}, {'issue': '14., aktualisierte und überarbeitete Auflage', 'count': 70, 'libraries': ['DE-24', 'DE-Mh35', 'DE-916', 'DE-Wim2', 'DE-Sa16', 'DE-Fn1', 'DE-1033', 'DE-104', 'DE-520', 'DE-953', 'DE-Meg1', 'DE-Ilm1', 'DE-Hed2', 'DE-941', 'DE-8', 'DE-45', 'DE-Fn1-VS', 'DE-Vil2', 'DE-551', 'DE-90', 'DE-93', 'DE-972', 'DE-27', 'DE-14', 'DE-Shm2', 'DE-Kon4', 'DE-Rt2', 'DE-18-302', 'DE-958', 'DE-1926', 'DE-Mh39', 'DE-715', 'DE-988', 'DE-959', 'DE-46', 'DE-841', 'DE-L189', 'DE-16', 'DE-943', 'DE-31', 'DE-Stg259']}, {'issue': '13., aktualisierte und überarbeitete Auflage', 'count': 1, 'libraries': ['DE-18']}, {'issue': '13., aktualisierte und überarbeitete Auflage', 'count': 93, 'libraries': ['DE-Luen4', 'DE-839', 'DE-Mh35', 'DE-100', 'DE-916', 'DE-Ga20', 'DE-Sra5', 'DE-84', 'DE-B69', 'DE-Sa16', 'DE-Fn1', 'DE-1033', 'DE-104', 'DE-897', 'DE-755', 'DE-700', 'DE-953', 'DE-Ilm1', 'DE-7', 'DE-960-3', 'DE-8', 'DE-15', 'DE-Fn1-VS', 'DE-Hed2', 'DE-Zi4', 'DE-93', 'DE-972', 'DE-27', 'DE-14', 'DE-Shm2', 'DE-L229', 'DE-Rt2', 'DE-18-302', 'DE-1926', 'DE-542', 'DE-Loer2', 'DE-46', 'DE-21-119', 'DE-352', 'DE-28', 'DE-Rav1-a', 'DE-L189', 'DE-89', 'DE-16', 'DE-943', 'DE-31', 'DE-Stg259', 'DE-517']}, {'issue': '12., aktual. u. überarb. Aufl.', 'count': 6, 'libraries': ['DE-1033', 'DE-Ofb1', 'DE-L189', 'DE-180', 'DE-Mh39']}, {'issue': '12., aktualisierte und überarbeitete Auflage 2016, 1., korrigierter Nachdruck 2017', 'count': 3, 'libraries': ['DE-15', 'DE-289', 'DE-93']}, {'issue': '12., aktualisierte und überarbeitete Auflage', 'count': 2, 'libraries': ['DE-18', 'DE-89']}, {'issue': '12., aktualisierte und überarbeitete Auflage', 'count': 65, 'libraries': ['DE-840', 'DE-Mh35', 'DE-Stg258', 'DE-3', 'DE-916', 'DE-Ma9', 'DE-Sra5', 'DE-1033', 'DE-Fn1', 'DE-Bn3', 'DE-953', 'DE-59', 'DE-960', 'DE-Ilm1', 'DE-15', 'DE-93', 'DE-972', 'DE-27', 'DE-14', 'DE-Va1', 'DE-Shm2', 'DE-L229', 'DE-Rt2', 'DE-18-302', 'DE-180', 'DE-840-3', 'DE-Ofb1', 'DE-46', 'DE-28', 'DE-841', 'DE-L189', 'DE-89', 'DE-16', 'DE-943', 'DE-31', 'DE-Stg259', 'DE-517']}, {'issue': '11., aktualisierte und überarb. Aufl.', 'count': 71, 'libraries': ['DE-991a', 'DE-Luen4', 'DE-839', 'DE-24', 'DE-Mh35', 'DE-3', 'DE-916', 'DE-18', 'DE-105', 'DE-Sa16', 'DE-Fn1', 'DE-Fl3', 'DE-953', 'DE-J59', 'DE-960', 'DE-Ilm1', 'DE-7', 'DE-Hed2', 'DE-8', 'DE-45', 'DE-Zi4', 'DE-Wis1', 'DE-27', 'DE-14', 'DE-Shm2', 'DE-25', 'DE-Zwi2', 'DE-180', 'DE-1926', 'DE-715', 'DE-1871', 'DE-Fn1-TUT', 'DE-959', 'DE-Stg259', 'DE-Ofb1', 'DE-963', 'DE-830', 'DE-352', 'DE-841', 'DE-D161', 'DE-L189', 'DE-16', 'DE-943', 'DE-31', 'DE-9']}, {'issue': '10., aktualisierte und überarb. Aufl., 1. Nachdr', 'count': 27, 'libraries': ['DE-840', 'DE-Mh35', 'DE-Sra5', 'DE-951', 'DE-21-24', 'DE-1033', 'DE-Fn1', 'DE-953', 'DE-Hed2', 'DE-15', 'DE-15-292', 'DE-14', 'DE-Zwi2', 'DE-18-302', 'DE-Lg1', 'DE-Ch1', 'DE-180', 'DE-289', 'DE-1871', 'DE-Fn1-TUT', 'DE-Ofb1', 'DE-Loer2', 'DE-1834s', 'DE-352', 'DE-31']}, {'issue': '10., aktualisierte und überarb. Aufl.', 'count': 26, 'libraries': ['DE-715', 'DE-23', 'DE-840', 'DE-J59', 'DE-700', 'DE-46', 'DE-18', 'DE-8', 'DE-352', 'DE-15', 'DE-Lg1', 'DE-89', 'DE-Ch1', 'DE-180', 'DE-31', 'DE-289', 'DE-14']}, {'issue': '10. aktualisierte und überarb. Aufl.', 'count': 37, 'libraries': ['DE-23', 'DE-916', 'DE-18', 'DE-Sra5', 'DE-Fl3', 'DE-104', 'DE-J59', 'DE-700', 'DE-755', 'DE-564', 'DE-Ilm1', 'DE-Hil2', 'DE-8', 'DE-Shm2', 'DE-18-302', 'DE-715', 'DE-959', 'DE-46', 'DE-Ei6', 'DE-89']}, {'issue': '9., aktualisierte und überarbeitete Auflage', 'count': 1, 'libraries': ['DE-Ilm1']}, {'issue': '9., aktualisierte Aufl., 1., korrigierter Nachdr', 'count': 11, 'libraries': ['DE-Bn3', 'DE-953', 'DE-Ofb1', 'DE-Loer2', 'DE-Hed2', 'DE-841', 'DE-Zwi2', 'DE-951', 'DE-31', 'DE-93-131']}, {'issue': '[9., aktualisierte und überarb. Aufl.]', 'count': 8, 'libraries': ['DE-Ofb1', 'DE-18', 'DE-84', 'DE-951', 'DE-31', 'DE-14', 'DE-93-131']}, {'issue': '9., aktualisierte [und überarb.] Aufl., 1., korr. Nachdr.', 'count': 15, 'libraries': ['DE-Ka88', 'DE-104', 'DE-1871', 'DE-960', 'DE-Hil2', 'DE-18', 'DE-28', 'DE-84', 'DE-14']}, {'issue': '9., aktualisierte und überarb. Aufl.', 'count': 2, 'libraries': ['DE-705', 'DE-46']}, {'issue': '[8., aktualisierte Aufl.2009; 2. Nachdruck]', 'count': 2, 'libraries': ['DE-15', 'DE-14']}, {'issue': '8., aktualis. Aufl.2009; 2. Nachdruck', 'count': 6, 'libraries': ['DE-991a', 'DE-Sg2', 'DE-953', 'DE-1871', 'DE-15', 'DE-14']}, {'issue': '[8., aktualisierte Aufl.]', 'count': 20, 'libraries': ['DE-Sa16', 'DE-Shm2', 'DE-520', 'DE-834', 'DE-J59', 'DE-24', 'DE-Mh39', 'DE-46', 'DE-18', 'DE-8', 'DE-28', 'DE-45', 'DE-B108', 'DE-291-407', 'DE-89', 'DE-31', 'DE-14', 'DE-Sa16-1']}, {'issue': '8., aktualisierte Aufl., 1. Nachdr.', 'count': 21, 'libraries': ['DE-24', 'DE-Bn3', 'DE-520', 'DE-953', 'DE-15', 'DE-45', 'DE-291-407', 'DE-972', 'DE-14', 'DE-Sa16-1', 'DE-Ch1', 'DE-16-121', 'DE-289', 'DE-Mh39', 'DE-46', 'DE-753', 'DE-28', 'DE-943', 'DE-31', 'DE-16-300']}, {'issue': '8., aktualisierte Aufl.', 'count': 14, 'libraries': ['DE-Shm2', 'DE-104', 'DE-579', 'DE-J59', 'DE-959', 'DE-Ilm1', 'DE-B108', 'DE-8', 'DE-89']}, {'issue': '7., aktualisierte und erw. Aufl., 1. Nachdr.', 'count': 26, 'libraries': ['DE-991a', 'DE-24', 'DE-93-36', 'DE-Bs68', 'DE-105', 'DE-Fn1', 'DE-104', 'DE-Ki95', 'DE-960', 'DE-Hil2', 'DE-Ilm1', 'DE-944', 'DE-14', 'DE-25', 'DE-93-208', 'DE-291-114', 'DE-841', 'DE-943', 'DE-31']}, {'issue': '7., aktual. und erw. Aufl.', 'count': 14, 'libraries': ['DE-Luen4', 'DE-1158', 'DE-755', 'DE-46', 'DE-Hil2', 'DE-616', 'DE-18', 'DE-1373', 'DE-89', 'DE-Sra5', 'DE-27']}, {'issue': '6., aktualisierte und erw. Aufl., 1., korrigierter Nachdr.', 'count': 22, 'libraries': ['DE-991a', 'DE-Luen4', 'DE-291-417', 'DE-105', 'DE-84', 'DE-Ilm1', 'DE-15', 'DE-8', 'DE-206', 'DE-291-407', 'DE-90', 'DE-972', 'DE-14', 'DE-897-1', 'DE-352', 'DE-90-148', 'DE-89', 'DE-31', 'DE-16-7']}, {'issue': '6., aktualisierte und erw. Aufl., 1. korrigierter Nachdr.', 'count': 29, 'libraries': ['DE-Luen4', 'DE-104', 'DE-897', 'DE-Hil2', 'DE-18', 'DE-830', 'DE-28', 'DE-8', 'DE-89', 'DE-551', 'DE-9']}, {'issue': '5., aktualisierte und erw. Aufl., 1. Nachdr', 'count': 15, 'libraries': ['DE-Fl3', 'DE-93-157', 'DE-25', 'DE-Hil2', 'DE-21-119', 'DE-15', 'DE-8', 'DE-89', 'DE-B19', 'DE-180', 'DE-31', 'DE-289']}, {'issue': '5., aktualisierte und erw. Aufl.', 'count': 72, 'libraries': ['DE-527', 'DE-715', 'DE-18-301', 'DE-959', 'DE-46', 'DE-Ilm1', 'DE-45', 'DE-Wim2', 'DE-89', 'DE-84']}, {'issue': '4. Aufl. zum Tiger-Release., 1 Nachdr', 'count': 3, 'libraries': ['DE-15', 'DE-747', 'DE-31']}, {'issue': '4. Aufl. zum Tiger-Release', 'count': 17, 'libraries': ['DE-Shm2', 'DE-46', 'DE-Ilm1', 'DE-18', 'DE-830', 'DE-45', 'DE-841', 'DE-89', 'DE-84', 'DE-547', 'DE-Sra5', 'DE-517']}, {'issue': '3. Aufl., [Online-Ausg.]', 'count': 2, 'libraries': ['DE-180']}, {'issue': '3. aktual. u. erw. Aufl', 'count': 22, 'libraries': ['DE-180', 'DE-Shm2', 'DE-Kt1', 'DE-Gat1', 'DE-Ilm1', 'DE-18', 'DE-15', 'DE-841', 'DE-89', 'DE-84', 'DE-Sra5', 'DE-517']}, {'issue': '2. Aufl.', 'count': 10, 'libraries': ['DE-951', 'DE-Ilm1', 'DE-15', 'DE-8', 'DE-747', 'DE-941', 'DE-180', 'DE-1817']}, {'issue': '1. Aufl.', 'count': 11, 'libraries': ['DE-705', 'DE-Shm2', 'DE-J59', 'DE-3', 'DE-Ilm1', 'DE-18', 'DE-830', 'DE-89', 'DE-84', 'DE-9']}]
    transf=CreateNotification()
    formated= transf.create_notification(currlist)
    print("------------------")
    print(formated)
    print("------------------")
    iterated=transf.create_notification_iterated(currlist)
    print(iterated)
    iter_noti=transf.create_notification(iterated)
    print("#------------------#")
    print(iter_noti)
    print("#------------------#")