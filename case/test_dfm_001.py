from method.dde_dock_method import DdeDockMethod
from method.dde_file_manager_method import DdeFileManagerMethod
from case.base_case import BaseCase


class TestDfm(BaseCase):

    def test_dfm_001(self):
        """任务栏启动文管"""
        DdeDockMethod().click_dde_file_manager_on_dock_by_attr()
        DdeFileManagerMethod().click_desktop_dir_in_left_view_by_attr()
        self.assert
