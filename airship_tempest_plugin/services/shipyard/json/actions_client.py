# Copyright 2018 AT&T Corp
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""
http://airship-shipyard.readthedocs.io/en/latest/API.html#action-api
"""

from oslo_serialization import jsonutils as json

from tempest.lib.common import rest_client


# NOTE(rb560u): The following will need to be rewritten in the future if
# functional testing is desired:
#  - 'def create_action`
# This initial implementation is just to meet the first use case which is RBAC
# testing. For RBAC testing, we only need to hit the API endpoint and check
# role permission to that API.


class ActionsClient(rest_client.RestClient):
    api_version = "v1.0"

    def list_actions(self):
        resp, body = self.get('actions')
        self.expected_success(200, resp.status)
        body = json.loads(body)
        if isinstance(body, list):
            return rest_client.ResponseBodyList(resp, body)
        else:
            return rest_client.ResponseBody(resp, body)

    def create_action(self, action=None):
        url = 'actions'
        # Update post_body if functional testing is desired
        post_body = json.dumps({"name": action})
        resp, body = self.post(url, post_body)
        self.expected_success(201, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def get_action(self, action_id=None):
        resp, body = self.get('actions/%s' % action_id)
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def get_action_validation(self, action_id=None, validation_id=None):
        resp, body = \
            self.get('actions/%s/validations/%s' % (action_id, validation_id))
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def get_action_step(self, action_id=None, step_id=None):
        resp, body = self.get('actions/%s/steps/%s' % (action_id, step_id))
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)

    def invoke_action_control(self, action_id=None, control_verb=None):
        url = 'actions/%s/control/%s' % (action_id, control_verb)
        post_body = json.dumps({})
        resp, body = self.post(url, post_body)
        self.expected_success(202, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)
