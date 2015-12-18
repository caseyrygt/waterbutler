import pytest

from tests.utils import async

import io
from http import client

import aiohttpretty

import logging

from waterbutler.core import streams
from waterbutler.core import exceptions
from waterbutler.core.path import WaterButlerPath

from waterbutler.providers.onedrive import OneDriveProvider
from waterbutler.providers.onedrive.settings import settings
from waterbutler.providers.onedrive.metadata import OneDriveRevision
from waterbutler.providers.onedrive.metadata import OneDriveFileMetadata
from waterbutler.providers.onedrive.metadata import OneDriveFolderMetadata

logger = logging.getLogger(__name__)

@pytest.fixture
def auth():
    return {
        'name': 'cat',
        'email': 'cat@cat.com',
    }


@pytest.fixture
def credentials():
    return {'token': 'wrote harry potter'}


@pytest.fixture
def settings():
    return {'folder': '11446498'}


@pytest.fixture
def provider(auth, credentials, settings):
    return OneDriveProvider(auth, credentials, settings)


@pytest.fixture
def file_content():
    return b'SLEEP IS FOR OSX GO SERVE STREAMS'


@pytest.fixture
def file_like(file_content):
    return io.BytesIO(file_content)


@pytest.fixture
def file_stream(file_like):
    return streams.FileStreamReader(file_like)

@pytest.fixture
def folder_object_metadata():
    return {
       "lastModifiedBy": {
    
          "user": {
    
             "thumbnails": {
    
                "source": {
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:WebReady"
    
                },
    
                "large": {
    
                   "height": 1198,
    
                   "width": 1198,
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileCroppedOriginal"
    
                },
    
                "medium": {
    
                   "height": 180,
    
                   "width": 180,
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileMedium"
    
                },
    
                "small": {
    
                   "height": 96,
    
                   "width": 96,
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileStatic"
    
                }
    
             },
    
             "id": "75bfe374ebeb1211",
    
             "displayName": "Ryan Casey"
    
          },
    
          "application": {
    
             "thumbnails": {
    
                "small": {
    
                   "height": 50,
    
                   "width": 50,
    
                   "url": "https://public-sn3302.files.1drv.com/y3atLEyz-EB17OzMbWyJzwu39hoELyHbCjb13GdM4Jeq5vEVLllH7jt4ftWt4nvvsiT5UNQJTPdirhWACyo92cbGASFxSER2MCuTQKTtVi-Yvo09ENEPhScewG0sNMEqRun?psid=1"
    
                }
    
             },
    
             "id": "4416c3d3",
    
             "displayName": "GT OSF OneDrive"
    
          }
    
       },
    
       "size": 119410,
    
       "name": "sub1-b",
    
       "fileSystemInfo": {
    
          "lastModifiedDateTime": "2015-12-07T16:45:28.46Z",
    
          "createdDateTime": "2015-11-29T17:21:09.997Z"
    
       },
    
       "folder": {
    
          "childCount": 4
    
       },
    
       "@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items/$entity",
    
       "id": "75BFE374EBEB1211!118",
    
       "createdDateTime": "2015-11-29T17:21:09.997Z",
    
       "lastModifiedDateTime": "2015-12-07T16:45:28.46Z",
    
       "parentReference": {
    
          "driveId": "75bfe374ebeb1211",
    
          "path": "/drive/root:/ryan-test1",
    
          "id": "75BFE374EBEB1211!107"
    
       },
    
       "createdBy": {
    
          "user": {
    
             "thumbnails": {
    
                "source": {
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:WebReady"
    
                },
    
                "large": {
    
                   "height": 1198,
    
                   "width": 1198,
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileCroppedOriginal"
    
                },
    
                "medium": {
    
                   "height": 180,
    
                   "width": 180,
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileMedium"
    
                },
    
                "small": {
    
                   "height": 96,
    
                   "width": 96,
    
                   "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileStatic"
    
                }
    
             },
    
             "id": "75bfe374ebeb1211",
    
             "displayName": "Ryan Casey"
    
          },
    
          "application": {
    
             "id": "44048800",
    
             "displayName": "OneDrive website"
    
          }
    
       },
    
       "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!118",
    
       "cTag": "adDo3NUJGRTM3NEVCRUIxMjExITExOC42MzU4NTEwMzUyODQ2MDAwMDA",
    
       "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExMTguMw"

    }


