# import pytest
# from base_classes.qase_integration import QaseMethods
# from datetime import datetime
# import datetime
# import os


# @pytest.fixture(scope='session')
# def qase_run_id():
#     """
#         The fixture create new test run on the platform QASE, which depends on specific test plan id.
#         Returns id of created test run.
#     """
#     qase_run = QaseMethods()
#     test_run = qase_run.create_test_run(test_plan_id=1)
#     return test_run


# @pytest.fixture(scope='function')
# def get_start_time():
#     start_time = datetime.datetime.now()
#     time_part = str(start_time).split()[1]
#     time_without_ms = time_part.split('.')[0]
#     hours, minutes, seconds = map(int, time_without_ms.split(':'))
#     total_seconds = hours * 3600 + minutes * 60 + seconds
#     yield total_seconds


# @pytest.fixture(scope='session', autouse=True)
# def send_test_run(qase_run_id):
#     qase_run = QaseMethods()
#     start_hours = datetime.datetime.now()
#     yield
#     url = qase_run.update_publicity_specific_run(qase_run_id)
#     end_hours = datetime.datetime.now()
#     result = end_hours - start_hours
#     trimmed_time = str(result).split('.')[0]
#     # debug_channel = "#qa-qase-results-debug"
#     release_channel = "#qa-qase-results-release"
#     qase_run.send_run_to_slack(slack_channel=release_channel, public_test_run_url=url, test_time=trimmed_time)































































