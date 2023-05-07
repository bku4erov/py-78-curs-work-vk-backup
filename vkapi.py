import json
from datetime import datetime
from pprint import pprint

import requests


class VkApi:
    
    url = 'https://api.vk.com/method/'
    
    def __init__(self, token, version = '5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }
    
    def get_photos(self, user_id):
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': user_id,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1
        }
        req = requests.get(photos_url, params={**self.params, **photos_params}).json()
        return req
    
    def save_photos_to_yadisk(self, user_id, count=5):
        # get photos from VK by user_id
        photos = self.get_photos(user_id)
        # with open('photos.json', 'rt') as json_file:
        #     photos = json.load(json_file)

        # get list of user profile's photos (count=5 first photos)
        photos_list = photos['response']['items'][:min(count, photos['response']['count'])]
        
        # find number of likes which several (more than one) photos have
        likes_cnt_list = [photo["likes"]["count"] for photo in photos_list]
        dup_likes_cnt = set(likes_cnt for likes_cnt in likes_cnt_list if likes_cnt_list.count(likes_cnt) > 1)
        
        photos_info = []
        for photo in photos_list:
            # generate file name using likes count and photo upload date
            likes_count = photo["likes"]["count"]
            if likes_count in dup_likes_cnt:
                file_name = f'{likes_count} {datetime.fromtimestamp(photo["date"])}.jpg'
            else:
                file_name = f'{likes_count}.jpg'
            
            # get type of photo's max size
            size = photo['sizes'][-1]['type']

            # add information about photo to output json-file
            photos_info.append({'file_name': file_name, 'size': size})
            # print(file_name, size)
        
        pprint(photos_info)
