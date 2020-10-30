# MSC-26646-1, "Core Flight System Test Framework (CTF)"
#
# Copyright (c) 2019-2020 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration. All Rights Reserved.
#
# This software is governed by the NASA Open Source Agreement (NOSA) License and may be used,
# distributed and modified only pursuant to the terms of that agreement.
# See the License for the specific language governing permissions and limitations under the
# License at https://software.nasa.gov/ .
#
# Unless required by applicable law or agreed to in writing, software distributed under the
# License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either expressed or implied.


class CtfTestError(Exception):
    pass


class CtfConditionError(CtfTestError):
    def __init__(self, message, test_condition):
        super().__init__(message)
        self.condition = test_condition


class CtfParameterError(CtfTestError):
    def __init__(self, message, parameter):
        super().__init__(message)
        self.parameter = parameter