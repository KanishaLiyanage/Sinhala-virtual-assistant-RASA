from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from datetime import date as dt, timedelta

class ActionGetBalance(Action):

    def name(self) -> Text:
        return "action_get_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        trackers = tracker.latest_message['entities']
        print(trackers)
        
        message = "Balance triggered!"

        dispatcher.utter_message(text = message)

        return []

class ActionGetPackage(Action):

    def name(self) -> Text:
        return "action_get_package"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        trackers = tracker.latest_message['entities']
        print(trackers)
    
        message = "Package triggered!"

        dispatcher.utter_message(text = message)

        return []
    
class ActionGetLoyalty(Action):

    def name(self) -> Text:
        return "action_get_loyalty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        trackers = tracker.latest_message['entities']
        print(trackers)
    
        message = "Loyalty triggered!"

        dispatcher.utter_message(text = message)

        return []
    
class ActionGetUsage(Action):

    def name(self) -> Text:
        return "action_get_usage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        trackers = tracker.latest_message['entities']
        print(trackers)

        message = "Usage triggered!"

        dispatcher.utter_message(text = message)

        return []
    
class ActionGetPaymentHistory(Action):

    def name(self) -> Text:
        return "action_get_payment_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        trackers = tracker.latest_message['entities']
        print(trackers)
    
        message = "Payment History triggered!"

        dispatcher.utter_message(text = message)

        return []
    
class ActionUpgradePackage(Action):

    def name(self) -> Text:
        return "action_package_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        trackers = tracker.latest_message['entities']
        print(trackers)

        message = "Package Upgrade Triggered!"

        dispatcher.utter_message(text = message)

        return []