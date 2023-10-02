if __name__ == "__main__":
    notification = {
      "subscriber": "urn:li:person:zLqTygBP8S",
      "lastModifiedAt": 1691574506310,
      "decoratedSourcePost": {
        "owner": "urn:li:organization:96072893",
        "mediaCategory": "NONE",
        "text": "This is my post 0008",
        "entity": "urn:li:share:7094637247487995904"
      },
      "sourcePost": "urn:li:activity:7094637247890620418",
      "decoratedGeneratedActivity": {
        "comment": {
          "owner": "urn:li:person:zLqTygBP8S",
          "text": "Commenting as Sumit Butola...",
          "entity": "urn:li:comment:(urn:li:activity:7094637247890620418,7094977717598625792)",
          "object": "urn:li:activity:7094637247890620418"
        }
      },
      "action": "COMMENT",
      "notificationId": 5603453321,
      "organizationalEntity": "urn:li:organization:96072893",
      "generatedActivity": "urn:li:comment:(activity:7094637247890620418,7094977717598625792)"
    }

    action = notification.get('action')

    if action in ["ADMIN_COMMENT", "COMMENT"]:
        notification_id = notification.get('notificationId')
        action_time = notification.get('lastModifiedAt')
        organizational_entity_id = notification.get('organizationalEntity')
        generated_activity_id = notification.get('generatedActivity')

        event_source_post_id = notification.get('sourcePost')

        event_source_post = notification.get('decoratedSourcePost')
        event_source_post_owner_id = event_source_post.get('owner')
        event_source_post_text = event_source_post.get('text')
        event_source_post_mediatype = event_source_post.get('mediaCategory')
        event_source_post_entity_id = event_source_post.get('entity')

        event_comment = notification.get('decoratedGeneratedActivity').get('comment')
        event_comment_owner_id = event_comment.get('owner')
        event_comment_text = event_comment.get('text')
        event_comment_id = event_comment.get('entity')
        event_comment_parent_object = event_comment.get('object')

    elif action == "LIKE":
        notification_id = notification.get('notificationId')
        action_time = notification.get('lastModifiedAt')
        organizational_entity_id = notification.get('organizationalEntity')
        generated_activity_id = notification.get('generatedActivity')

        event_source_post_id = notification.get('sourcePost')

        event_source_post = notification.get('decoratedSourcePost')
        event_source_post_owner_id = event_source_post.get('owner')
        event_source_post_text = event_source_post.get('text')
        event_source_post_mediatype = event_source_post.get('mediaCategory')
        event_source_post_entity_id = event_source_post.get('entity')

    elif action == 'SHARE':
        notification_id = notification.get('notificationId')
        action_time = notification.get('lastModifiedAt')
        organizational_entity_id = notification.get('organizationalEntity')
        generated_activity_id = notification.get('generatedActivity')

        event_source_post_id = notification.get('sourcePost')

        event_source_post = notification.get('decoratedSourcePost')
        event_source_post_owner_id = event_source_post.get('owner')
        event_source_post_text = event_source_post.get('text')
        event_source_post_mediatype = event_source_post.get('mediaCategory')
        event_source_post_entity_id = event_source_post.get('entity')

        event_share = notification.get('decoratedGeneratedActivity').get('comment')
        event_share_owner_id = event_share.get('owner')
        event_share_text = event_share.get('text')
        event_share_id = event_share.get('entity')
        event_share_parent_object = event_share.get('object')








