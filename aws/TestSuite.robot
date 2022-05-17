*** Variables ***
${BUCKET_NAME}  PUT_YOUR_BUCKET_NAME_HERE


*** Settings ***
Resource          keywords.resource
Default Tags      s3


*** Test Cases ***
Is Bucket Encrypted
    Verify Bucket Encrypted      ${BUCKET_NAME}

Is Tag Key Source In Bucket
    Check Tag Key Presence      ${BUCKET_NAME}      source

Is Bucket Size Less Than
    Verify Bucket Size Is Less Than     ${BUCKET_NAME}    1