@pytest.fixture
def folder_list_metadata():
    return {

           "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!107",
        
           "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExMDcuMA",
        
           "fileSystemInfo": {
        
              "lastModifiedDateTime": "2015-11-22T14:33:33.57Z",
        
              "createdDateTime": "2015-11-22T14:33:33.57Z"
        
           },
           
           "children@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items('75BFE374EBEB1211%21107')/children",
        
           "id": "75BFE374EBEB1211!107",
        
           "lastModifiedDateTime": "2015-12-11T14:45:36.6Z",
        
           "size": 203146,
        
           "@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items/$entity",
        
           "createdDateTime": "2015-11-22T14:33:33.57Z",
        
           "folder": {
        
              "childCount": 3
        
           },
        
           "cTag": "adDo3NUJGRTM3NEVCRUIxMjExITEwNy42MzU4NTQ0MTkzNjYwMDAwMDA",
        
           "children": [
        
              {
        
                 "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!118",
        
                 "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExMTguMw",
        
                 "fileSystemInfo": {
        
                    "lastModifiedDateTime": "2015-12-07T16:45:28.46Z",
        
                    "createdDateTime": "2015-11-29T17:21:09.997Z"
        
                 },        
        
                 "id": "75BFE374EBEB1211!118",
        
                 "lastModifiedDateTime": "2015-12-09T01:48:52.31Z",
        
                 "size": 119410,
        
                 "createdDateTime": "2015-11-29T17:21:09.997Z",
        
                 "folder": {
        
                    "childCount": 4
        
                 },
        
                 "cTag": "adDo3NUJGRTM3NEVCRUIxMjExITExOC42MzU4NTIyMjUzMjMxMDAwMDA",
                 
                 "name": "sub1-b",
        
                 "parentReference": {
        
                    "driveId": "75bfe374ebeb1211",
        
                    "path": "/drive/root:/ryan-test1",
        
                    "id": "75BFE374EBEB1211!107"
        
                 }
        
              },
        
              {
        
                 "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!143",
        
                 "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExNDMuMTI",
        
                 "fileSystemInfo": {
        
                    "lastModifiedDateTime": "2015-12-07T17:26:09.48Z",
        
                    "createdDateTime": "2015-12-01T16:52:33.07Z"
        
                 },         
        
                 "id": "75BFE374EBEB1211!143",
        
                 "lastModifiedDateTime": "2015-12-07T17:26:09.48Z",
        
                 "size": 0,
        
                 "createdDateTime": "2015-12-01T16:52:33.07Z",
        
                 "folder": {
        
                    "childCount": 1
        
                 },
        
                 "cTag": "adDo3NUJGRTM3NEVCRUIxMjExITE0My42MzU4NTEwNTk2OTQ4MDAwMDA",         
        
                 "name": "sub1-z",
        
                 "parentReference": {
        
                    "driveId": "75bfe374ebeb1211",
        
                    "path": "/drive/root:/ryan-test1",
        
                    "id": "75BFE374EBEB1211!107"
        
                 }
        
              },
        
              {
        
                 "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!150",
        
                 "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExNTAuMTE",
        
                 "fileSystemInfo": {
        
                    "lastModifiedDateTime": "2015-12-08T21:51:15.593Z",
        
                    "createdDateTime": "2015-12-02T20:25:26.51Z"
        
                 },         
        
                 "id": "75BFE374EBEB1211!150",
        
                 "lastModifiedDateTime": "2015-12-08T21:51:15.593Z",
        
                 "photo": {
        
                    "takenDateTime": "2013-04-17T14:32:26Z"
        
                 },
        
                 "size": 83736,
        
                 "@content.downloadUrl": "https://public-ch3302.files.1drv.com/y3mgyZqUob4fS1RGIHa8w3tl0ozOlXXiKPMmz3hxZ0KbMqyZmIOnzXL8G9fWREL01mog9XRQn2g2qExRSSFce9ixl7fOlq_yjwOxX-6F2CNzgp3-wE9oThZSrvTix8h7cMD32RHd-__uwGK6Db0ErsGuxorWJKfRlmkpJFn7b8F9ZVvsIsLOmJWVKMyxrQMfves",
        
                 "cTag": "aYzo3NUJGRTM3NEVCRUIxMjExITE1MC4yNTc",
        
                 "image": {
        
                    "width": 883,
        
                    "height": 431
        
                 },
        
                 "file": {
        
                    "mimeType": "image/jpeg",
        
                    "hashes": {
        
                       "crc32Hash": "6D98C9D5",
        
                       "sha1Hash": "68A4192BF9DEAD103D7E4EA481074745932989F4"
        
                    }
        
                 },         
        
                 "name": "elect-a.jpg",
        
                 "parentReference": {
        
                    "driveId": "75bfe374ebeb1211",
        
                    "path": "/drive/root:/ryan-test1",
        
                    "id": "75BFE374EBEB1211!107"
        
                 },
        
                 "createdDateTime": "2015-12-02T20:25:26.51Z"
        
              }
        
           ],   
        
           "name": "ryan-test1",
        
           "parentReference": {
        
              "driveId": "75bfe374ebeb1211",
        
              "path": "/drive/root:",
        
              "id": "75BFE374EBEB1211!103"
        
           }
        
    }

