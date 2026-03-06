from optparse import Option
from appEvents import packageEvent
from ecommerce_state import NewState




class DoorDashPackage:

    def __init__(self, package_id: str):
        self.package_id = package_id
        self.transition_to(NewState())

    def transition_to(self, app_state):
        # we are storing the new State in the _state variable
        self._state = app_state
        print(f"Package transitioned to {app_state} state with {type(app_state).__name__}")
        # we are calling the State class Context property method Here and assign it to the current object ( DoorDashPackage)
        # so we can access the context from the State class
        self._state.context = self


    def next_process(self, event: packageEvent):
        self._state.next_process(event)

    def cancel_package(self):
        self._state.cancel_package()





