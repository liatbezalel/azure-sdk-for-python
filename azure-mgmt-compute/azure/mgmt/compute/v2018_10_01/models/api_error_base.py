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


class ApiErrorBase(Model):
    """Api error base.

    :param code: The error code.
    :type code: str
    :param target: The target of the particular error.
    :type target: str
    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApiErrorBase, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.target = kwargs.get('target', None)
        self.message = kwargs.get('message', None)
