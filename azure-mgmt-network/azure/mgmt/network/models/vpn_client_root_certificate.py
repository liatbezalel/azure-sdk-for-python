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

from .sub_resource import SubResource


class VpnClientRootCertificate(SubResource):
    """VPN client root certificate of virtual network gateway.

    :param id: Resource Id
    :type id: str
    :param public_cert_data: Gets or sets the certificate public data
    :type public_cert_data: str
    :param provisioning_state: Gets provisioning state of the VPN client root
     certificate resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'public_cert_data': {'key': 'properties.publicCertData', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, public_cert_data=None, provisioning_state=None, name=None, etag=None):
        super(VpnClientRootCertificate, self).__init__(id=id)
        self.public_cert_data = public_cert_data
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag