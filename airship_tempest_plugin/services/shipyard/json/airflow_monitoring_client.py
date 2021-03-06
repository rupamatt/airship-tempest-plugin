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
http://airship-shipyard.readthedocs.io/en/latest/API.html#airflow-monitoring-api
"""

from oslo_serialization import jsonutils as json
from tempest.lib.common import rest_client


class AirflowMonitoringClient(rest_client.RestClient):
    api_version = "v1.0"

    def list_workflows(self):
        resp, body = self.get('workflows')
        self.expected_success(200, resp.status)
        body = json.loads(body)
        if isinstance(body, list):
            return rest_client.ResponseBodyList(resp, body)
        else:
            return rest_client.ResponseBody(resp, body)

    def get_workflow(self, workflow_id=None):
        resp, body = self.get('workflows/%s' % workflow_id)
        self.expected_success(200, resp.status)
        body = json.loads(body)
        return rest_client.ResponseBody(resp, body)
