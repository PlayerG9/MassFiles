from imports import *


class EventHandlerClass:
    def __init__(self):
        self.events: Dict[str, List[callable]] = {}

    def register(self, event: str, callback: callable) -> None:
        self.events.setdefault(event, [])
        self.events[event].append(callback)

    def unregister(self, event: str, callback: callable):
        if event not in self.events: return
        self.events[event].remove(callback)

    def invoke(self, event: AnyStr) -> None:
        if event not in self.events: return
        for callback in self.events[event]:
            callback()


EventHandler = EventHandlerClass()
