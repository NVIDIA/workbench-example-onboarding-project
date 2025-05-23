# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for auto continuing associated tasks."""
from typing import Any
from pathlib import Path
import sys

try:
    from common import testing
    from common import wb_svc_client
except ImportError:
    # this helps with debugging and allows direct importing or execution
    sys.path.append("..")
    from common import testing
    from common import wb_svc_client


PROJECT_NAME = "nvidia-ai-workbench-onboarding"
ROOT_DIR = "/"
PROJECT_DIR = "/project"
FOLDER_NAME = "my-first-folder"
FILE_NAME = "delete-me.txt"
CODE_FOLDER_NAME = "code"
DELETE_ME_FILE_NAME = "delete-me.txt"

UBUNTU_PACKAGE = "jq"

def check_folder_exists() -> dict[str, Any]:
    """Ensure the folder is created."""
    _ = testing.get_folder(PROJECT_NAME, ROOT_DIR, FOLDER_NAME)



def check_file_in_folder() -> dict[str, Any]:
    """Check if any file exists in my-first-folder."""
    import os
    
    folder_path = os.path.join(PROJECT_DIR, FOLDER_NAME)
    # Check for any non-hidden file
    for filename in os.listdir(folder_path):
        if not filename.startswith('.'):
            return None  # Found at least one non-hidden file
            
    raise testing.TestFail("info_wait_for_file_upload")
    
    # Don't return anything, just like other test functions

def check_file_deleted() -> dict[str, Any]:
    """Check if the file is deleted."""
    import os
    
    folder_path = os.path.join(PROJECT_DIR, CODE_FOLDER_NAME)
    
    # Check if delete-me.txt still exists
    if os.path.exists(os.path.join(folder_path, DELETE_ME_FILE_NAME)):
        raise testing.TestFail("info_wait_for_delete")
            
    return None

def check_file_changed() -> dict[str, Any]:
    """Check if example-file.txt has been modified."""
    import os
    
    file_path = os.path.join(PROJECT_DIR, CODE_FOLDER_NAME, "example-file.txt")
    
    # Read the file contents
    with open(file_path, 'r') as f:
        content = f.read().strip()
    
    # Check if content is different from original
    if content == "this is an example":
        raise testing.TestFail("info_wait_for_edit")
            
    return None
    

def add_ubuntu_package():
    """Wait for the package to be added."""
    testing.ensure_package(PROJECT_NAME, "apt", UBUNTU_PACKAGE)


def ensure_gpu_count() -> int:
    """Ensure that a project has at least one GPU assigned.

    Error message keys:
        - info_no_gpu_assigned
        - info_wait_for_project
    """
    response = wb_svc_client.get_gpu_request(PROJECT_NAME) or {}
    gpu_count = (
        response.get("data", {})
                .get("project", {})
                .get("resources", {})
                .get("gpusRequested")
    )

    if gpu_count is None:
        raise testing.TestFail("info_wait_for_project")

    if gpu_count < 1:
        raise testing.TestFail("info_no_gpu_assigned")


def check_changes_discarded() -> None:
    """Check that the user has discarded all changes to the project."""
    testing.ensure_changes_discarded(PROJECT_NAME)
