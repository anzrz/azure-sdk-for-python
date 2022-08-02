# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models
from ._configuration import AutomanageClientConfiguration
from .operations import BestPracticesOperations, BestPracticesVersionsOperations, ConfigurationProfileAssignmentsOperations, ConfigurationProfileHCIAssignmentsOperations, ConfigurationProfileHCRPAssignmentsOperations, ConfigurationProfilesOperations, ConfigurationProfilesVersionsOperations, HCIReportsOperations, HCRPReportsOperations, Operations, ReportsOperations, ServicePrincipalsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class AutomanageClient:    # pylint: disable=too-many-instance-attributes
    """Automanage Client.

    :ivar best_practices: BestPracticesOperations operations
    :vartype best_practices: azure.mgmt.automanage.aio.operations.BestPracticesOperations
    :ivar best_practices_versions: BestPracticesVersionsOperations operations
    :vartype best_practices_versions:
     azure.mgmt.automanage.aio.operations.BestPracticesVersionsOperations
    :ivar configuration_profiles: ConfigurationProfilesOperations operations
    :vartype configuration_profiles:
     azure.mgmt.automanage.aio.operations.ConfigurationProfilesOperations
    :ivar configuration_profiles_versions: ConfigurationProfilesVersionsOperations operations
    :vartype configuration_profiles_versions:
     azure.mgmt.automanage.aio.operations.ConfigurationProfilesVersionsOperations
    :ivar configuration_profile_assignments: ConfigurationProfileAssignmentsOperations operations
    :vartype configuration_profile_assignments:
     azure.mgmt.automanage.aio.operations.ConfigurationProfileAssignmentsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.automanage.aio.operations.Operations
    :ivar reports: ReportsOperations operations
    :vartype reports: azure.mgmt.automanage.aio.operations.ReportsOperations
    :ivar service_principals: ServicePrincipalsOperations operations
    :vartype service_principals: azure.mgmt.automanage.aio.operations.ServicePrincipalsOperations
    :ivar configuration_profile_hcrp_assignments: ConfigurationProfileHCRPAssignmentsOperations
     operations
    :vartype configuration_profile_hcrp_assignments:
     azure.mgmt.automanage.aio.operations.ConfigurationProfileHCRPAssignmentsOperations
    :ivar hcrp_reports: HCRPReportsOperations operations
    :vartype hcrp_reports: azure.mgmt.automanage.aio.operations.HCRPReportsOperations
    :ivar configuration_profile_hci_assignments: ConfigurationProfileHCIAssignmentsOperations
     operations
    :vartype configuration_profile_hci_assignments:
     azure.mgmt.automanage.aio.operations.ConfigurationProfileHCIAssignmentsOperations
    :ivar hci_reports: HCIReportsOperations operations
    :vartype hci_reports: azure.mgmt.automanage.aio.operations.HCIReportsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-05-04". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = AutomanageClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.best_practices = BestPracticesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.best_practices_versions = BestPracticesVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configuration_profiles = ConfigurationProfilesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configuration_profiles_versions = ConfigurationProfilesVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configuration_profile_assignments = ConfigurationProfileAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.reports = ReportsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.service_principals = ServicePrincipalsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configuration_profile_hcrp_assignments = ConfigurationProfileHCRPAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.hcrp_reports = HCRPReportsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configuration_profile_hci_assignments = ConfigurationProfileHCIAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.hci_reports = HCIReportsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutomanageClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)