# Safe version: no hardcoded secret is stored in the source code.
# The value should come from an environment variable or GitHub Secret.

import os


AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

# NOMADPAY-12345678
# NOMADPAY-87654321
# NOMADPAY-11223344
# NOMAD-12345678
# NOMADPAY-1234567
# NOMADPAY-123456789
