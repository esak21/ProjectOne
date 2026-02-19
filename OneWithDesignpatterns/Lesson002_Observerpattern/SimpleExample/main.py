from utils import Observer, EmailNotification, SMSNotifiaction, SlackNotification, pipelineStatus


def main():
    email_subscription = EmailNotification()
    slack_subscription = SlackNotification()
    sms_subscription = SMSNotifiaction()


    observer = Observer()
    observer.add_subscribers(email_subscription)
    observer.add_subscribers(slack_subscription)
    observer.add_subscribers(sms_subscription)


    observer.pipeline_tasks()



if __name__ == "__main__":
    main()

