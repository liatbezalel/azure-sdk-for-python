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


class Operation(Model):
    """HANA operation information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation being performed on this particular
     object. This name should match the action name that appears in RBAC / the
     event service.
    :vartype name: str
    :param display: Displayed HANA operation information
    :type display: ~azure.mgmt.hanaonazure.models.Display
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'Display'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = kwargs.get('display', None)
