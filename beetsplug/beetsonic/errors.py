"""
This file contains the error codes and default error messages returned by the
Subsonic server.
"""
GENERIC_ERROR_CODE = 0
REQUIRED_PARAMETER_ERROR_CODE = 10
CLIENT_UPGRADE_ERROR_CODE = 20
SERVER_UPGRADE_ERROR_CODE = 30
AUTHENTICATION_ERROR_CODE = 40
LDAP_TOKEN_NOT_SUPPORTED_ERROR_CODE = 41
USER_NOT_AUTHORIZED_ERROR_CODE = 50
PREMIUM_TRIAL_OVER_ERROR_CODE = 60
DATA_NOT_FOUND_ERROR_CODE = 70

GENERIC_ERROR_MSG = u'An unexpected error has occured'
REQUIRED_PARAMETER_ERROR_MSG = u'Required parameter is missing'
CLIENT_UPGRADE_ERROR_MSG = u'Incompatible Subsonic REST protocol version. ' + \
                           u'Client must upgrade.'
SERVER_UPGRADE_ERROR_MSG = u'Incompatible Subsonic REST protocol version. ' + \
                           u'Server must upgrade.'
AUTHENTICATION_ERROR_MSG = u'Authentication information is incorrect'
LDAP_TOKEN_NOT_SUPPORTED_ERROR_MSG = u'Token authentication not supported ' + \
                                     u'for LDAP users.'
USER_NOT_AUTHORIZED_ERROR_MSG = u'User is not authorized for the ' + \
                                u'given operation.'
PREMIUM_TRIAL_OVER_ERROR_MSG = u'Hell has frozen over and beetsonic is ' + \
                               u'premium only'
DATA_NOT_FOUND_ERROR_MSG = u'The requested data was not found.'
