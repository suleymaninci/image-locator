# Image Template Locator

This image template locator program locates the template image in original image. It gives rectangle highlighted original image and 4-point location information. Additionally, there are some command line options:

- optional `--template` flag which changes template image. Default is ./images/Small_area.png

- optional `--image` flag which changes original image. Default is ./images/StarMap.png

#### Python usage
` $ python3 main.py --template="your template directory" --image="your org. image directory" `

### Sample Output
```
$ python3 main.py --template=images/Small_area.png --image=StarMap.png
template: images/Small_area.png
Location: 855:969,150:264
```

<img src="https://github.com/suleymaninci/image-locator/raw/main/images/ss.jpg" width="600" height="450">
