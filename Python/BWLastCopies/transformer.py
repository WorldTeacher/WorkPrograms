

class CreateNotification:
    def __init__(self) -> None:
        """
        _summary_
        """
        pass

    def create_notification(self, message: list) -> str:
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


if __name__ == '__main__':
    # liste = [{'issue': '1', 'count': 1,
    #           'libraries': ['Bibliothek 1', 'Bibliothek 2']},
    #          {'issue': '2', 'count': 1,
    #           'libraries': ['Bibliothek 1', 'Bibliothek 2']}]
    # print(liste)

    # a = CreateNotification().create_notification(liste)
    # print(a)
    import os
    #print 