from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def notification(self):
        pass

class NewsNotify(Observer):

    def notification(self):
        print('New update has been published')


class News:

    def __init__(self,Title,Author,Text):
        self.Title = Title
        self.Author = Author
        self.Text = Text

    def display(self):
        print('Title: ',self.Title)
        print('Author: ',self.Author)
        print('Text: ',self.Text)


class NewsStation:
    def __init__(self):
        self.observers: list[Observer] = []
    
    def Subscribe(self,observer :Observer):
        self.observers.append(observer)
    
    def UnSubscribe(self,observer :Observer):
        self.observers.remove(observer)
    
    def notify_subscribers(self,news : News):
        for subscriber in self.observers:
            subscriber.notification()
            news.display()


def main():

    station = NewsStation()

    user1 = NewsNotify()
    user2 = NewsNotify()

    station.Subscribe(user1)
    station.Subscribe(user2)

    news = News(
        "TechPrysm Launches AI Platform",
        "Ikhlas Ahmad",
        "TechPrysm has officially launched its AI-powered learning platform."
    )

    station.notify_subscribers(news)


if __name__ == "__main__":
    main()