@pytest.fixture
def file_root_parent_metadata2():
    return {
           "id": "75BFE374EBEB1211!128",
           "cTag": "adDo3NUJGRTM3NEVCRUIxMjExITEyOC42MzU4NTYxODI2MDA5MzAwMDA",
           "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExMjguMA",
           "size": 998322,
           "name": "sub1",
           "parentReference": {
              "id": "75BFE374EBEB1211!103",
              "path": "/drive/root:",
              "driveId": "75bfe374ebeb1211"
           },
           "@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items/$entity",
           "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!128",
           "folder": {
              "childCount": 3
           }
    }

@pytest.fixture
def file_root_parent_metadata():
    return {
           "id": "75BFE374EBEB1211!150",
        
           "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!150",

           "@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items/$entity",

           "cTag": "aYzo3NUJGRTM3NEVCRUIxMjExITE1MC4yNTc",

           "children": [],
        
           "image": {
        
              "width": 883,
        
              "height": 431
        
           },
        
           "file": {
        
              "hashes": {
        
                 "sha1Hash": "68A4192BF9DEAD103D7E4EA481074745932989F4",
        
                 "crc32Hash": "6D98C9D5"
        
              },
        
              "mimeType": "image/jpeg"
        
           },   
        
           "fileSystemInfo": {
        
              "createdDateTime": "2015-12-02T20:25:26.51Z",
        
              "lastModifiedDateTime": "2015-12-08T21:51:15.593Z"
        
           },
        
           "createdDateTime": "2015-12-02T20:25:26.51Z",
        
           "size": 83736,
        
           "photo": {
        
              "takenDateTime": "2013-04-17T14:32:26Z"
        
           },
        
           "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExNTAuMTE",
        
           "name": "elect-a.jpg",
        
           "@content.downloadUrl": "https://public-ch3302.files.1drv.com/y3mnrbLFOgJJ8JQA7Ots0pzvL0xHYJx9NQJylS6IoQqp5G2CIIG5IWCKT_ADdp035kbr3qEmz6Va5j8-NCplk4ZMG_cYipxUfhP-NNl-SjlKocwc7yDplc1qWEynHGm_lME_o98pKSxNg6sKbEphRPufHea_h7LU1XH2qkFEGOIZGHQlw_JmH9fvygq8_XY2iE-",
        
           "children@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items('75BFE374EBEB1211%21150')/children",
        
           "parentReference": {
        
              "id": "75BFE374EBEB1211!107",
        
              "driveId": "75bfe374ebeb1211",
        
              "path": "/drive/root:"
        
           },
        
           "lastModifiedDateTime": "2015-12-08T21:51:15.593Z"
    }


@pytest.fixture
def file_metadata():
    return {
           "id": "75BFE374EBEB1211!150",
        
           "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!150",

           "@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items/$entity",

           "cTag": "aYzo3NUJGRTM3NEVCRUIxMjExITE1MC4yNTc",

           "children": [],
        
           "image": {
        
              "width": 883,
        
              "height": 431
        
           },
        
           "file": {
        
              "hashes": {
        
                 "sha1Hash": "68A4192BF9DEAD103D7E4EA481074745932989F4",
        
                 "crc32Hash": "6D98C9D5"
        
              },
        
              "mimeType": "image/jpeg"
        
           },   
        
           "fileSystemInfo": {
        
              "createdDateTime": "2015-12-02T20:25:26.51Z",
        
              "lastModifiedDateTime": "2015-12-08T21:51:15.593Z"
        
           },
        
           "createdDateTime": "2015-12-02T20:25:26.51Z",
        
           "size": 83736,
        
           "photo": {
        
              "takenDateTime": "2013-04-17T14:32:26Z"
        
           },
        
           "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExNTAuMTE",
        
           "name": "elect-a.jpg",
        
           "@content.downloadUrl": "https://public-ch3302.files.1drv.com/y3mnrbLFOgJJ8JQA7Ots0pzvL0xHYJx9NQJylS6IoQqp5G2CIIG5IWCKT_ADdp035kbr3qEmz6Va5j8-NCplk4ZMG_cYipxUfhP-NNl-SjlKocwc7yDplc1qWEynHGm_lME_o98pKSxNg6sKbEphRPufHea_h7LU1XH2qkFEGOIZGHQlw_JmH9fvygq8_XY2iE-",
        
           "children@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items('75BFE374EBEB1211%21150')/children",
        
           "parentReference": {
        
              "id": "75BFE374EBEB1211!107",
        
              "driveId": "75bfe374ebeb1211",
        
              "path": "/drive/root:/ryan-test1"
        
           },
        
           "lastModifiedDateTime": "2015-12-08T21:51:15.593Z"
    }


