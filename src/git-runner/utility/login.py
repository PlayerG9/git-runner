#!/usr/bin/python3
# -*- coding=utf-8 -*-
r"""

"""
import spwd
import crypt
import hmac
import utility


class LoginError(Exception):
    pass


def verify_login(username, password):
    """Tries to authenticate a user.
    Returns True if the authentication succeeds"""
    try:
        enc_pwd = spwd.getspnam(username)[1]
        if enc_pwd in ["NP", "!", "", None]:
            # no password set
            raise LoginError("user is not available for login")
        if enc_pwd in ["LK", "*"]:
            # account is locked
            raise LoginError("user is not available for login")
        if enc_pwd == "!!":
            # password has expired
            raise LoginError("user is not available for login")
        # Encryption happens here, the hash is stripped from the
        # enc_pwd and the algorithm id and salt are used to encrypt
        # the password.
        if crypt.crypt(password, enc_pwd) == enc_pwd:
            return True
        else:
            # incorrect password
            raise LoginError("password is incorrect")
    except PermissionError:
        # server is not started with sudo/root
        # thus not able to verify user and password
        fallback_auth = utility.getConfig('fallback-auth', default={})
        return (
            hmac.compare_digest(username, fallback_auth.get('username', ''))
            and
            hmac.compare_digest(password, fallback_auth.get('password', ''))
        )
    except KeyError:
        # user not found
        raise LoginError("user not found")
