# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import
from tapioca import (TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)
from requests_oauthlib import OAuth2
from resource_mapping import RESOURCE_MAPPING
import re



class BookingSyncClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://www.bookingsync.com/api/v3/'
    resource_mapping = RESOURCE_MAPPING
    re_links = re.compile(
        r'(?i)(?:<(?P<link>(?:[\w\.\d\/\=:]*)(?:\?page=(?P<page>\d+)))>;\s*rel="(?P<rel>first|next|prev|last)")')

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(BookingSyncClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = OAuth2(
            api_params.get('client_id', ''), token={
                'access_token': api_params.get('access_token'),
                'token_type': 'Bearer'})

        return params

    def process_response(self, response):
        obj = super(BookingSyncClientAdapter, self).process_response(response)
        return obj

    def get_iterator_list(self, response_data):
        # items = []
        # assert isinstance(response_data, dict)
        # for k, v in response_data.iteritems():
        #     if isinstance(v, list):
        #         items.extend(v)
        # return items
        return response_data

    def response_to_native(self, response):
        native = super(BookingSyncClientAdapter, self).response_to_native(response)
        items = []
        assert isinstance(native, dict)
        for k, v in native.iteritems():
            if isinstance(v, list):
                items.extend(v)
        return items

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs, response_data, response):
        links = [m.groupdict() for m in self.re_links.finditer(response.headers['link'])]
        next_link = filter(lambda x: x.get('rel') == 'next', links)
        if not next_link:
            return
        else:
            return {'url': next_link[0]['link']}


BookingSync = generate_wrapper_from_adapter(BookingSyncClientAdapter)
