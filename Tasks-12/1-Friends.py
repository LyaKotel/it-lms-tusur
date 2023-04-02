class Friends:
    #Конструктор
    def __init__(self, connections):
        self.connections = connections
        print('Сработал Friends конструктор')
    #Показать связи
    def show(self):
        print('Connections list:')
        for k, i in enumerate(self.connections):
            print(k+1, i, sep=': ')
    #Добавить новую связь
    def add(self, connection):
        if (connection in self.connections):
            print('Add false...')
            return False
        else:
            print('Add true!')
            self.connections.append(connection)
            return True
    #Убрать связь
    def remove(self, connection):
        if (connection in self.connections):
            print('Remove true!')
            self.connections.remove(connection)
            return True
        else:
            print('Remove false...')
            return False
    #Показать имена со связями
    def names(self):
        print('These names have connections:')
        names = set()
        for k in self.connections:
            for i in k:
                if(i not in names): names.add(i)
        print(names)
        return names
    #Показать всех связанных с определенным именем
    def connected(self, name):
        print('This name have these friends:')
        friends = set()
        for k in self.connections:
            if(name in k):
                for i in k:
                    if(i != name): friends.add(i)
        print(friends)
        return friends


f = Friends([ {'Oleg','Nikola'}, {'Tanya','Ivan'}, {'Liza','Masha'}, {'Liza','Ivan'}, {'Tanya','Masha'} ])
f.add( {'Albert','Zigmund'} )
f.show()
f.remove( {'Nikola','Oleg'} )
f.show()
f.names()
f.connected('Liza')