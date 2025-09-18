import pytest
from datetime import datetime
from app.models.user import User  # adjust path if needed
from app.schema.user import UserBase



def test_user_repr():
    user = User(username="ramya", email="ramya@example.com", password="secret")
    repr_str = repr(user)
    assert "ramya" in repr_str
    assert "ramya@example.com" in repr_str
    assert repr_str.startswith("<User(")


def test_user_to_dict():
    user = User(id=1, username="ramya", email="ramya@example.com", password="secret")
    result = user.to_dict()

    assert isinstance(result, UserBase)
    assert result.id == 1
    assert result.username == "ramya"
    assert result.email == "ramya@example.com"


def test_user_to_dict_with_defaults():
    user = User(username="testuser", email="test@example.com", password="12345")
    result = user.to_dict()

    # id may not be set yet, so should fallback to 0
    assert result.id == 0
    assert result.username == "testuser"
    assert result.email == "test@example.com"


def test_created_at_defaults_to_now():
    user = User(username="tim", email="tim@example.com", password="pwd123")
    assert isinstance(user.created_at, datetime)
