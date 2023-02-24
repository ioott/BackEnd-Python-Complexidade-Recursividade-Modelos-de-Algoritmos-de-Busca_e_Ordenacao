from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    test_message = "testmessage"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(test_message, "key")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 1)

    not_in_range = encrypt_message(test_message, 15)
    assert not_in_range == "egassemtset"

    key_is_odd = encrypt_message(test_message, 5)
    assert key_is_odd == "mtset_egasse"

    key_is_pair = encrypt_message(test_message, 4)
    assert key_is_pair == "egassem_tset"
