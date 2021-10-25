# DEPRECATED

# Brief how to use

## files to run
- main.py

## build docker
 docker build --pull --rm -f "Dockerfile" -t tafetimetable:latest .

## run in docker
docker run -e DISCORD_KEY_SPRING=your_key_here tafetimetable
