# observer.

class Sub:
    def react(self, creator):
        print("Sub реагирует лайком на новое видео от: ")
        print(creator)
        
class Creator:
    
    def __init__(self, name):
        self.subs = []
        self.name = name  # сохранять в.
    def __str__(self):
        return f"{self.name}"
    def follow(self, sub):
        self.subs.append(sub)
        print("подписчик успешно подписался.")
    def notify_all(self):
        for sub in self.subs:
            sub.react(self)
    def create_event(self):
        print("произошло новое видео.")
        self.notify_all()


chan_owner = Creator("MGH Channel")
chan_owner.subs
[]
chan_owner.name
'MGH Channel'
sub1 = Sub()
chan_owner.follow(sub1)
подписчик успешно подписался.
sub2 = Sub()
sub3 = Sub()
chan_owner.follow(sub2)
подписчик успешно подписался.
chan_owner.subs
[<__main__.Sub object at 0x000001EC8903B340>, <__main__.Sub object at 0x000001EC8903B7F0>]
chan_owner.create_event()
произошло новое видео.
Sub реагирует лайком на новое видео от: 
MGH Channel
Sub реагирует лайком на новое видео от: 
MGH Channel
