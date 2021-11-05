# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, Iterable, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_list_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/libraries')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_flush_request_initial(
    library_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/libraries/{libraryName}/flush')
    path_format_arguments = {
        "libraryName": _SERIALIZER.url("library_name", library_name, 'str', max_length=100, min_length=0),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_operation_result_request(
    operation_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/libraryOperationResults/{operationId}')
    path_format_arguments = {
        "operationId": _SERIALIZER.url("operation_id", operation_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request_initial(
    library_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/libraries/{libraryName}')
    path_format_arguments = {
        "libraryName": _SERIALIZER.url("library_name", library_name, 'str', max_length=100, min_length=0),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    library_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/libraries/{libraryName}')
    path_format_arguments = {
        "libraryName": _SERIALIZER.url("library_name", library_name, 'str', max_length=100, min_length=0),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_request_initial(
    library_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/libraries/{libraryName}')
    path_format_arguments = {
        "libraryName": _SERIALIZER.url("library_name", library_name, 'str', max_length=100, min_length=0),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_append_request(
    library_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    comp = kwargs.pop('comp', "appendblock")  # type: str
    api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    blob_condition_append_position = kwargs.pop('blob_condition_append_position', None)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/libraries/{libraryName}')
    path_format_arguments = {
        "libraryName": _SERIALIZER.url("library_name", library_name, 'str', max_length=100, min_length=0),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['comp'] = _SERIALIZER.query("comp", comp, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if blob_condition_append_position is not None:
        header_parameters['x-ms-blob-condition-appendpos'] = _SERIALIZER.header("blob_condition_append_position", blob_condition_append_position, 'long')
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class LibraryOperations(object):
    """LibraryOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.synapse.artifacts.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.LibraryListResponse"]
        """Lists Library.

        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either LibraryListResponse or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.synapse.artifacts.models.LibraryListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LibraryListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_list_request(
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("LibraryListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/libraries'}  # type: ignore

    def _flush_initial(
        self,
        library_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LibraryResourceInfo"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LibraryResourceInfo"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_flush_request_initial(
            library_name=library_name,
            api_version=api_version,
            template_url=self._flush_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 202:
            deserialized = self._deserialize('LibraryResourceInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _flush_initial.metadata = {'url': '/libraries/{libraryName}/flush'}  # type: ignore


    @distributed_trace
    def begin_flush(
        self,
        library_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.LibraryResourceInfo"]
        """Flush Library.

        :param library_name: file name to upload. Minimum length of the filename should be 1 excluding
         the extension length.
        :type library_name: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either LibraryResourceInfo or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.LibraryResourceInfo]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LibraryResourceInfo"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._flush_initial(
                library_name=library_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('LibraryResourceInfo', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_flush.metadata = {'url': '/libraries/{libraryName}/flush'}  # type: ignore

    @distributed_trace
    def get_operation_result(
        self,
        operation_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Union["_models.LibraryResource", "_models.OperationResult"]
        """Get Operation result for Library.

        :param operation_id: operation id for which status is requested.
        :type operation_id: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LibraryResource or OperationResult, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.LibraryResource or
         ~azure.synapse.artifacts.models.OperationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["_models.LibraryResource", "_models.OperationResult"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_get_operation_result_request(
            operation_id=operation_id,
            api_version=api_version,
            template_url=self.get_operation_result.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('LibraryResource', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('OperationResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_operation_result.metadata = {'url': '/libraryOperationResults/{operationId}'}  # type: ignore


    def _delete_initial(
        self,
        library_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LibraryResourceInfo"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LibraryResourceInfo"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_delete_request_initial(
            library_name=library_name,
            api_version=api_version,
            template_url=self._delete_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 409]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 202:
            deserialized = self._deserialize('LibraryResourceInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _delete_initial.metadata = {'url': '/libraries/{libraryName}'}  # type: ignore


    @distributed_trace
    def begin_delete(
        self,
        library_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.LibraryResourceInfo"]
        """Delete Library.

        :param library_name: file name to upload. Minimum length of the filename should be 1 excluding
         the extension length.
        :type library_name: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either LibraryResourceInfo or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.LibraryResourceInfo]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LibraryResourceInfo"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(
                library_name=library_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('LibraryResourceInfo', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {'url': '/libraries/{libraryName}'}  # type: ignore

    @distributed_trace
    def get(
        self,
        library_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LibraryResource"]
        """Get Library.

        :param library_name: file name to upload. Minimum length of the filename should be 1 excluding
         the extension length.
        :type library_name: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LibraryResource, or the result of cls(response)
        :rtype: ~azure.synapse.artifacts.models.LibraryResource or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LibraryResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_get_request(
            library_name=library_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LibraryResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/libraries/{libraryName}'}  # type: ignore


    def _create_initial(
        self,
        library_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.LibraryResourceInfo"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.LibraryResourceInfo"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str

        
        request = build_create_request_initial(
            library_name=library_name,
            api_version=api_version,
            template_url=self._create_initial.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 202:
            deserialized = self._deserialize('LibraryResourceInfo', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_initial.metadata = {'url': '/libraries/{libraryName}'}  # type: ignore


    @distributed_trace
    def begin_create(
        self,
        library_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.LibraryResourceInfo"]
        """Creates a library with the library name.

        :param library_name: file name to upload. Minimum length of the filename should be 1 excluding
         the extension length.
        :type library_name: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either LibraryResourceInfo or the result of
         cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.synapse.artifacts.models.LibraryResourceInfo]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        polling = kwargs.pop('polling', True)  # type: Union[bool, azure.core.polling.PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.LibraryResourceInfo"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_initial(
                library_name=library_name,
                api_version=api_version,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('LibraryResourceInfo', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        if polling is True: polling_method = LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create.metadata = {'url': '/libraries/{libraryName}'}  # type: ignore

    @distributed_trace
    def append(
        self,
        library_name,  # type: str
        content,  # type: IO
        blob_condition_append_position=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Append the content to the library resource created using the create operation. The maximum
        content size is 4MiB. Content larger than 4MiB must be appended in 4MiB chunks.

        :param library_name: file name to upload. Minimum length of the filename should be 1 excluding
         the extension length.
        :type library_name: str
        :param content: Library file chunk.
        :type content: IO
        :param blob_condition_append_position: Set this header to a byte offset at which the block is
         expected to be appended. The request succeeds only if the current offset matches this value.
         Otherwise, the request fails with the AppendPositionConditionNotMet error (HTTP status code 412
         – Precondition Failed).
        :type blob_condition_append_position: long
        :keyword comp: The default value is "appendblock". Note that overriding this default value may
         result in unsupported behavior.
        :paramtype comp: str
        :keyword api_version: Api Version. The default value is "2020-12-01". Note that overriding this
         default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        comp = kwargs.pop('comp', "appendblock")  # type: str
        api_version = kwargs.pop('api_version', "2020-12-01")  # type: str
        content_type = kwargs.pop('content_type', "application/octet-stream")  # type: Optional[str]

        content = content

        request = build_append_request(
            library_name=library_name,
            comp=comp,
            api_version=api_version,
            content_type=content_type,
            content=content,
            content=content,
            blob_condition_append_position=blob_condition_append_position,
            template_url=self.append.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudErrorAutoGenerated, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    append.metadata = {'url': '/libraries/{libraryName}'}  # type: ignore

