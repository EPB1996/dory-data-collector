from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar("T")


def to_camel(snake_str: str) -> str:
    words = snake_str.split("_")
    return words[0] + "".join(w.title() for w in words[1:])


class Page(BaseModel, Generic[T]):
    items: list[T]
    total: int

    class ConfigDict:
        alias_generator = to_camel
        populate_by_name = True