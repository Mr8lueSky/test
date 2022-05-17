*** Settings ***
Library     TestS3Library.py

*** Keywords ***
Verify Bucket Encrypted
    [Arguments]             ${bucket_name}
    ${encryptions}=     Get Bucket Encryption Types     ${bucket_name}
    Should Not Be Empty     ${encryptions}


Check Tag Key Presence
    [Arguments]     ${bucket_name}      ${tag_key}
    ${tags}=        Get Bucket Tags     ${bucket_name}
    ${tags_keys}    Evaluate    [tag['Key'] for tag in $tags]
    Run Keyword If  $tag_key in $tags_keys
    ...  pass execution  ${tag_key} in tags
    fail    ${tag_key} is not in tags


Verify Bucket Size Is Less Than
    [Arguments]      ${bucket_name}  ${less_than}
    ${size}=    Get Bucket Size Mb   ${bucket_name}
    Run Keyword If  $size < ${less_than}
    ...  pass execution  ${size} is less than ${less_than}
    fail    ${size} is greater than ${less_than}