@pytest.fixture
def revisions_list_metadata():
    return {        
#        "@odata.deltaLink": "https://api.onedrive.com/v1.0/drives('me')/items('75BFE374EBEB1211!132')/view.delta?$top=250&token=aTE09NjM1ODU0NDA1ODYxNDc7SUQ9NzVCRkUzNzRFQkVCMTIxMSExMzI7TFI9NjM1ODU0NDIzNjQ1NTA7RVA9NTtTTz0y",
#     
#        "@delta.token": "aTE09NjM1ODU0NDA1ODYxNDc7SUQ9NzVCRkUzNzRFQkVCMTIxMSExMzI7TFI9NjM1ODU0NDIzNjQ1NTA7RVA9NTtTTz0y",
#     
#        "@odata.context": "https://api.onedrive.com/v1.0/$metadata#drives('me')/items",
#     
#        "value": [
#     
#                   {
#             
#                      "lastModifiedDateTime": "2015-12-11T14:23:06.143Z",
#             
#                      "name": "elect.jpg",
#             
#                      "size": 83736,
#             
#                      "file": {
#             
#                         "hashes": {
#             
#                            "sha1Hash": "68A4192BF9DEAD103D7E4EA481074745932989F4",
#             
#                            "crc32Hash": "6D98C9D5"
#             
#                         },
#             
#                         "mimeType": "image/jpeg; charset=UTF-8"
#             
#                      },
#             
#                         "user": {
#             
#                            "id": "75bfe374ebeb1211",
#             
#                            "displayName": "Ryan Casey",
#             
#                            "thumbnails": {
#             
#                               "source": {
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:WebReady"
#             
#                               },
#             
#                               "small": {
#             
#                                  "height": 96,
#             
#                                  "width": 96,
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileStatic"
#             
#                               },
#             
#                               "medium": {
#             
#                                  "height": 180,
#             
#                                  "width": 180,
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileMedium"
#             
#                               },
#             
#                               "large": {
#             
#                                  "height": 1198,
#             
#                                  "width": 1198,
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileCroppedOriginal"
#             
#                               }
#             
#                            }
#             
#                         }
#             
#                      },
#             
#                      "cTag": "aYzo3NUJGRTM3NEVCRUIxMjExITEzMi4yNTc",
#             
#                      "eTag": "aNzVCRkUzNzRFQkVCMTIxMSExMzIuMw",
#             
#                      "createdDateTime": "2015-12-01T11:38:59.073Z",
#             
#                      "id": "75BFE374EBEB1211!132",
#             
#                      "webUrl": "https://onedrive.live.com/redir?resid=75BFE374EBEB1211!132",
#             
#                         "user": {
#             
#                            "id": "75bfe374ebeb1211",
#             
#                            "displayName": "Ryan Casey",
#             
#                            "thumbnails": {
#             
#                               "source": {
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:WebReady"
#             
#                               },
#             
#                               "small": {
#             
#                                  "height": 96,
#             
#                                  "width": 96,
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileStatic"
#             
#                               },
#             
#                               "medium": {
#             
#                                  "height": 180,
#             
#                                  "width": 180,
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileMedium"
#             
#                               },
#             
#                               "large": {
#             
#                                  "height": 1198,
#             
#                                  "width": 1198,
#             
#                                  "url": "https://storage.live.com/users/0x75bfe374ebeb1211/myprofile/expressionprofile/profilephoto:UserTileCroppedOriginal"
#             
#                               }
#             
#                            }
#             
#                         },
#             
#                         "application": {
#             
#                            "id": "4416c3d3",
#             
#                            "displayName": "GT OSF OneDrive",
#             
#                            "thumbnails": {
#             
#                               "small": {
#             
#                                  "height": 50,
#             
#                                  "width": 50,
#             
#                                  "url": "https://public-sn3302.files.1drv.com/y3atLEyz-EB17OzMbWyJzwu39hoELyHbCjb13GdM4Jeq5vEVLllH7jt4ftWt4nvvsiT5UNQJTPdirhWACyo92cbGASFxSER2MCuTQKTtVi-Yvo09ENEPhScewG0sNMEqRun?psid=1"
#             
#                               }
#             
#                            }
#             
#                         }
#             
#                      },
#             
#                      "parentReference": {
#             
#                         "id": "75BFE374EBEB1211!128",
#             
#                         "driveId": "75bfe374ebeb1211"
#             
#                      },
#             
#                      "image": {
#             
#                         "height": 431,
#             
#                         "width": 883
#             
#                      },
#             
#                      "fileSystemInfo": {
#             
#                         "lastModifiedDateTime": "2015-12-11T14:23:06.143Z",
#             
#                         "createdDateTime": "2015-12-01T11:38:59.073Z"
#             
#                      },
#             
#                      "photo": {
#             
#                         "takenDateTime": "2013-04-17T14:32:26Z"
#             
#                      },
#             
#                      "@content.downloadUrl": "https://public-ch3302.files.1drv.com/y3mmg9Mn_vgJJuNnZYfH0beiugywKP4oNs7_RuneBi3haXsFaM4559Xqa4eH8TtkY8zyIYGmLfHFIVwQNCCIHubhtfQkWOSJwHQb3ySJpL_Py8enRsDj4ZhpXOEzJrFDs2Nkd_xNIdLCury1UfAMXdI4HdRxazBaEXI_iG8kiujv23r-CNDonz_TLe3qSQcikyYa2NXs6QOeAkFnGExGnwbzw"
#             
#               }]
    }


# class TestValidatePath:
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_validate_v1_path_file(self, provider, file_metadata):
#         file_id = '5000948880'
# 
#         good_url = provider.build_url('files', file_id, fields='id,name,path_collection')
#         bad_url = provider.build_url('folders', file_id, fields='id,name,path_collection')
# 
#         aiohttpretty.register_json_uri('get', good_url, body=file_metadata['entries'][0], status=200)
#         aiohttpretty.register_uri('get', bad_url, status=404)
# 
#         try:
#             wb_path_v1 = yield from provider.validate_v1_path('/' + file_id)
#         except Exception as exc:
#             pytest.fail(str(exc))
# 
#         with pytest.raises(exceptions.NotFoundError) as exc:
#             yield from provider.validate_v1_path('/' + file_id + '/')
# 
#         assert exc.value.code == client.NOT_FOUND
# 
#         wb_path_v0 = yield from provider.validate_path('/' + file_id)
# 
#         assert wb_path_v1 == wb_path_v0
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_validate_v1_path_folder(self, provider, folder_object_metadata):
#         provider.folder = '0'
#         folder_id = '11446498'
# 
#         good_url = provider.build_url('folders', folder_id, fields='id,name,path_collection')
#         bad_url = provider.build_url('files', folder_id, fields='id,name,path_collection')
# 
#         aiohttpretty.register_json_uri('get', good_url, body=folder_object_metadata, status=200)
#         aiohttpretty.register_uri('get', bad_url, status=404)
#         try:
#             wb_path_v1 = yield from provider.validate_v1_path('/' + folder_id + '/')
#         except Exception as exc:
#             pytest.fail(str(exc))
# 
#         with pytest.raises(exceptions.NotFoundError) as exc:
#             yield from provider.validate_v1_path('/' + folder_id)
# 
#         assert exc.value.code == client.NOT_FOUND
# 
#         wb_path_v0 = yield from provider.validate_path('/' + folder_id + '/')
# 
#         assert wb_path_v1 == wb_path_v0

