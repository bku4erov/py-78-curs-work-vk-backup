import json
import os
from pprint import pprint

from vkapi import VkApi

CONFIG_FILENAME = 'config.txt'

if __name__ == '__main__':
    vk_token = None
    ya_disk_token = None
    if os.path.exists(CONFIG_FILENAME):
        try:
            with open(CONFIG_FILENAME, 'rt') as config_file:
                config = json.load(config_file)
                vk_token = config['vk token']
                # ya_disk_token = config['yandex disk token']
        except Exception as config_err:
            print('Error while reading config file:')
            print(type(config_err))
            print(config_err)
            print()
            
    else:
        print('Config file not found.')
    
    if vk_token is None:
        print('Load VK token from config file failed.')
        vk_token = input('Please, input VK token value: ')
    
    # # if ya_disk_token is None:
    # #     print('Load Yandex.Disk token from config file failed.')
    # #     ya_disk_token = input('Please, input Yandex.Disk token value: ')

    # print(f'VK token: {vk_token}')
    # # print(f'Yandex.Disk token: {ya_disk_token}')

    user_vk_api = VkApi(vk_token)
    # photos = user_vk_api.get_photos(1)

    # pprint(photos)

    # json_obj_photos = json.dumps(photos, indent=4)

    # with open("photos.json", "w") as outfile:
    #     outfile.write(json_obj_photos)

    user_vk_api.save_photos_to_yadisk(user_id=1)
