# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

setuptools.setup(
    name='megalista_dataflow',
    version='5',
    author='Google',
    author_email='megalista-admin@google.com',
    url='https://github.com/google/megalista/',
    install_requires=['google-ads==25.1.0',
                      'google-api-python-client==2.154.0',
                      'google-cloud-bigquery==3.27.0',
                      'aiohttp==3.11.7',
                      'google-cloud-storage==2.18.2',
                      'google-cloud-firestore==2.19.0',
                      'pandas==2.2.2',
                      'boto3==1.35.12',
                      'tadau==1.0.7'],
    packages=setuptools.find_packages(),
)