# 
# class TestDownload:
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_download(self, provider, file_metadata):
#         item = file_metadata['entries'][0]
#         path = WaterButlerPath('/triangles.txt', _ids=(provider.folder, item['id']))
# 
#         metadata_url = provider.build_url('files', item['id'])
#         content_url = provider.build_url('files', item['id'], 'content')
# 
#         aiohttpretty.register_json_uri('GET', metadata_url, body=item)
#         aiohttpretty.register_uri('GET', content_url, body=b'better', auto_length=True)
# 
#         result = yield from provider.download(path)
#         content = yield from result.read()
# 
#         assert content == b'better'
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_download_not_found(self, provider, file_metadata):
#         item = file_metadata['entries'][0]
#         path = WaterButlerPath('/vectors.txt', _ids=(provider.folder, None))
#         metadata_url = provider.build_url('files', item['id'])
#         aiohttpretty.register_uri('GET', metadata_url, status=404)
# 
#         with pytest.raises(exceptions.DownloadError) as e:
#             yield from provider.download(path)
# 
#         assert e.value.code == 404
# 
# 
# class TestUpload:
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_upload_create(self, provider, folder_object_metadata, folder_list_metadata, file_metadata, file_stream, settings):
#         path = WaterButlerPath('/newfile', _ids=(provider.folder, None))
# 
#         upload_url = provider._build_upload_url('files', 'content')
#         folder_object_url = provider.build_url('folders', path.parent.identifier)
#         folder_list_url = provider.build_url('folders', path.parent.identifier, 'items')
# 
#         aiohttpretty.register_json_uri('POST', upload_url, status=201, body=file_metadata)
# 
#         metadata, created = yield from provider.upload(file_stream, path)
# 
#         expected = OneDriveFileMetadata(file_metadata['entries'][0], path).serialized()
# 
#         assert metadata.serialized() == expected
#         assert created is True
#         assert path.identifier_path == metadata.path
#         assert aiohttpretty.has_call(method='POST', uri=upload_url)
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_upload_update(self, provider, folder_object_metadata, folder_list_metadata, file_metadata, file_stream, settings):
#         item = folder_list_metadata['entries'][0]
#         path = WaterButlerPath('/newfile', _ids=(provider.folder, item['id']))
#         upload_url = provider._build_upload_url('files', item['id'], 'content')
#         aiohttpretty.register_json_uri('POST', upload_url, status=201, body=file_metadata)
# 
#         metadata, created = yield from provider.upload(file_stream, path)
# 
#         expected = OneDriveFileMetadata(file_metadata['entries'][0], path).serialized()
# 
#         assert metadata.serialized() == expected
#         assert created is False
#         assert aiohttpretty.has_call(method='POST', uri=upload_url)
# 
# 
# class TestDelete:
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_delete_file(self, provider, file_metadata):
#         item = file_metadata['entries'][0]
#         path = WaterButlerPath('/{}'.format(item['name']), _ids=(provider.folder, item['id']))
#         url = provider.build_url('files', path.identifier)
# 
#         aiohttpretty.register_uri('DELETE', url, status=204)
# 
#         yield from provider.delete(path)
# 
#         assert aiohttpretty.has_call(method='DELETE', uri=url)
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_delete_folder(self, provider, folder_object_metadata):
#         item = folder_object_metadata
#         path = WaterButlerPath('/{}/'.format(item['name']), _ids=(provider.folder, item['id']))
#         url = provider.build_url('folders', path.identifier, recursive=True)
# 
#         aiohttpretty.register_uri('DELETE', url, status=204)
# 
#         yield from provider.delete(path)
# 
#         assert aiohttpretty.has_call(method='DELETE', uri=url)
# 
#     @async
#     def test_must_not_be_none(self, provider):
#         path = WaterButlerPath('/Goats', _ids=(provider.folder, None))
# 
#         with pytest.raises(exceptions.NotFoundError) as e:
#             yield from provider.delete(path)
# 
#         assert e.value.code == 404
#         assert str(path) in e.value.message



class TestMoveOperations:

#     @async
#     def test_must_not_be_none(self, provider):
#         path = WaterButlerPath('/Goats', _ids=(provider.folder, None))
# 
#         with pytest.raises(exceptions.NotFoundError) as e:
#             yield from provider.metadata(path)
# 
#         assert e.value.code == 404
#         assert str(path) in e.value.message

    @async
    @pytest.mark.aiohttpretty
    def test_rename_file(self, provider, folder_object_metadata, folder_list_metadata):
#         dest_path::WaterButlerPath('/elect-b.jpg', prepend='75BFE374EBEB1211!128') srcpath:WaterButlerPath('/75BFE374EBEB1211!132', prepend='75BFE374EBEB1211!128')
        dest_path = WaterButlerPath('/elect-b.jpg', prepend='75BFE374EBEB1211!128')
        src_path = WaterButlerPath('/75BFE374EBEB1211!132', prepend='75BFE374EBEB1211!128')
        
