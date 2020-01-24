# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
#  from rasa_sdk import Action, Tracker
#  from rasa_sdk.executor import CollectingDispatcher
#
#
#  class ActionHelloWorld(Action):

#      def name(self) -> Text:
#          return "action_hello_world"
# 
#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# 
#          dispatcher.utter_message("Hello World!")
#
#          return []

#class ActionSubscribeNewsletter(Action):
#    """ This action calls our newsletter API and subscribes the user with their email address"""

#    def name(self):
#        return "action_subscribe_newsletter"

#    def run(self, dispatcher, tracker, domain):
#        email = tracker.get_slot('email')
#        if email:
            # if the email is already subscribed, this returns False
#            subscribed = check_if_subscribed(email)

#            return [SlotSet('subscribed', subscribed)]
#        return []







