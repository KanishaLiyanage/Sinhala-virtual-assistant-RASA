from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
from datetime import date as dt, timedelta
from db_connection import get_balance, get_package, get_loyalty, get_usage, get_payment_history
    
class ActionGetBalance(Action):

    def name(self) -> Text:
        return "action_get_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = ""

        trackers = tracker.latest_message['entities']
        print(trackers)

        for tracker in trackers:
            if tracker['entity'] == 'name':
                name = tracker['value']

        print(name)
        # Call the get_balance function to fetch the balance for the specified customer
        balance = get_balance(name)

        # Process the fetched balance as needed
        dispatcher.utter_message(f"{name}, your account balance is Rs. {balance}")

        return []

class ActionGetPackage(Action):

    def name(self) -> Text:
        return "action_get_package"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = ""

        trackers = tracker.latest_message['entities']
        print(trackers)

        for tracker in trackers:
            if tracker['entity'] == 'name':
                name = tracker['value']

        print(name)
        # Call the get_package function to fetch the package for the specified customer
        package = get_package(name)

        # Process the fetched package as needed
        dispatcher.utter_message(f"{name}, your package is {package}")

        return []
    
class ActionGetLoyalty(Action):

    def name(self) -> Text:
        return "action_get_loyalty"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = ""

        trackers = tracker.latest_message['entities']
        print(trackers)

        for tracker in trackers:
            if tracker['entity'] == 'name':
                name = tracker['value']

        print(name)
        loyalty_points = get_loyalty(name)

        dispatcher.utter_message(f"{name}, your remain loyalty points are {loyalty_points}")

        return []
    
class ActionGetUsage(Action):

    def name(self) -> Text:
        return "action_get_usage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
        name = ""

        trackers = tracker.latest_message['entities']
        print(trackers)

        for tracker in trackers:
            if tracker['entity'] == 'name':
                name = tracker['value']

        print(name)
        usage_report = get_usage(name)

        dispatcher.utter_message(f"{name}, your usage report is, \n {usage_report}")

        return []
    
class ActionGetPaymentHistory(Action):

    def name(self) -> Text:
        return "action_get_payment_history"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = ""

        trackers = tracker.latest_message['entities']
        print(trackers)

        for tracker in trackers:
            if tracker['entity'] == 'name':
                name = tracker['value']

        print(name)
        payment_history = get_payment_history(name)

        dispatcher.utter_message(f"{name}, Here is your payment history \n {payment_history}")

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