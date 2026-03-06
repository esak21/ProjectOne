from OneWithDesignpatterns.Lesson_003_StateDesignPattern.ecommerce_site import DoorDashPackage
from appEvents import packageEvent

def main():
    pass




if __name__ == "__main__":
    order = DoorDashPackage("order-001-Az")
    event = packageEvent()
    failure_event = packageEvent(event_type="DELIVERY_FAILED")
    order.next_process(event)
    print("Customer Pays the Amount ")
    order.next_process(event)
    order.next_process(event)
    order.cancel_package()

    order.next_process(event)

    order.next_process(failure_event)



    order.next_process(failure_event)

    order.next_process(failure_event)

