# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_request(
    subscription_id: str,
    resource_group: str,
    fluid_relay_server_name: str,
    fluid_relay_container_name: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/fluidRelayContainers/{fluidRelayContainerName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroup": _SERIALIZER.url("resource_group", resource_group, 'str'),
        "fluidRelayServerName": _SERIALIZER.url("fluid_relay_server_name", fluid_relay_server_name, 'str'),
        "fluidRelayContainerName": _SERIALIZER.url("fluid_relay_container_name", fluid_relay_container_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_delete_request(
    subscription_id: str,
    resource_group: str,
    fluid_relay_server_name: str,
    fluid_relay_container_name: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/fluidRelayContainers/{fluidRelayContainerName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroup": _SERIALIZER.url("resource_group", resource_group, 'str'),
        "fluidRelayServerName": _SERIALIZER.url("fluid_relay_server_name", fluid_relay_server_name, 'str'),
        "fluidRelayContainerName": _SERIALIZER.url("fluid_relay_container_name", fluid_relay_container_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_list_by_fluid_relay_servers_request(
    subscription_id: str,
    resource_group: str,
    fluid_relay_server_name: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/fluidRelayContainers")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroup": _SERIALIZER.url("resource_group", resource_group, 'str'),
        "fluidRelayServerName": _SERIALIZER.url("fluid_relay_server_name", fluid_relay_server_name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

class FluidRelayContainersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.fluidrelay.FluidRelayManagementClient`'s
        :attr:`fluid_relay_containers` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def get(
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        fluid_relay_container_name: str,
        **kwargs: Any
    ) -> _models.FluidRelayContainer:
        """Get a Fluid Relay container.

        Get a Fluid Relay container.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :param fluid_relay_container_name: The Fluid Relay container resource name.
        :type fluid_relay_container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FluidRelayContainer, or the result of cls(response)
        :rtype: ~azure.mgmt.fluidrelay.models.FluidRelayContainer
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayContainer]

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            fluid_relay_container_name=fluid_relay_container_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FluidRelayContainer', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/fluidRelayContainers/{fluidRelayContainerName}"}  # type: ignore


    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        fluid_relay_container_name: str,
        **kwargs: Any
    ) -> None:
        """Delete a Fluid Relay container.

        Delete a Fluid Relay container.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :param fluid_relay_container_name: The Fluid Relay container resource name.
        :type fluid_relay_container_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[None]

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group=resource_group,
            fluid_relay_server_name=fluid_relay_server_name,
            fluid_relay_container_name=fluid_relay_container_name,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/fluidRelayContainers/{fluidRelayContainerName}"}  # type: ignore


    @distributed_trace
    def list_by_fluid_relay_servers(
        self,
        resource_group: str,
        fluid_relay_server_name: str,
        **kwargs: Any
    ) -> Iterable[_models.FluidRelayContainerList]:
        """List all Fluid Relay containers which are children of a given Fluid Relay server.

        List all Fluid Relay containers which are children of a given Fluid Relay server.

        :param resource_group: The resource group containing the resource.
        :type resource_group: str
        :param fluid_relay_server_name: The Fluid Relay server resource name.
        :type fluid_relay_server_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FluidRelayContainerList or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.fluidrelay.models.FluidRelayContainerList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2022-06-01"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.FluidRelayContainerList]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_fluid_relay_servers_request(
                    subscription_id=self._config.subscription_id,
                    resource_group=resource_group,
                    fluid_relay_server_name=fluid_relay_server_name,
                    api_version=api_version,
                    template_url=self.list_by_fluid_relay_servers.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_fluid_relay_servers_request(
                    subscription_id=self._config.subscription_id,
                    resource_group=resource_group,
                    fluid_relay_server_name=fluid_relay_server_name,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("FluidRelayContainerList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_fluid_relay_servers.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.FluidRelay/fluidRelayServers/{fluidRelayServerName}/fluidRelayContainers"}  # type: ignore