from  dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class pipelineStatus:
    status: str
    message: str
    pipeline_name: str


class NotificationService(ABC):
    @abstractmethod
    def update(self, pipeline_metadata: pipelineStatus):
        pass

class EmailNotification(NotificationService):
    def update(self, pipeline_metadata: pipelineStatus):
        print(f"Email Notification Sent for the pipeline {pipeline_metadata.pipeline_name}")



class SMSNotifiaction(NotificationService):
    def update(self, pipeline_metadata: pipelineStatus):
        print(f"SMS Notification Sent {pipeline_metadata.pipeline_name}")


class SlackNotification(EmailNotification):
    def update(self, pipeline_metadata: pipelineStatus):
        print(f"Slack Notification Sent {pipeline_metadata.pipeline_name}")
        print(f"Slack Message {pipeline_metadata}")



class Observer():

    def __init__(self):
        self.subscribers = []

    def add_subscribers(self, notification_service: NotificationService):
        self.subscribers.append(notification_service)

    def remove_subscribers(self, notification_service: NotificationService):
        self.subscribers.remove(notification_service)

    def notify_subscribers(self, pipeline_metadata: pipelineStatus):
        for subscriber in self.subscribers:
            subscriber.update(pipeline_metadata)


    def pipeline_tasks(self):
        try:
            pipeline_metadata = pipelineStatus(status="success", message="Pipeline completed successfully", pipeline_name="Test Pipeline")
            print(f"Pipeline  Tasks are running")
            # TO Simulate the Failure
            #results = 1/ 0
            print("Pipeline tasks completed")
            self.notify_subscribers(pipeline_metadata)
        except :
            pipeline_metadata = pipelineStatus(status="Failed", message="Pipeline completed successfully", pipeline_name="Test Pipeline")
            print(f"Pipeline  Tasks are failed")
            self.notify_subscribers(pipeline_metadata)
