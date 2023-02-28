from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionMathOperation(Action):
    def name(self) -> Text:
        return "action_math_operation"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict[Text, Any]]:

        # get slots
        operation = tracker.get_slot("operation")
        operand1 = tracker.get_slot("operand1")
        operand2 = tracker.get_slot("operand2")

        # perform math operation
        if operation == "add":
            result = operand1 + operand2
            message = f"Sum of {operand1} and {operand2} is {result}"
        elif operation == "subtract":
            result = operand1 - operand2
            message = f"Difference between {operand1} and {operand2} is {result}"
        elif operation == "multiply":
            result = operand1 * operand2
            message = f"Product of {operand1} and {operand2} is {result}"
        elif operation == "divide":
            if operand2 == 0:
                message = "Cannot divide by zero. Please enter a valid second operand."
            else:
                result = operand1 / operand2
                message = f"Division of {operand1} by {operand2} is {result}"
        else:
            message = "Invalid operation selected. Please select a valid operation."

        dispatcher.utter_message(text=message)

        # reset slots
        return [
            SlotSet("operation", None),
            SlotSet("operand1", None),
            SlotSet("operand2", None),
        ]
