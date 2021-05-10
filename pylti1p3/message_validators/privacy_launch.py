from ..exception import LtiException
from .resource_message import ResourceMessageValidator


class PrivacyLaunchValidator(ResourceMessageValidator):
    """Validates the body of a LTI data privacy launch.

    The launch must omit the context claim, and include
    a for_user claim specifying the user that the launch
    was made on behalf of.
    """

    def validate(self, jwt_body):
        super(PrivacyLaunchValidator, self).validate(jwt_body)

        if 'https://purl.imsglobal.org/spec/lti/claim/context' in jwt_body:
            raise LtiException('Context claim must be omitted from a DataPrivacyLaunchRequest')

        for_user_claim = jwt_body.get('https://purl.imsglobal.org/spec/lti/claim/for_user')
        if for_user_claim is None:
            raise LtiException('For user claim must be included in a DataPrivacyLaunchRequest')

        return True

    def can_validate(self, jwt_body):
        return jwt_body.get('https://purl.imsglobal.org/spec/lti/claim/message_type') == 'DataPrivacyLaunchRequest'
