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

from oslo_policy import opts as policy_opts
from oslo_utils import fileutils

from oslo_upgradecheck import upgradecheck

"""
Common checks which can be used by multiple services.
"""


def check_policy_json(self, conf):
    "Checks to see if policy file is JSON-formatted policy file."

    # NOTE(gmann): This method need [oslo_policy].policy_file
    # config value so register those options in case they
    # are not register by services.
    conf.register_opts(policy_opts._options,
                       group=policy_opts._option_group)

    msg = ("Your policy file is JSON-formatted which is "
           "deprecated. You need to switch to YAML-formatted file. "
           "Use the ``oslopolicy-convert-json-to-yaml`` "
           "tool to convert the existing JSON-formatted files to "
           "YAML in a backwards-compatible manner: "
           "https://docs.openstack.org/oslo.policy/"
           "latest/cli/oslopolicy-convert-json-to-yaml.html.")
    status = upgradecheck.Result(upgradecheck.Code.SUCCESS)
    # Check if policy file exist and is JSON-formatted.
    policy_path = conf.find_file(conf.oslo_policy.policy_file)
    if policy_path and fileutils.is_json(policy_path):
        status = upgradecheck.Result(upgradecheck.Code.FAILURE, msg)
    return status
