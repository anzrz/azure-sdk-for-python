# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from msrest import Deserializer, Serializer

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models
from ._configuration import SearchClientConfiguration
from .operations import AliasesOperations, DataSourcesOperations, IndexersOperations, IndexesOperations, SearchClientOperationsMixin, SkillsetsOperations, SynonymMapsOperations

class SearchClient(SearchClientOperationsMixin):    # pylint: disable=too-many-instance-attributes
    """Client that can be used to manage and query indexes and documents, as well as manage other
    resources, on a search service.

    :ivar data_sources: DataSourcesOperations operations
    :vartype data_sources: azure.search.documents.indexes.aio.operations.DataSourcesOperations
    :ivar indexers: IndexersOperations operations
    :vartype indexers: azure.search.documents.indexes.aio.operations.IndexersOperations
    :ivar skillsets: SkillsetsOperations operations
    :vartype skillsets: azure.search.documents.indexes.aio.operations.SkillsetsOperations
    :ivar synonym_maps: SynonymMapsOperations operations
    :vartype synonym_maps: azure.search.documents.indexes.aio.operations.SynonymMapsOperations
    :ivar indexes: IndexesOperations operations
    :vartype indexes: azure.search.documents.indexes.aio.operations.IndexesOperations
    :ivar aliases: AliasesOperations operations
    :vartype aliases: azure.search.documents.indexes.aio.operations.AliasesOperations
    :param endpoint: The endpoint URL of the search service.
    :type endpoint: str
    :keyword api_version: Api Version. The default value is "2021-04-30-Preview". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        endpoint: str,
        **kwargs: Any
    ) -> None:
        _base_url = '{endpoint}'
        self._config = SearchClientConfiguration(endpoint=endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=_base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.data_sources = DataSourcesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.indexers = IndexersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.skillsets = SkillsetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.synonym_maps = SynonymMapsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.indexes = IndexesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.aliases = AliasesOperations(self._client, self._config, self._serialize, self._deserialize)


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
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SearchClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
