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

from __future__ import annotations

import typing as t
from contextlib import contextmanager

from .server import _Server
from .request import _BaseRequestAccessor

if t.TYPE_CHECKING:
    from ...gui import Gui


class _FastAPIServer(_Server):
    type = "fastapi"
    server_base_class = None

    def __init__(
        self,
        gui: "Gui",
        server: t.Optional[t.Any] = None,
        path_mapping: t.Optional[dict] = None,
        **kwargs,
    ):
        self.request = _BaseRequestAccessor()
        self._gui = gui
        self._server = server
        self.__path_mapping = path_mapping or {}
        self._is_running = False
        self._host = "127.0.0.1"
        self._port = 5000

    def get_server_instance(self):
        return self._server

    def get_app_context(self) -> t.Any:
        return None

    def get_port(self) -> int:
        return self._port

    def send_ws_message(self, *args, **kwargs):
        pass

    def direct_render_json(self, data):
        return data

    def save_uploaded_file(self, file, path):
        pass

    def send_file(self, *args, **kwargs):
        pass

    def send_from_directory(self, *args, **kwargs):
        pass

    def has_server_context(self):
        return False

    def is_running_from_reloader(self):
        return False

    def register_routes(self, styles: t.List[str], scripts: t.List[str]):
        pass

    def _get_default_handler(
        self,
        static_folder: str,
        template_folder: str,
        title: str,
        favicon: str,
        root_margin: str,
        scripts: t.List[str],
        styles: t.List[str],
        version: str,
        client_config: t.Dict[str, t.Any],
        watermark: t.Optional[str],
        css_vars: str,
        base_url: str,
    ):
        return None

    def test_client(self):
        return None

    @contextmanager
    def test_request_context(self, path, data):
        yield None

    def create_http_response(
        self, message: str, status_code: int = 200, headers: t.Optional[t.Dict[str, t.Any]] = None
    ):
        return None

    def run(
        self,
        host,
        port,
        client_url,
        debug,
        use_reloader,
        server_log,
        run_in_thread,
        allow_unsafe_werkzeug,
        notebook_proxy,
        port_auto_ranges,
    ):
        self._host = host
        self._port = port
        self._is_running = True

    def is_running(self):
        return self._is_running

    def stop_thread(self):
        self._is_running = False
