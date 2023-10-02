import facebook

if __name__ == '__main__':
    graph = facebook.GraphAPI(access_token="EAAathGdn1gcBAOYwyDGQyuFWqZCpfayZCm2lU00127pJ8YEPGc8tfQS8rQ9LmSAy97uUK0eGAwDDdqznH5gQDuD851zZAhrx4e7kegctTRHjMrfQC5HT6A6j9IHHe9M622svHUX7qs0DhCZBfDmZARX4TKE71wl8HW9gUsLGW5aOHO7jTHHcW", version="3.1")

    image_path = '/home/sumit/Desktop/postManagementService/DataNext/src/python/social/socialHubIntegrationService/multimedia/image.jpg'

    response = graph.put_photo(image=open(image_path, 'rb'),
                               message='Look at this cool photo!')
    print(response)
