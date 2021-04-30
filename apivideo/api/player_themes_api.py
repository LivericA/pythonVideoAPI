"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem-team@api.video
"""

import os  # noqa: F401
import re  # noqa: F401
import sys  # noqa: F401

from apivideo.api_client import ApiClient
from apivideo.endpoint import EndPoint as _EndPoint
from apivideo.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from apivideo.exceptions import ApiTypeError, ApiValueError
from apivideo.model.bad_request import BadRequest
from apivideo.model.not_found import NotFound
from apivideo.model.player import Player
from apivideo.model.player_creation_payload import PlayerCreationPayload
from apivideo.model.player_update_payload import PlayerUpdatePayload
from apivideo.model.players_list_response import PlayersListResponse


class PlayerThemesApi(_EndPoint):
    """NOTE: This class is auto generated. Do not edit the class manually.
    """

    def delete(
            self,
            player_id,
            **kwargs
        ):
            """Delete a player  # noqa: E501

            Delete a player if you no longer need it. You can delete any player that you have the player ID for.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete(player_id, async_req=True)
            >>> result = thread.get()

            Args:
                player_id (str): The unique identifier for the player you want to delete.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['player_id'] = \
                player_id

            params_map = {
                'all': [
                    'player_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [
                    'player_id',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'player_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
                'player_id': 'playerId',
            }
            location_map = {
                'player_id': 'path',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `delete`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `delete`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`delete`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/players/{playerId}",
                "DELETE",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=None,
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def delete_logo(
            self,
            player_id,
            **kwargs
        ):
            """Delete logo  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_logo(player_id, async_req=True)
            >>> result = thread.get()

            Args:
                player_id (str): The unique identifier for the player.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['player_id'] = \
                player_id

            params_map = {
                'all': [
                    'player_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [
                    'player_id',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'player_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
                'player_id': 'playerId',
            }
            location_map = {
                'player_id': 'path',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `delete_logo`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `delete_logo`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`delete_logo`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/players/{playerId}/logo",
                "DELETE",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=None,
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def list(
            self,
            **kwargs
        ):
            """List all players  # noqa: E501

            Retrieve a list of all the players you created, as well as details about each one.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                sort_by (str): createdAt is the time the player was created. updatedAt is the time the player was last updated. The time is presented in ISO-8601 format.. [optional]
                sort_order (str): Allowed: asc, desc. Ascending for date and time means that earlier values precede later ones. Descending means that later values preced earlier ones.. [optional]
                current_page (int): Choose the number of search results to return per page. Minimum value: 1. [optional] if omitted the server will use the default value of 1
                page_size (int): Results per page. Allowed values 1-100, default is 25.. [optional] if omitted the server will use the default value of 25
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                async_req (bool): execute request asynchronously

            Returns:
                PlayersListResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )

            params_map = {
                'all': [
                    'sort_by',
                    'sort_order',
                    'current_page',
                    'page_size',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                    'sort_by',
                    'sort_order',
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
                ('sort_by',): {

                    "CREATEDAT": "createdAt",
                    "UPDATEDAT": "updatedAt"
                },
                ('sort_order',): {

                    "ASC": "asc",
                    "DESC": "desc"
                },
            }
            openapi_types = {
                'sort_by':
                    (str,),
                'sort_order':
                    (str,),
                'current_page':
                    (int,),
                'page_size':
                    (int,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
                'sort_by': 'sortBy',
                'sort_order': 'sortOrder',
                'current_page': 'currentPage',
                'page_size': 'pageSize',
            }
            location_map = {
                'sort_by': 'query',
                'sort_order': 'query',
                'current_page': 'query',
                'page_size': 'query',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `list`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `list`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`list`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/players",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(PlayersListResponse,),
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def get(
            self,
            player_id,
            **kwargs
        ):
            """Show a player  # noqa: E501

            Use a player ID to retrieve details about the player and display it for viewers.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get(player_id, async_req=True)
            >>> result = thread.get()

            Args:
                player_id (str): The unique identifier for the player you want to retrieve. 

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                async_req (bool): execute request asynchronously

            Returns:
                Player
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['player_id'] = \
                player_id

            params_map = {
                'all': [
                    'player_id',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [
                    'player_id',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'player_id':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
                'player_id': 'playerId',
            }
            location_map = {
                'player_id': 'path',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/players/{playerId}",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(Player,),
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def update(
            self,
            player_id,
            player_update_payload,
            **kwargs
        ):
            """Update a player  # noqa: E501

            Use a player ID to update specific details for a player. NOTE: It may take up to 10 min before the new player configuration is available from our CDN.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update(player_id, player_update_payload, async_req=True)
            >>> result = thread.get()

            Args:
                player_id (str): The unique identifier for the player.
                player_update_payload (PlayerUpdatePayload):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                async_req (bool): execute request asynchronously

            Returns:
                Player
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['player_id'] = \
                player_id
            kwargs['player_update_payload'] = \
                player_update_payload

            params_map = {
                'all': [
                    'player_id',
                    'player_update_payload',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [
                    'player_id',
                    'player_update_payload',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'player_id':
                    (str,),
                'player_update_payload':
                    (PlayerUpdatePayload,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
                'player_id': 'playerId',
            }
            location_map = {
                'player_id': 'path',
                'player_update_payload': 'body',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `update`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `update`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`update`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/players/{playerId}",
                "PATCH",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(Player,),
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def create(
            self,
            player_creation_payload,
            **kwargs
        ):
            """Create a player  # noqa: E501

            Create a player for your video, and customise it.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create(player_creation_payload, async_req=True)
            >>> result = thread.get()

            Args:
                player_creation_payload (PlayerCreationPayload):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                async_req (bool): execute request asynchronously

            Returns:
                Player
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['player_creation_payload'] = \
                player_creation_payload

            params_map = {
                'all': [
                    'player_creation_payload',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [
                    'player_creation_payload',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'player_creation_payload':
                    (PlayerCreationPayload,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
            }
            location_map = {
                'player_creation_payload': 'body',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `create`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `create`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`create`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/players",
                "POST",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(Player,),
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def upload_logo(
            self,
            player_id,
            file,
            link,
            **kwargs
        ):
            """Upload a logo  # noqa: E501

            The uploaded image maximum size should be 200x100 and its weight should be 200KB.  It will be scaled down to 30px height and converted to PNG to be displayed in the player.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.upload_logo(player_id, file, link, async_req=True)
            >>> result = thread.get()

            Args:
                player_id (str): The unique identifier for the player.
                file (file_type): The name of the file you want to use for your logo.
                link (str): The path to the file you want to upload and use as a logo.

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                async_req (bool): execute request asynchronously

            Returns:
                Player
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['player_id'] = \
                player_id
            kwargs['file'] = \
                file
            kwargs['link'] = \
                link

            params_map = {
                'all': [
                    'player_id',
                    'file',
                    'link',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [
                    'player_id',
                    'file',
                    'link',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'player_id':
                    (str,),
                'file':
                    (file_type,),
                'link':
                    (str,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
                'player_id': 'playerId',
                'file': 'file',
                'link': 'link',
            }
            location_map = {
                'player_id': 'path',
                'file': 'form',
                'link': 'form',
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `upload_logo`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `upload_logo`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`upload_logo`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/players/{playerId}/logo",
                "POST",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(Player,),
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

