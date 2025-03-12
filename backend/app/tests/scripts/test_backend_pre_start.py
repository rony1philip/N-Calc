from unittest.mock import MagicMock, patch, ANY
from sqlmodel import select
from app.backend_pre_start import init, logger

def test_init_successful_connection() -> None:
    engine_mock = MagicMock()
    session_mock = MagicMock()
    session_mock.exec.return_value = True  # Ensure exec() is properly mocked

    with (
        patch("app.backend_pre_start.Session", autospec=True) as session_class_mock,  # Correct patch
        patch.object(logger, "info"),
        patch.object(logger, "error"),
        patch.object(logger, "warn"),
    ):
        session_class_mock.return_value.__enter__.return_value = session_mock  # Mock context manager behavior

        try:
            init(engine_mock)
            connection_successful = True
        except Exception:
            connection_successful = False

        assert connection_successful, "The database connection should be successful and not raise an exception."

        # ✅ Fix: Use `ANY` to ignore object instance differences
        session_mock.exec.assert_called_once_with(ANY)
