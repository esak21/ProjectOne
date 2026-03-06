from abc import ABC
from appEvents import packageEvent

class State(ABC):

    @property
    def context(self):
        return self._context


    # we are storing the ContextClass Variable Here
    @context.setter
    def context(self, context):
        self._context = context


    def next_process(self, event: packageEvent):
        raise NotImplementedError

    def cancel_package(self):
        raise NotImplementedError




class NewState(State):

    def next_process(self, event: packageEvent):
        print("Package is in New State")
        # we are calling the ContextClass method Here
        self.context.transition_to(PaymentProcessingState())

    def cancel_package(self):
        print("🛑 Cancellation successful. Refund initiated.")
        self.context.transition_to(CancelledState())



class  PaymentProcessingState(State):
    def next_process(self, event: packageEvent):
        print("Payment is in Processing State")
        print("Payment completed")
        self.context.transition_to(OrderedState())

    def cancel_package(self):
        print("🛑 Cancellation successful. Refund initiated.")
        self.context.transition_to(CancelledState())

class OrderedState(State):
    def next_process(self, event: packageEvent):
        print("Package is in Ordered State")
        self.context.transition_to(ShipmentState())

    def cancel_package(self):
        print("🛑 Cancellation successful. Refund initiated.")
        self.context.transition_to(CancelledState())

class ShipmentState(State):
    def next_process(self, event: packageEvent):

        print("Package is in Delivered State")
        self.context.transition_to(DeliveredState())

    def cancel_package(self):
        print("Shipment State ❌❌❌ Too late to cancel manually!")
        self.context.transition_to(CancelledState())

class DeliveredState(State):
    def next_process(self, event: packageEvent):
        if event.event_type == "DELIVERY_FAILED":
            print("🚚 package has Lost. Package delivered Failed!")
            self.context.transition_to(TicketState())
        else:
            print("🚚 Driver has arrived. Package delivered!")

    def cancel_package(self):
        print("DeliveredState ❌❌❌ Too late to cancel manually!")
        self.context.transition_to(CancelledState())

class CancelledState(State):
    def next_process(self,event: packageEvent):
        print("Package is in Cancelled State")
        self.context.transition_to(CancelledState())

    def cancel_package(self):
        print("❌ Too late to cancel manually!")



class TicketState(State):
    def next_process(self,event: packageEvent):
        print("🔍 Support is investigating. Cannot move to next step yet.")

    def cancel_package(self):
        print("❌ Too late to cancel manually!")