#         logger.info('test_metadata path:{} provider.folder:{} provider:'.format(repr(path), repr(provider.folder), repr(provider)))

        list_url = provider.build_url(str(src_path))

        aiohttpretty.register_json_uri('PATCH', list_url, body=folder_object_metadata)

        result = yield from provider.intra_move(provider, src_path, dest_path)
        
        assert result is not None
        

    @async
    @pytest.mark.aiohttpretty
    def test_rename_folder(self, provider, folder_object_metadata, folder_list_metadata):
#         dest_path::WaterButlerPath('/elect-b.jpg', prepend='75BFE374EBEB1211!128') srcpath:WaterButlerPath('/75BFE374EBEB1211!132', prepend='75BFE374EBEB1211!128')
        dest_path = WaterButlerPath('/foo-bar', prepend='75BFE374EBEB1211!128')
        src_path = WaterButlerPath('/75BFE374EBEB1211!132', prepend='75BFE374EBEB1211!128')
        
#         logger.info('test_metadata path:{} provider.folder:{} provider:'.format(repr(path), repr(provider.folder), repr(provider)))

        list_url = provider.build_url(str(src_path))

        aiohttpretty.register_json_uri('PATCH', list_url, body=folder_object_metadata)

        result = yield from provider.intra_move(provider, src_path, dest_path)
        
        assert result is not None       

class TestMetadata:

#     @async
#     def test_must_not_be_none(self, provider):
#         path = WaterButlerPath('/Goats', _ids=(provider.folder, None))
# 
#         with pytest.raises(exceptions.NotFoundError) as e:
#             yield from provider.metadata(path)
# 
#         assert e.value.code == 404
#         assert str(path) in e.value.message

#      @async
#      @pytest.mark.aiohttpretty
#      def test_metadata_root(self, provider, folder_object_metadata, folder_list_metadata):
#          path = WaterButlerPath('/0/', _ids=(0, ))
#          logger.info('test_metadata path:{} provider.folder:{} provider:'.format(repr(path), repr(provider.folder), repr(provider)))
#  
#          list_url = provider.build_url('root', expand='children')
#  
#          aiohttpretty.register_json_uri('GET', list_url, body=folder_list_metadata)
#  
#          result = yield from provider.metadata(path)
#  
#          assert len(result) == 3
        
#      @async
#      @pytest.mark.aiohttpretty
#      def test_metadata_file_root_parent(self, provider, folder_object_metadata, file_root_parent_metadata):
#          path = WaterButlerPath('/75BFE374EBEB1211!129/', _ids=(provider.folder, ))
#          logger.info('test_metadata path:{} provider.folder:{} provider:'.format(repr(path), repr(provider.folder), repr(provider)))
#  
#          list_url = provider.build_url('75BFE374EBEB1211!129', expand='children')
#  
#          aiohttpretty.register_json_uri('GET', list_url, body=file_root_parent_metadata)
#  
#          result = yield from provider.metadata(path)
#          logger.info('result:: {}'.format(repr(result)))
#  
#          assert '/{}'.format(file_root_parent_metadata['id']) == result.path        
#      
    @pytest.mark.aiohttpretty
    def test_metadata_file_root_parent_names(self, provider, folder_object_metadata, file_root_parent_metadata):
        result = provider._get_names(file_root_parent_metadata)

        assert result == '/elect-a.jpg'

#      @async
#      @pytest.mark.aiohttpretty
#      def test_metadata_sub_folder(self, provider, folder_object_metadata, folder_list_metadata):
#          path = WaterButlerPath('/foo/', _ids=(provider.folder, ))
#          logger.info('test_metadata path:{} provider.folder:{} provider:'.format(repr(path), repr(provider.folder), repr(provider)))
#  
#          list_url = provider.build_url('foo', expand='children')
#  
#          aiohttpretty.register_json_uri('GET', list_url, body=folder_list_metadata)
#  
#          result = yield from provider.metadata(path)
#  
#          assert len(result) == 3


#     @async
#     @pytest.mark.aiohttpretty
#     def test_metadata_nested(self, provider, file_metadata):
#         item = file_metadata['entries'][0]
#         path = WaterButlerPath('/name.txt', _ids=(provider, item['id']))
# 
#         file_url = provider.build_url('files', path.identifier)
#         aiohttpretty.register_json_uri('GET', file_url, body=item)
# 
#         result = yield from provider.metadata(path)
# 
#         expected = OneDriveFileMetadata(item, path)
#         assert result == expected
#         assert aiohttpretty.has_call(method='GET', uri=file_url)
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_metadata_missing(self, provider):
#         path = WaterButlerPath('/Something', _ids=(provider.folder, None))
# 
#         with pytest.raises(exceptions.NotFoundError):
#             yield from provider.metadata(path)

