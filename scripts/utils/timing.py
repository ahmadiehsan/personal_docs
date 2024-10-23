from datetime import UTC, datetime

STANDARD_TIME_FORMAT = "%Y-%m-%d__%H-%M-%S-%f"


def now_formatted() -> str:
    return datetime.now(tz=UTC).strftime(STANDARD_TIME_FORMAT)
