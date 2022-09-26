from abc import ABC, abstractmethod


class Task(object, ABC):

    @abstractmethod
    def __init__(self):
        self.Session = db.scoped_session(db.sessionmaker(bind=db.engine))

    def run(self, task_runner, message_payload):
        pass

    def get_task_string(self):
        raise NotImplementedError('Missing get_task_string method.')

