from challenge import transform, params
import submission
from hypothesis import given

# Pytest discovers all Classes and methods which start with test by default
# Having the test function inside a class which is not discovered by pytest makes it more difficult to execute
# Testing the user submission could be done with:
# $ py.test RenameColumn/test.py::TestSubmission

# The testing of the transform function should be decoupled from generating examples in my opinition, Since those are two very different use cases
# Testing the transform function could be done with:
# $ py.test RenameColumn/test.py::TestTransform

# In this class the Static tests which validate the transform function could be written
class TestTransform:
    def test_schmest(self):
        assert True


import submission
# Here all the Tests for the User Submitted Code could be written
class TestSubmission:
    @given(df = params.df)
    def test_rename_columns(self, df):
        expected_df = transform(df)
        user_df = submission.rename_column(df)
        assert tm.assert_frame_equal(user_df, expected_df)