# 
# class TestRevisions:
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_get_revisions(self, provider, file_metadata, revisions_list_metadata):
#         item = file_metadata['entries'][0]
# 
#         path = WaterButlerPath('/name.txt', _ids=(provider, item['id']))
# 
#         file_url = provider.build_url('files', path.identifier)
#         revisions_url = provider.build_url('files', path.identifier, 'versions')
# 
#         aiohttpretty.register_json_uri('GET', file_url, body=item)
#         aiohttpretty.register_json_uri('GET', revisions_url, body=revisions_list_metadata)
# 
#         result = yield from provider.revisions(path)
# 
#         expected = [
#             OneDriveRevision(each)
#             for each in [item] + revisions_list_metadata['entries']
#         ]
# 
#         assert result == expected
#         assert aiohttpretty.has_call(method='GET', uri=file_url)
#         assert aiohttpretty.has_call(method='GET', uri=revisions_url)
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_get_revisions_free_account(self, provider, file_metadata):
#         item = file_metadata['entries'][0]
#         path = WaterButlerPath('/name.txt', _ids=(provider, item['id']))
# 
#         file_url = provider.build_url('files', path.identifier)
#         revisions_url = provider.build_url('files', path.identifier, 'versions')
# 
#         aiohttpretty.register_json_uri('GET', file_url, body=item)
#         aiohttpretty.register_json_uri('GET', revisions_url, body={}, status=403)
# 
#         result = yield from provider.revisions(path)
#         expected = [OneDriveRevision(item)]
#         assert result == expected
#         assert aiohttpretty.has_call(method='GET', uri=file_url)
#         assert aiohttpretty.has_call(method='GET', uri=revisions_url)

# 
# class TestCreateFolder:
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_must_be_folder(self, provider):
#         path = WaterButlerPath('/Just a poor file from a poor folder', _ids=(provider.folder, None))
# 
#         with pytest.raises(exceptions.CreateFolderError) as e:
#             yield from provider.create_folder(path)
# 
#         assert e.value.code == 400
#         assert e.value.message == 'Path must be a directory'
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_id_must_be_none(self, provider):
#         path = WaterButlerPath('/Just a poor file from a poor folder/', _ids=(provider.folder, 'someid'))
# 
#         assert path.identifier is not None
# 
#         with pytest.raises(exceptions.FolderNamingConflict) as e:
#             yield from provider.create_folder(path)
# 
#         assert e.value.code == 409
#         assert e.value.message == 'Cannot create folder "Just a poor file from a poor folder" because a file or folder already exists at path "/Just a poor file from a poor folder/"'
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_already_exists(self, provider):
#         url = provider.build_url('folders')
#         data_url = provider.build_url('folders', provider.folder)
#         path = WaterButlerPath('/50 shades of nope/', _ids=(provider.folder, None))
# 
#         aiohttpretty.register_json_uri('POST', url, status=409)
#         aiohttpretty.register_json_uri('GET', data_url, body={
#             'id': provider.folder,
#             'type': 'folder',
#             'name': 'All Files',
#             'path_collection': {
#                 'entries': []
#             }
#         })
# 
#         with pytest.raises(exceptions.FolderNamingConflict) as e:
#             yield from provider.create_folder(path)
# 
#         assert e.value.code == 409
#         assert e.value.message == 'Cannot create folder "50 shades of nope" because a file or folder already exists at path "/50 shades of nope/"'
# 
#     @async
#     @pytest.mark.aiohttpretty
#     def test_returns_metadata(self, provider, folder_object_metadata):
#         url = provider.build_url('folders')
#         folder_object_metadata['name'] = '50 shades of nope'
#         path = WaterButlerPath('/50 shades of nope/', _ids=(provider.folder, None))
# 
#         aiohttpretty.register_json_uri('POST', url, status=201, body=folder_object_metadata)
# 
#         resp = yield from provider.create_folder(path)
# 
#         assert resp.kind == 'folder'
#         assert resp.name == '50 shades of nope'
#         assert resp.path == '/{}/'.format(folder_object_metadata['id'])
#         assert isinstance(resp, OneDriveFolderMetadata)
#         assert path.identifier_path == '/' + folder_object_metadata['id'] + '/'
