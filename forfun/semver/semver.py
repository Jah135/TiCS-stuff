class Version:
    patch: int
    minor: int
    major: int

    @classmethod
    def from_string(cls, version_str: str) -> Version:
        segments = version_str.split(".")

        return cls(int(segments[0]), int(segments[1]), int(segments[2]))

    def __str__(self) -> str:
        return f"v{self.major}.{self.minor}.{self.patch}"

    def __init__(self, major: int, minor: int, patch: int) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Version):
            return False
        return (
            value.major == self.major
            and value.minor == self.minor
            and value.patch == self.patch
        )

    def __lt__(self, other: Version) -> bool:
        if other.major > self.major:
            return True
        if other.major < self.major:
            return False

        if other.minor > self.minor:
            return True
        if other.minor < self.minor:
            return False

        if other.patch > self.patch:
            return True
        if other.patch < self.patch:
            return False

        return False

    def __le__(self, other: Version) -> bool:
        return self < other or self == other


older_version = Version(0, 0, 10)
newer_version = Version.from_string("1.1.1")

print(older_version < newer_version)
