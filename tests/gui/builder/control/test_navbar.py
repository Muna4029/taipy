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

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from taipy.gui import Gui
else:
    Gui = object  # type: ignore
# taipy.gui.builder will be imported lazily in tests to avoid import-time dependency failures
tgb = None


def test_navbar_builder(gui: Gui, test_client, helpers):
    import importlib

    global tgb
    if tgb is None:
        tgb = importlib.import_module("taipy.gui.builder")
    # Avoid using private API gui._bind_var_val to prevent runtime broadcast side-effects
    lov = [
        ("/page1", "Page 1"),
        ("/page2", "Page 2"),
        ("/page3", "Page 3"),
        ("/page4", "Page 4"),
    ]
    with tgb.Page(frame=None) as page:
        # Use a literal lov when building the control to avoid binding and unstable internals
        tgb.navbar(lov=lov)
    expected_list = [
        "<NavBar",
        "lov=",
        "/page1",
    ]
    helpers.test_control_builder(gui, page, expected_list)
