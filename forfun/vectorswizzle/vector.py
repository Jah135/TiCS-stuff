from typing import Any

class Vector:
    components: str

    def __repr__(self) -> str:
        args = ", ".join(str(self[component]) for component in self.components)
        return f"{self.__class__.__name__}({args})"

    def __getitem__(self, key: Any) -> Any:
        if key in self.components:
            return self.__getattribute__(key)
        raise TypeError()

    def swizzle(self, sequence: str) -> Vector:
        new_vector_size = len(sequence)
        args = []

        for char in sequence:
            if char == "_":
                args.append(0)
                continue
            
            if char not in self.components:
                raise ValueError(sequence)
            args.append(self[char])

        if new_vector_size == 2:
            return Vector2(*args)
        elif new_vector_size == 3:
            return Vector3(*args)
        elif new_vector_size == 4:
            return Vector4(*args)

        raise ValueError(f"Invalid vector swizzle size: {new_vector_size}")

class Vector2(Vector):
    components = "xy"
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

class Vector3(Vector):
    components = "xyz"
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

class Vector4(Vector):
    components = "xyzw"
    x: float
    y: float
    z: float
    w: float

    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

vec = Vector2(1, 10)
print(vec.swizzle("xy___"))
