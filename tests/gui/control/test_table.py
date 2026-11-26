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

import inspect

from taipy.gui import Gui


def test_table_md_1(gui: Gui, helpers, csvdata):
    md_string = "<|{csvdata}|table|page_size=10|page_size_options=10;30;100|columns=Day;Entity;Code;Daily hospital occupancy|date_format=eee dd MMM yyyy|>"  # noqa: E501
    expected_list = [
        "<Table",
        'defaultColumns="',
        'height="80vh"',
        'width="100%"',
        'pageSizeOptions="[',
        'pageSize="',
    ]
    gui._set_frame(inspect.currentframe())
    helpers.test_control_md(gui, md_string, expected_list)


def test_table_reset_md(gui: Gui, helpers, csvdata):
    md_string = "<|{csvdata}|table|rebuild|page_size=10|page_size_options=10;30;100|columns=Day;Entity;Code;Daily hospital occupancy|date_format=eee dd MMM yyyy|>"  # noqa: E501
    expected_list = [
        "<Table",
        'defaultColumns="',
        'height="80vh"',
        'width="100%"',
        'pageSizeOptions="[',
        'pageSize="',
        'columns="',
    ]
    gui._set_frame(inspect.currentframe())
    helpers.test_control_md(gui, md_string, expected_list)


def test_table_md_2(gui: Gui, helpers, csvdata):
    table_properties = {  # noqa: F841
        "page_size": 10,
        "page_size_options": [10, 50, 100, 500],
        "allow_all_rows": True,
        "columns": {
            "Day": {"index": 0, "format": "dd/MM/yyyy", "title": "Date of measure"},
            "Entity": {"index": 1},
            "Code": {"index": 2},
            "Daily hospital occupancy": {"index": 3},
        },
        "date_format": "eee dd MMM yyyy",
        "number_format": "%.3f",
        "width": "60vw",
        "height": "60vh",
    }
    md_string = "<|{csvdata}|table|properties=table_properties|auto_loading|editable|>"
    expected_list = [
        "<Table",
        'allowAllRows="{!true',
        'autoLoading="{!true',
        'editable="{!true',
        'onEdit="__gui.table_on_edit',
        'onDelete="__gui.table_on_delete',
        'onAdd="__gui.table_on_add',
        'defaultColumns="',
        'height="60vh"',
        'width="60vw"',
        'pageSizeOptions="[',
        'pageSize="',
    ]
    gui._set_frame(inspect.currentframe())
    helpers.test_control_md(gui, md_string, expected_list)


def test_table_html_1(gui: Gui, helpers, csvdata):
    html_string = '<taipy:table data="{csvdata}" page_size="10" page_size_options="10;30;100" columns="Day;Entity;Code;Daily hospital occupancy" date_format="eee dd MMM yyyy" />'  # noqa: E501
    expected_list = [
        "<Table",
        'defaultColumns="',
        'height="80vh"',
        'width="100%"',
        'pageSizeOptions="[',
        'pageSize="',
    ]
    gui._set_frame(inspect.currentframe())
    helpers.test_control_html(gui, html_string, expected_list)


def test_table_html_2(gui: Gui, helpers, csvdata):
    table_properties = {  # noqa: F841
        "page_size": 10,
        "page_size_options": [10, 50, 100, 500],
        "allow_all_rows": True,
        "columns": {
            "Day": {"index": 0, "format": "dd/MM/yyyy", "title": "Date of measure"},
            "Entity": {"index": 1},
            "Code": {"index": 2},
            "Daily hospital occupancy": {"index": 3},
        },
        "date_format": "eee dd MMM yyyy",
        "number_format": "%.3f",
        "width": "60vw",
        "height": "60vh",
    }
    html_string = '<taipy:table data="{csvdata}" properties="table_properties" auto_loading="True" show_all="True" />'
    expected_list = [
        "<Table",
        'allowAllRows="{!true',
        'autoLoading="{!true',
        'showAll="{!true',
        'defaultColumns="',
        'height="60vh"',
        'width="60vw"',
        'pageSizeOptions="[',
        'pageSize="',
    ]
    gui._set_frame(inspect.currentframe())
    helpers.test_control_html(gui, html_string, expected_list)
