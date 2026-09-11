class Context:
    directories: dict[str, Context]

    def key(self, name: str) -> Context:
        return self.directories.setdefault(name, Context())
