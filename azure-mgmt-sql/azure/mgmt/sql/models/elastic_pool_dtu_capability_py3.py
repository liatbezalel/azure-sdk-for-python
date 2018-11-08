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


class ElasticPoolDtuCapability(Model):
    """The Elastic Pool DTU capability.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar limit: The DTU limit for the pool.
    :vartype limit: int
    :ivar max_database_count: The maximum number of databases supported.
    :vartype max_database_count: int
    :ivar included_max_size: The included (free) max size for this DTU.
    :vartype included_max_size: ~azure.mgmt.sql.models.MaxSizeCapability
    :ivar supported_max_sizes: The list of supported max sizes.
    :vartype supported_max_sizes:
     list[~azure.mgmt.sql.models.MaxSizeCapability]
    :ivar supported_per_database_max_sizes: The list of supported per database
     max sizes.
    :vartype supported_per_database_max_sizes:
     list[~azure.mgmt.sql.models.MaxSizeCapability]
    :ivar supported_per_database_max_dtus: The list of supported per database
     max DTUs.
    :vartype supported_per_database_max_dtus:
     list[~azure.mgmt.sql.models.ElasticPoolPerDatabaseMaxDtuCapability]
    :ivar status: The status of the capability. Possible values include:
     'Visible', 'Available', 'Default', 'Disabled'
    :vartype status: str or ~azure.mgmt.sql.models.CapabilityStatus
    :param reason: The reason for the capability not being available.
    :type reason: str
    """

    _validation = {
        'limit': {'readonly': True},
        'max_database_count': {'readonly': True},
        'included_max_size': {'readonly': True},
        'supported_max_sizes': {'readonly': True},
        'supported_per_database_max_sizes': {'readonly': True},
        'supported_per_database_max_dtus': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'limit': {'key': 'limit', 'type': 'int'},
        'max_database_count': {'key': 'maxDatabaseCount', 'type': 'int'},
        'included_max_size': {'key': 'includedMaxSize', 'type': 'MaxSizeCapability'},
        'supported_max_sizes': {'key': 'supportedMaxSizes', 'type': '[MaxSizeCapability]'},
        'supported_per_database_max_sizes': {'key': 'supportedPerDatabaseMaxSizes', 'type': '[MaxSizeCapability]'},
        'supported_per_database_max_dtus': {'key': 'supportedPerDatabaseMaxDtus', 'type': '[ElasticPoolPerDatabaseMaxDtuCapability]'},
        'status': {'key': 'status', 'type': 'CapabilityStatus'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(self, *, reason: str=None, **kwargs) -> None:
        super(ElasticPoolDtuCapability, self).__init__(**kwargs)
        self.limit = None
        self.max_database_count = None
        self.included_max_size = None
        self.supported_max_sizes = None
        self.supported_per_database_max_sizes = None
        self.supported_per_database_max_dtus = None
        self.status = None
        self.reason = reason