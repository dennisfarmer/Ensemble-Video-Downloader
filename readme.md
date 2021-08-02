# Ensemblevideo Link Converter 

[![LICENSE](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://raw.githubusercontent.com/dennisfarmer/Ensemble-Video-Downloader/master/LICENSE)

Down

### Requirements:
`pyperclip, PyQt5`

### Use:

**Shell:**

```zsh
python install.py
python app.py
```

**Windows 10:**

run `install.py` with Python to install requirements (first time only)

then run `app.py` to launch application

Press enter to grab clipboard link, convert to downloadable format, then copy new link to clipboard, or q then enter to exit.

#### Before (yucky):
```
https://washtenaw.ensemblevideo.com/hapi/v1/contents/d5cedd1f-a75c-449f-8000-e4f16773d456/launch?idn_playlist=ec4d8686-acfc-44d5-b689-a9ec72a1abc0&idn_init=False&idn_sig=prmGHSxKawTxeGmNOdXKdOX1LGA%3D&?displayTitle=true&startTime=0&autoPlay=true&hideControls=False&showCaptions=False&displaySharing=False&displayAnnotations=True&displayAttachments=True&displayLinks=True&displayDownloadIcon=False&displayMetaData=true&displayEmbedCode=True&audioPreviewImage=False&displayCaptionSearch=True&displayViewersReport=False&displayAxdxs=False&forceDisplayAdsOff=False&embedAsThumbnail=False&playlistId=&displayCredits=False&isJavaScriptEmbed=False&isContentPreview=False&isResponsive=False&useFourByThreeRatio=False&isJavascriptInIframe=False
```
![Before](Before.png)

#### After (less yucky):
```
https://washtenaw.ensemblevideo.com/hapi/v1/contents/d5cedd1f-a75c-449f-8000-e4f16773d456/launch?&displayDownloadIcon=True
```
![After](After.png)


