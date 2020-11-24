# ImageNamePipeline
This is an example of a pipeline that lets you configure which name gets set for downloaded images. 
ImageNamePipeline is a sub class of [ImagesPipeline](https://doc.scrapy.org/en/latest/_modules/scrapy/pipelines/images.html).

## Settings
To enable the pipeline in your project you need to set [ITEM_PIPELINES](https://docs.scrapy.org/en/latest/topics/item-pipeline.html#activating-an-item-pipeline-component) in [settings.py](https://docs.scrapy.org/en/latest/topics/settings.html)

```python
ITEM_PIPELINES = {
    'your_project.pipelines.ImageNamePipeline': 200,
}
```

Also you need to define IMAGE_URL_FIELDS in `settings.py` or your settings object as a Dictionary in the following format:

```python
IMAGE_URL_FIELDS = {
    'your_items_image_url_field': {
        'name_field': 'item_field_used_to_name_image',
        'sub_folder': 'folder_to_which_file_gets_downloaded',
        'path_field': 'item_field_to_store_image_paths'
    }, 'second_image_url_field': {
        'name_field': 'name',
        'sub_folder': 'folder',
        'path_field': 'path_field'
    }
}
```

You can also specify a field `base_url` if necessary, since the pipeline can't handle relative urls. 

```python
IMAGE_URL_FIELDS = {
    'your_items_image_url_field': {
        ...
        'base_url': 'http://example.com'
    }
}

```

## Additional information
You cannot use ImagesPipelines [IMAGE_URLS_FIELD](https://docs.scrapy.org/en/latest/topics/media-pipeline.html?highlight=IMAGE_URLS_FIELD#std-setting-IMAGES_URLS_FIELD) with this sub class. You need to either implement `IMAGES_RESULT_FIELD` or provide the standard field `images` in your Item.  
