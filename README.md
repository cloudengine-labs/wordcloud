# Wordcloud Python Project
This python program can be used to generate a "WordCloud" image from the given `sample_text`

## Tasks
- [x] Application to generate WordCloud
- [x] Creating container image for the app
- [ ] TODO: Upload the file wordcloud.png to GitHub or Cloud Storage
- [x] Pass text as input argument to the script

## Possible Enhancements
- Upload generated images directly to cloud storage (GCS/S3/Azure Blob) via optional flags.
- Add support for custom font, color map, and stopwords through CLI options.
- Add CI checks for linting + script execution on pull requests.
- Add automated tests for argument parsing and file output generation.
- Add API mode (Flask/FastAPI) to generate word clouds via HTTP requests.

## Executing the Script
### Method 1
- Run below command to execute the program with default sample text:
```
python3 -m pip install -r requirements.txt
python3 show_wordcloud.py
```

- Pass inline text:
```
python3 show_wordcloud.py --text "GitHub Actions GitHub Packages Protected branches"
```

- Pass text from a file:
```
python3 show_wordcloud.py --text-file /path/to/input.txt --output /path/to/wordcloud.png
```

- You can also set a custom output file:
```
python3 show_wordcloud.py --text "example text" --output mycloud.png
```

### Method 2
**Docker Container method**
- Use the below commands to `build` and `run` the image locally
```
docker buildx build -f Dockerfile -t gsdockit/wordcloud:localtest .
docker run -d gsdockit/wordcloud:localtest
```
- While running as Docker container, the output file will be saved inside the container. 
- You can use the following command to copy the file from container to host machine
```
docker cp <ContainerID-NAME-or-HASH>:/app/wordcloud.png /host/path/target/location
```

- Get the container ID using the command below
```
$ docker container ls -a
CONTAINER ID   IMAGE                          COMMAND                  CREATED         STATUS                     PORTS     NAMES
0defc9c86375   gsdockit/wordcloud:localtest   "python3 show_wordcl…"   3 minutes ago   Exited (0) 3 minutes ago             distracted_liskov
```

- Example 1: `docker cp 0defc9c86375:/app/wordcloud.png /home/wordcloud.png`
- Example 2: `docker cp <ContainerID-NAME-or-HASH>:/app/wordcloud.png .`
