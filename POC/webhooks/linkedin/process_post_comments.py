import json

post_comments = {
    "paging": {
        "start": 0,
        "count": 10,
        "links": [],
        "total": 2
    },
    "elements": [
        {
            "actor": "urn:li:person:zLqTygBP8S",
            "commentsSummary": {
                "selectedComments": [
                    "urn:li:comment:(urn:li:activity:7095684521727016961,7095697728675995648)",
                    "urn:li:comment:(urn:li:activity:7095684521727016961,7095685305311068160)"
                ],
                "totalFirstLevelComments": 2,
                "aggregatedTotalComments": 2
            },
            "created": {
                "actor": "urn:li:person:zLqTygBP8S",
                "time": 1691743122924
            },
            "lastModified": {
                "actor": "urn:li:person:zLqTygBP8S",
                "time": 1691743122924
            },
            "id": "7095684947448897536",
            "$URN": "urn:li:comment:(urn:li:activity:7095684521727016961,7095684947448897536)",
            "message": {
                "attributes": [],
                "text": "User Test Comment 004"
            },
            "likesSummary": {
                "selectedLikes": [
                    "urn:li:like:(urn:li:person:4I4z9VlyZG,urn:li:comment:(urn:li:activity:7095684521727016961,7095684947448897536))",
                    "urn:li:like:(urn:li:person:zLqTygBP8S,urn:li:comment:(urn:li:activity:7095684521727016961,7095684947448897536))"
                ],
                "aggregatedTotalLikes": 2,
                "likedByCurrentUser": "True",
                "totalLikes": 2
            },
            "object": "urn:li:activity:7095684521727016961"
        },
        {
            "actor": "urn:li:organization:96072893",
            "commentsSummary": {
                "selectedComments": [
                    "urn:li:comment:(urn:li:activity:7095684521727016961,7095697841515298817)",
                    "urn:li:comment:(urn:li:activity:7095684521727016961,7095684701721436160)"
                ],
                "totalFirstLevelComments": 2,
                "aggregatedTotalComments": 2
            },
            "created": {
                "actor": "urn:li:organization:96072893",
                "impersonator": "urn:li:person:zLqTygBP8S",
                "time": 1691743043936
            },
            "lastModified": {
                "actor": "urn:li:organization:96072893",
                "impersonator": "urn:li:person:zLqTygBP8S",
                "time": 1691743043936
            },
            "id": "7095684616149176322",
            "$URN": "urn:li:comment:(urn:li:activity:7095684521727016961,7095684616149176322)",
            "message": {
                "attributes": [],
                "text": "Admin Test Comment 004"
            },
            "object": "urn:li:activity:7095684521727016961"
        }
    ]
}

if __name__ == '__main__':

    main_comments = post_comments.get('elements')

    for main_comment in main_comments:

        nested_comments = main_comment.get('commentsSummary').get('selectedComments')

        comment_creation_info = main_comment.get('created')
        comment_creator = comment_creation_info.get('actor')
        creation_time = comment_creation_info.get('time')

        comment_modify_info = main_comment.get('lastModified')
        comment_updator = comment_modify_info.get('actor')
        comment_update_time = comment_modify_info.get('time')

        comment_id = main_comment.get('id')
        comment_urn = main_comment.get('$URN')

        comment_details = main_comment.get('message')
        comment_attributes = comment_details.get('attributes')
        comment_text = comment_details.get('text')

        comment_likes_details = main_comment.get('likesSummary')

        if comment_likes_details:
            comment_likes = comment_likes_details.get('selectedLikes')
            comment_likes_count = comment_likes_details.get('totalLikes')
        else:
            comment_likes = []
            comment_likes_count = 0

        comment_source_activity = main_comment.get('object')

        print(f"Comment ID: {comment_id}")
        print(f"Comment URN: {comment_urn}")
        print(f"Comment Creator: {comment_creator}")
        print(f"Creation Time: {creation_time}")
        print(f"Comment Updator: {comment_updator}")
        print(f"Update Time: {comment_update_time}")
        print(f"Comment Text: {comment_text}")
        print(f"Comment Likes: {comment_likes}")
        print(f"Total Likes: {comment_likes_count}")
        print(f"Comment Source Activity: {comment_source_activity}")
        print("=" * 30)
