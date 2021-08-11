# youtube_thumbnail

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/youtube_thumbnail)
![PyPI](https://img.shields.io/pypi/v/youtube_thumbnail)
![Travis (.org)](https://img.shields.io/travis/animesh-chouhan/youtube_thumbnail)
![license](https://img.shields.io/github/license/animesh-chouhan/youtube_thumbnail)

> CLI tool to download YouTube thumbnails

## Usage

IMPORTANT: Enclose URL in single quotes

```sh
youtube_thumbnail [-h] [-o FILE] url
```
Example:

```sh
youtube_thumbnail 'https://youtu.be/dQw4w9WgXcQ' -o best_meme_ever
```

![preview](https://raw.githubusercontent.com/animesh-chouhan/youtube_thumbnail/main/assets/preview.png)


## Setup

### Cloning the repository:
```sh
# Clone the repo
git clone https://github.com/animesh-chouhan/youtube_thumbnail.git
cd youtube_thumbnail

# Run the command
python3 -m youtube_thumbnail 'https://youtu.be/dQw4w9WgXcQ'
```
### Running tests
```sh
# If in vc-creator folder
cd youtube_thumbnail/tests

# Run the test
python3 test_youtube_thumbnail.py
```

### Installation:

To install it right away, type:
```sh
pip3 install youtube_thumbnail
```

### Help:
```sh
python3 -m youtube_thumbnail --help
```
OR

```sh
youtube_thumbnail --help
```

## Contributing

1. Fork the repo (<https://github.com/animesh-chouhan/youtube_thumbnail/>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[license]: https://img.shields.io/github/license/animesh-chouhan/youtube_thumbnail
[wiki]: https://github.com/animesh-chouhan/youtube_thumbnail/wiki

## License
MIT License
copyright (c) 2021 [Animesh Singh Chouhan](https://github.com/animesh-chouhan). Please have a look at the [license](LICENSE) for more details.
