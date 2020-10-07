#!/bin/bash
# Copyright 2019 Google LLC
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


if [ $# != 3 ]; then
    echo "Usage: $0 gcp_project_id bucket_name region"
    exit 1
fi

cd megalist_dataflow
gcloud config set project $1
python3 -m pip install --user -q -r requirements.txt
python3 -m main --runner DataflowRunner --project $1 --gcp_project_id $1 --temp_location gs://$2/tmp/ --region $3 --setup_file ./setup.py --template_location gs://$2/templates/megalist --num_workers 1 --autoscaling_algorithm=NONE
gsutil cp megalist_metadata gs://$2/templates/megalist_metadata
cd ..