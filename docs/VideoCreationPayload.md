# VideoCreationPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of your new video. | 
**description** | **str** | A brief description of your video. | [optional] 
**source** | **str** | If you add a video already on the web, this is where you enter the url for the video. | [optional] 
**public** | **bool** | Whether your video can be viewed by everyone, or requires authentication to see it. A setting of false will require a unique token for each view. | [optional]  if omitted the server will use the default value of True
**panoramic** | **bool** | Indicates if your video is a 360/immersive video. | [optional]  if omitted the server will use the default value of False
**mp4_support** | **bool** | Enables mp4 version in addition to streamed version. | [optional]  if omitted the server will use the default value of True
**player_id** | **str** | The unique identification number for your video player. | [optional] 
**tags** | **[str]** | A list of tags you want to use to describe your video. | [optional] 
**metadata** | [**[Metadata]**](Metadata.md) | A list of key value pairs that you use to provide metadata for your video. These pairs can be made dynamic, allowing you to segment your audience. You can also just use the pairs as another way to tag and categorize your videos. | [optional] 
**published_at** | **datetime** | The API uses ISO-8601 format for time, and includes 3 places for milliseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

