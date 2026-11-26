# Copyright 2021-2025 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import os
import shutil
import subprocess


def initialize_as_git_project(project_dir: str) -> str:
    if shutil.which("git") is None:
        msg = "\nERROR: Git executable not found, skipping git initialisation"
        return msg

    try:
        subprocess.run(
            ["git", "init", "."],
            cwd=project_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        msg = f"\nInitialized Git repository in {project_dir}"

    except subprocess.CalledProcessError:
        msg = f"\nERROR: Failed to initialise Git repository in {project_dir}"

    return msg


# Use TOML config file or not


def perform_post_gen_actions(
    project_dir: str = None,
    use_toml_config: str = "{{ cookiecutter.__use_toml_config }}",
    git_choice: str = "{{ cookiecutter.__git }}",
    main_file: str = "{{cookiecutter.__main_file}}",
) -> None:
    """Perform post-generation filesystem and git initialisation safely.

    This function avoids performing any actions at import-time. If template
    placeholders are still present (e.g. "{{ ... }}"), the function will
    be a no-op to prevent accidental side effects during import or tests.
    """
    if project_dir is None:
        project_dir = os.getcwd()

    # If cookiecutter placeholders were not rendered, skip any side effects
    placeholders = ("{{", "}}")
    if (
        any(p in use_toml_config for p in placeholders)
        or any(p in git_choice for p in placeholders)
        or any(p in main_file for p in placeholders)
    ):
        return

    use = use_toml_config.upper().strip()
    if use in ("YES", "Y"):
        try:
            os.remove(os.path.join(project_dir, "config", "config.py"))
        except FileNotFoundError:
            pass
        try:
            os.rename(
                os.path.join(project_dir, "config", "config_with_toml.py"),
                os.path.join(project_dir, "config", "config.py"),
            )
        except FileNotFoundError:
            pass
    else:
        for fname in ("config_with_toml.py", "config.toml"):
            try:
                os.remove(os.path.join(project_dir, "config", fname))
            except FileNotFoundError:
                pass

    git_init_message = ""
    if git_choice.upper().strip() in ("YES", "Y"):
        git_init_message = initialize_as_git_project(project_dir)
    else:
        try:
            os.remove(os.path.join(project_dir, ".gitignore"))
        except FileNotFoundError:
            pass

    main_file_name = f"{main_file}.py"

    print(
        f"New Taipy application has been created at {project_dir}"
        f"{git_init_message}"
        f"\n\nTo start the application, change directory to the newly created folder:"
        f"\n\tcd {project_dir}"
        f"\nand run the application as follows:"
        f"\n\ttaipy run {main_file_name}"
    )
