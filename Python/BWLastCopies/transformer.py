


class CreateNotification:
    

    def create_notification(message:list)->str:
        """
        Create a notification based on a list

        It is hard-coded to work with the BWLastCopies project.

        Args:
            message (list): A list with relevant data for each issue.

        Returns:
            notification : _description_
        """
        notification_length=len(message)
        issues=[]
        counts=[]
        libraries=[]
        for i in range(notification_length):
            issues.append(message[i]['issue'])
            counts.append(message[i]['count'])
            libraries.append(message[i]['libraries'])
        notilist=[]
        spaces="       "
        for issue, count, library in zip(issues,counts,libraries):
            library_string=", ".join(library)
            # library_string=library_string.replace(",",", ")
            template=f'{issue}: {count} | Bibliotheken: {library_string} \n'
            notilist.append(template)
        notification=''.join(notilist)
        #print(notification)
        return notification
   


if __name__ == '__main__':
    a = CreateNorification().create_notification([{'issue': '1', 'count': 1, 'libraries': ['Bibliothek 1', 'Bibliothek 2']}, {'issue': '2', 'count': 1, 'libraries': ['Bibliothek 1', 'Bibliothek 2']}])
    print(a)