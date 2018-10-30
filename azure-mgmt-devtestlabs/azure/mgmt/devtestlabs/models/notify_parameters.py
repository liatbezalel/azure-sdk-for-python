# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NotifyParameters(Model):
    """Properties for generating a Notification.

    :param event_name: The type of event (i.e. AutoShutdown, Cost). Possible
     values include: 'AutoShutdown', 'Cost'
    :type event_name: str or
     ~azure.mgmt.devtestlabs.models.NotificationChannelEventType
    :param json_payload: Properties for the notification in json format.
    :type json_payload: str
    """

    _attribute_map = {
        'event_name': {'key': 'eventName', 'type': 'str'},
        'json_payload': {'key': 'jsonPayload', 'type': 'str'},
    }

    def __init__(self, event_name=None, json_payload=None):
        super(NotifyParameters, self).__init__()
        self.event_name = event_name
        self.json_payload = json_payload