# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._search_client_operations import build_get_service_statistics_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SearchClientOperationsMixin:

    @distributed_trace_async
    async def get_service_statistics(
        self,
        request_options: Optional["_models.RequestOptions"] = None,
        **kwargs: Any
    ) -> "_models.ServiceStatistics":
        """Gets service level statistics for a search service.

        :param request_options: Parameter group.
        :type request_options: ~azure.search.documents.indexes.models.RequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ServiceStatistics, or the result of cls(response)
        :rtype: ~azure.search.documents.indexes.models.ServiceStatistics
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ServiceStatistics"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-04-30-Preview")  # type: str

        _x_ms_client_request_id = None
        if request_options is not None:
            _x_ms_client_request_id = request_options.x_ms_client_request_id

        request = build_get_service_statistics_request(
            api_version=api_version,
            x_ms_client_request_id=_x_ms_client_request_id,
            template_url=self.get_service_statistics.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.SearchError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ServiceStatistics', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_service_statistics.metadata = {'url': "/servicestats"}  # type: ignore

